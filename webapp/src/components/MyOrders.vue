<template>
  <div class="container">
    <ul class="list-group">
      <li class="list-group-item" v-for="item in items">
        <span>{{extract('title', item)}}</span>
        <span class="text-right">{{item.status}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "MyOrders",
    data() {
      return {
        items: []
      }
    },
    mounted() {
      axios.get('/my-orders/').then(res => {
        this.items = res.data
      })
    },
    methods:{
      extract(what, item){
        let obj = JSON.parse(item.json_received)
        let order = obj['order']
        if (order && order['line_items']){
          return order['line_items'][0][what]
        }
        return "Error"
      },
    }
  }

</script>

<style scoped>

</style>
