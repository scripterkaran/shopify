// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import '@/assets/bootstrap.min.css'
import store from './store/index'

Vue.config.productionTip = false

axios.defaults.baseURL = '/api'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

axios.interceptors.request.use(function (config) {
  config.withCredentials = true
  return config;
}, function (error) {
  return Promise.reject(error);
});


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
