<template>
  <div class="zip-vehicle" :style="{
    bottom: positionY,
    left: positionX,
    transform: `rotate(-${rotationDeg}deg)`
    }" :class="hidden ? 'hidden' : ''">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M482.3 192c34.2 0 93.7 29 93.7 64c0 36-59.5 64-93.7 64l-116.6 0L265.2 495.9c-5.7 10-16.3 16.1-27.8 16.1l-56.2 0c-10.6 0-18.3-10.2-15.4-20.4l49-171.6L112 320 68.8 377.6c-3 4-7.8 6.4-12.8 6.4l-42 0c-7.8 0-14-6.3-14-14c0-1.3 .2-2.6 .5-3.9L32 256 .5 145.9c-.4-1.3-.5-2.6-.5-3.9c0-7.8 6.3-14 14-14l42 0c5 0 9.8 2.4 12.8 6.4L112 192l102.9 0-49-171.6C162.9 10.2 170.6 0 181.2 0l56.2 0c11.5 0 22.1 6.2 27.8 16.1L365.7 192l116.6 0z"/></svg>
  </div>
</template>

<script>
export default {
  name: 'ZipVehicle',
  components: {},
  props: {
    id: String,
    x: Number,
    y: Number,
    rotation: Number,
  },
  data() {
    return {
      positionX: 0,
      positionY: 0,
      rotationDeg: this.rotation,
      hidden: false,
    };
  },
  created() {
    this.position(this.x, this.y);
    if (this.x === 0 && this.y === 0) { this.hidden = true; }
  },
  methods: {
    position(x, y) {
      const xGridUnits = (x / 10000) + 6;
      const yGridUnits = (y / 10000) + 9;

      // each 1 GRID_CONST == 10k
      const GRID_CONST = 42;

      // +5 accounts for 30px wide in 40px grid
      this.positionY = `${(GRID_CONST * yGridUnits) - 20 + 5}px`;
      this.positionX = `${(GRID_CONST * xGridUnits) - 20 + 5}px`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.zip-vehicle {
  height: 30px;
  width: 30px;
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  z-index: 50;

  fill: $color-dark-1;

  .name-label {
    font-size: 12px;
    margin-top: 2px;
    padding: 2px 4px;
    line-height: 12px;
    background-color: rgb(231, 231, 231);
    border: 1px solid rgb(121, 121, 121);
    border-radius: 5px;
  }

  &.hidden {
    display: none;
  }
}

.zip-vehicle:hover {
  cursor: help;
}
</style>
