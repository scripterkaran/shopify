<template>
  <div id="app">
    <div class="header">
      <div class="col-xs-6 flex al-it-ce">
      <span class="flex">
        <img src="https://www.materialui.co/materialIcons/navigation/chevron_left_black_192x192.png" @click="goBack()" class="back">
        <div  @click="$router.push({path:'/'})">Mishipay Shopify</div>
      </span>
      </div>
      <div class="col-xs-6 flex al-it-ce">
        <div class="flex-grow" @click="$router.push({'name': 'MyOrders'})"><div class="pull-right">My Orders</div></div>
      </div>
    </div>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods:{
    goBack(){
      window.location.href = '/'
    }
  }
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

/*main {*/
  /*text-align: center;*/
  /*margin-top: 40px;*/
/*}*/

.header {
  margin: 0;
  height: 56px;
  padding: 0 16px 0 24px;
  background-color: #35495E;
  color: #ffffff;
  display: flex;
}
.flex {
  display: flex;
}
.al-it-ce{
  align-items: center;
}
.flex-grow{
  flex-grow: 1;
}

/*header span {*/
  /*display: block;*/
  /*position: relative;*/
  /*font-size: 20px;*/
  /*line-height: 1;*/
  /*letter-spacing: .02em;*/
  /*font-weight: 400;*/
  /*box-sizing: border-box;*/
  /*padding-top: 16px;*/
/*}*/
  .back{
    height: 20px;
  }
</style>

