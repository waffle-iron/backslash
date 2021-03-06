import Ember from 'ember';

export default Ember.Component.extend({
  entered_search: null,
  search: null,

  init() {
    this._super(...arguments);
    this.set('entered_search', this.get('search'));
  },

  actions: {
    search() {
      let entered_search = this.get("entered_search");
      if (entered_search !== this.get('search')) {
        this.set('searching', true);
      }
      this.set("search", entered_search);
    }
  }
});
