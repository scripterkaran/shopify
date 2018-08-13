import Vue from 'vue'
import Router from 'vue-router'
import ProductList from '@/components/ProductList.vue'
import ProductDetail from '@/components/ProductDetail.vue'
import Cart from '@/components/Cart.vue'
import MyOrders from '@/components/MyOrders.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ProductList',
      component: ProductList
    },
    {
      path: '/product/:id',
      name: 'ProductDetail',
      component: ProductDetail
    },
    // {
    //   path: '/cart',
    //   name: 'Cart',
    //   component: Cart
    // },
    {
      path: '/my-orders',
      name: 'MyOrders',
      component: MyOrders,
    }
  ]
})
