<template>
  <div class="container">
    <div v-show="loading" class="text-center loader">Loading.....</div>
    <div v-show="!loading" class="row">
      <div class="title">{{item.title}}</div>
      <div class="col-md-4"><img :src="displayImage"></div>
      <div class="col-md-8">
        <div class="col-md-6 col-md-offset-3">
          <label>Select Variant</label>
          <select v-model="selectedVariantId" class="form-control">
            <option v-for="variant in item.variants" :value="variant.id">
              {{variant.title}}
            </option>
          </select>
        </div>
        <div class="col-md-6 col-md-offset-3">
          <label for="quantity">Quantity</label>
          <input id="quantity" type="number" min="0" required v-model="quantity" class="form-control"><br>
          <div>Price: {{calculatedPrice}}</div>
          <button class="btn btn-success" :disabled="buttonLoading" @click="buyNow">{{  buttonLoading ? 'Placing order..': 'Buy Now'}}</button>
          <!--<button class="btn btn-success" :disabled="buttonLoading" @click="addProductToCart">{{  buttonLoading ? 'Placing order..': 'Add to Cart'}}</button>-->
        </div>
        <div class="clearfix"></div>
        <p></p>
        <div v-show="error" class="alert alert-danger">{{message}}</div>
        <div v-show="success" class="alert alert-success">{{message}}</div>
      </div>
    </div>
  </div>
</template>

<script>
  import client from '../services/client.js'
  import axios from 'axios'
  import {mapMutations} from 'vuex'
  import * as _ from 'lodash'

  export default {
    data() {
      return {
        item: {
          variants: []
        },
        quantity: 1,
        selectedVariantId: null,
        success: false,
        error: false,
        message: '',
        loading: true,
        buttonLoading : false,
      }
    },
    mounted() {
      let productId = this.$router.currentRoute.params.id
      // client.product.fetch(productId).then((product) => {
      //   this.item = product
      // });
      axios.get(`products/${productId}/`).then(res => {
        this.item = res.data.product
        this.loading = false
      })
    },
    methods: {
      preCheck(){
        if(!this.selectedVariantId){
          alert('Please Select a variant')
          return false
        }
        return true
      },
      constructItem(){
        return {id: this.selectedVariantId, quantity: this.quantity, 'title': this.item.title}
      },
      buyNow() {
        if (!this.preCheck()){
          return
        }
        this.buttonLoading = true
        axios.post('orders/', {'items': [this.constructItem()]}).then(res => {
          this.success = true
          this.buttonLoading = false
          this.message = 'Order Placed'
        }).catch(err => {
          this.error = true
         this.buttonLoading = false
          this.message = 'Cannot Create Order'
        })
      },
      addProductToCart(){
        if (!this.preCheck()){
          return
        }
        this.addItems(this.constructItem())
        this.success = true
        this.message = "Added to cart"
      },
      ...mapMutations(['addItems'])
    },

    computed: {
      displayImage() {
        if (this.item.images && this.item.images.length > 0) {
          return this.item.images[0].src
        }
        return "http://via.placeholder.com/350x350"

      },
      calculatedPrice(){
        if (this.selectedVariantId){
          let obj =_.find(this.item.variants, {id: this.selectedVariantId})
          return parseInt(obj.price) * this.quantity
        }
      }
    }
  }
</script>

<style scoped>
  .title {
    font-size: 38px;
  }
  .loader{
    font-size: 24px;
  }

  img{
    width: 100%;
  }

</style>
