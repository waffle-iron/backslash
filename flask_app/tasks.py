from __future__ import absolute_import

from datetime import timedelta
import functools
import os
import sys

import logging
import logging.handlers
import logbook

from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
from celery.log import redirect_stdouts_to_logger


from .app import create_app
from . import models

_logger = logbook.Logger(__name__)


queue = Celery('tasks', broker=os.environ.get('BACKSLASH_CELERY_BROKER_URL', 'amqp://guest:guest@localhost'))
queue.conf.update(
    CELERY_ENABLE_UTC=True,
)

def setup_log(**args):
    logbook.StreamHandler(sys.stderr).push_application()

APP = None

def needs_app_context(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        global APP              # pylint: disable=global-statement

        if APP is None:
            APP = create_app(setup_logging=False)

        with APP.app_context():
            return f(*args, **kwargs)

    return wrapper


after_setup_logger.connect(setup_log)
after_setup_task_logger.connect(setup_log)
################################################################################

@queue.task
@needs_app_context
def do_live_migrate():
    pending = models.BackgroundMigration.query\
                                          .filter_by(finished=False)\
                                          .order_by(models.BackgroundMigration.id.asc()).all()
    if not pending:
        return

    migration = pending.pop(0)
    _logger.debug('Running migration: {.name}...', migration)
    migration.do_single_iteration()
    if not migration.finished or pending:
        do_live_migrate.delay()
