<template>
  <div class="order-pane">
    <div class="title">Future Orders ({{ futureOrders !== null ? futureOrders.length : 0 }})</div>
    <div class="order-container">
      <div v-if="futureOrders === null || futureOrders.length === 0" class="no-orders">
        <i>All orders have been dispatched.</i>
      </div>
      <div v-else v-for="order in futureOrders" :key="order.id" class="order">
        <div class="order-time">{{ formatTime(order.time) }}</div>
        <div class="order-status" :class="order.status === 'Emergency' ? 'emergency' : 'resupply'"
        >{{ order.status }}</div>
        <div class="order-destination">{{ order.destination }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderDisplay',
  components: {},
  props: {
    futureOrders: Array,
  },
  methods: {
    formatTime(seconds) {
      const hours = Math.floor(seconds / 3600);
      const minutes = Math.floor((seconds % 3600) / 60);

      const formattedHours = String(hours).padStart(2, '0');
      const formattedMinutes = String(minutes).padStart(2, '0');

      return `${formattedHours}:${formattedMinutes}`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.order-pane {
  margin-top: 15px;
  width: 350px;
  height: 316px;
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

  .no-orders {
    display: flex;
    justify-content: center;
  }

  .order {
    height: 30px;
    width: 100%;
    background-color: #dbdbdb;
    margin: 5px 0;
    border-radius: 5px;

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    .order-time {
      margin: 0 20px;
      font-weight: 600;
    }

    .order-destination {
      width: 75px;
      text-align: center;
      margin: 0 10px;
    }

    .order-status {
      height: 70%;
      min-width: 90px;
      margin: 0 10px;
      font-weight: 600;
      line-height: 14px;
      border-radius: 5px;

      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;

      &.emergency {
        color: #d11818;
      }

      &.resupply {
        color: #00860b;
      }
    }
  }
}
</style>
