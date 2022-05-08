import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

// Axios config
window.axios = axios;
axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;
axios.defaults.headers['content-type'] = 'application/json';
axios.defaults.withCredentials = true;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
