import Vue from 'vue';
import Vuex from 'vuex';
import alert from './modules/alert';
import corpora from './modules/corpora';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    alert,
    corpora,
  },
});
