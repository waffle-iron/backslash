import os

from slash import plugins
from slash import Session
from backslash.contrib.slash_plugin import BackslashPlugin

from contextlib import ExitStack

from slash.frontend.slash_run import slash_run


def run_suite(backslash_url, name='simple'):
    with ExitStack() as stack:

        plugin = BackslashPlugin(backslash_url, keepalive_interval=10)
        plugin.fetch_token(username='vmalloc@gmail.com', password='password')

        plugins.manager.install(plugin, activate=True)
        stack.callback(plugins.manager.uninstall, plugin)
        slash_run([os.path.join('_sample_suites', name), '--session-label', 'testing'])
