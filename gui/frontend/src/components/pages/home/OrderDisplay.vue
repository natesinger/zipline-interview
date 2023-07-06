<template>
  <div class="order-pane">
    <div class="title">Unfulfilled Orders ({{ openOrders.length }})</div>
    <div class="order-container">
      <div v-for="order in openOrders" :key="order.id" class="order"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderDisplay',
  components: {},
  props: {
    openOrders: Array,
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.order-pane {
  margin-top: 15px;
  width: 400px;
  height: calc((100% - 391px - 15px));
  background-color: $color-light-5;
  border-radius: 10px;

  .title {
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    border-bottom: 2px solid black;
    background-color: $color-light-4;
    border-radius: 5px 5px 0 0;
  }

  .order-container {
    overflow-y: scroll;
    height: 280px;
    padding: 0 5px;
  }

  .order {
    height: 30px;
    width: 100%;
    background-color: red;
    margin: 5px 0;
    border-radius: 5px;
  }

  /*.flight {
    height: 30px;
    width: 98%;
    margin-top: 5px;
    border-radius: 5px;

    background-color: #dbdbdb;
    display: flex;
    align-items: center;
    flex-direction: row;

    font-size: 16px;
    font-weight: 350;
    line-height: 16px;

    .flight-id {
      margin: 0 10px;
    }

    .flight-status {
      height: 70%;
      min-width: 90px;
      margin: 0 10px;
      font-size: 14px;
      font-weight: 500;
      line-height: 14px;
      border-radius: 5px;

      color: $color-light-1;

      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;

      &.deployed {
        background-color: #234faf;
        border: 2px solid  #152e64;
      }

      &.standby {
        background-color: #00860b;
        border: 2px solid  #005e08;
      }
    }

    .flight-destination {
      min-width: 80px;
      text-align: center;
    }

    .flight-cords {
      flex-grow: 1;
      text-align: right;
      margin: 0 10px;
    }
  }*/
}
</style>
