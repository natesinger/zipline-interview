<template>
  <div class="flight-pane">
    <div class="title">Flights</div>
      <div class="flight"></div>
  </div>
</template>

<script>
export default {
  name: 'FlightDisplay',
  components: {},
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.flight-pane {
  width: 400px;
  height: calc((100% - 15px)/2);
  background-color: $color-light-5;
  border-radius: 10px;

  .title {
    font-size: 16px;
    font-weight: 600;
    text-align: center;
    border-bottom: 2px solid black;
  }
}
</style>
