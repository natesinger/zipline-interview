<template>
  <div class="content-pane"></div>
</template>

<script>
export default {
  name: 'FlightControl',
  components: {},
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.content-pane {
  width: 100%;
  background-color: $color-light-5;
  height: 75px;
  margin: 0;
  border-radius: 10px;
}
</style>
