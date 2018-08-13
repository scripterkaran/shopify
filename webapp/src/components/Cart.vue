<template>
  <div class="container">
    <div class="list-group-item" v-for="item in cart.items">
      {{item.title}} - {{item.quantity}}
    </div>
    <button @click="createOrder">Create Order</button>
  </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex'

  export default {
    name: "Cart",
    computed: {
      ...mapState(['cart'])
    },
    methods: {

      ...mapActions(['createOrder']),
    }
  }
</script>

<style scoped>

</style>
