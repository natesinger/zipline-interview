<template>
  <div class="hospital-base" :style="{top: positionY, left: positionX}">
    <img src="/img/hospital.svg" alt="hospital"/>
    <div class="name-label">{{ name }}</div>
  </div>
</template>

<script>
export default {
  name: 'HospitalBase',
  components: {},
  props: {
    name: String,
    x: Number,
    y: Number,
  },
  data() {
    return {
      positionX: 0,
      positionY: 0,
    };
  },
  created() {
    this.position(this.x, this.y);
  },
  methods: {
    position(x, y) {
      const xGridUnits = (x / 10000) + 8;
      const yGridUnits = (y / 10000) + 6;

      // each 1 GRID_CONST == 10k
      const GRID_CONST = 52;
      this.positionY = `${(GRID_CONST * yGridUnits) - 25}px`;
      this.positionX = `${(GRID_CONST * xGridUnits) - 25}px`;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.hospital-base {
  height: 52px;
  width: 52px;
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  img {
    opacity: 80%;
    height: 40px;
    width: 40px;
  }

  .name-label {
    font-size: 12px;
    margin-top: 2px;
    padding: 2px 4px;
    line-height: 12px;
    background-color: rgb(231, 231, 231);
    border: 1px solid rgb(121, 121, 121);
    border-radius: 5px;
  }
}
</style>
