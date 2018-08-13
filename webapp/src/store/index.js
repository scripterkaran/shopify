import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    cart: {
      items: []
    }
  },
  mutations: {
    addItems(state, payload) {
      state.cart.items.push(payload)
    },
    emptyCart(state, payload) {
      state.cart.items = []
    }
  },
  actions: {
    createOrder() {
      return axios.post('orders/', {'items': this.state.cart.items})

    }
  }
})

export default store
