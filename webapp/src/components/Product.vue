<template>
  <div class="media">
    <div class="media-left"  @click="$emit('clicked', product)">
      <img :src="displayImage" style="width:60px">
    </div>
    <div class="media-body">
      <h4 class="media-heading">{{product.title}}</h4>
      <p>Lorem ipsum...</p>
    </div>
</div>
</template>

<script>
  export default {
    props: ['product'],
    computed: {
      displayImage() {
        if (this.product.images && this.product.images.length > 0) {
          return this.product.images[0].src
        }
        return "http://via.placeholder.com/350x350"
      }
    }
  }
</script>
