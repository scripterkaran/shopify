<template>
  <div class="container">
    <Product :product="item" v-for="item in items" @clicked="handleClick">
    </Product>
  </div>
</template>

<script>
  import Product from './Product.vue'
  import client from '../services/client.js'
  import axios from 'axios'

  export default {
    components: {Product},
    data() {
      return {
        items: []
      }
    },
    mounted() {
      // client.product.fetchAll().then((products) => {
      //   this.items = products
      // });
      axios.get('products/').then(res => {
        this.items = res.data.products
      })

    },
    methods: {
      createCheckout() {
        // client.checkout.create().then((checkout) => {
        //   // Do something with the checkout
        //   console.log(checkout);
        // });
      },
      handleClick(args) {
        this.$router.push({name: 'ProductDetail', params: {id: args.id}})
      }

    }

  }
</script>
