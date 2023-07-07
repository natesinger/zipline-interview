<template>
  <div class="flight-pane">
    <div class="title">Vehicle Status</div>
    <div class="flights">
      <div v-if="flights === null" class="no-flights"></div>
      <div v-else v-for="flight in sortFlights(flights)" :key="flight" class="flight">
        <div class="flight-status"
        :class="flight.status === 'deployed' ? 'deployed' : 'standby'"
        >{{ flight.status.toUpperCase() }}</div>
        <div class="flight-destination">{{ flight.destination }}</div>
        <div class="flight-cords">
          {{ flight.x }}, {{ flight.y }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FlightDisplay',
  components: {},
  props: {
    flights: Object,
  },
  methods: {
    sortFlights(flights) {
      const flightsSorted = flights.sort((a, b) => a.status.localeCompare(b.status));
      return flightsSorted;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.flight-pane {
  width: 400px;
  height: 391px;
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

  .flights {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 5px;
  }

  .flight {
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
  }
}
</style>
