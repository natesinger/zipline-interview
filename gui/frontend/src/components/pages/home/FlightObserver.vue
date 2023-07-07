<template>
  <div class="observer-pane">
    <div class="y-labels">
      <div v-for="i in range(-7,8)" :key="i" class="label">{{ i*10 }}k</div>
    </div>
    <div class="grid">
      <div class="grid-border">
        <!-- need to accomedate (-80 to +80) and (-60 to + 40) so 16x to 12y-->
        <div v-for="i in 16" :key="i" class="grid-row">
          <div v-for="q in 12" :key="q" class="grid-box"></div>
        </div>
      </div>
      <div class="x-labels">
        <div v-for="i in range(-6, 5)" :key="i"
        class="label">{{ i*10 }}k</div>
      </div>
      <HospitalBase v-for="hospital in hospitals" :key="hospital.name"
      :name="hospital.name" :x="hospital.x" :y="hospital.y"></HospitalBase>
      <ZipVehicle v-for="flight in flights"
        :key="flight"
        :x="flight.x"
        :y="flight.y"
        :rotation="flight.rotation"></ZipVehicle>
      <div class="home">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M543.8 287.6c17 0 32-14 32-32.1c1-9-3-17-11-24L512 185V64c0-17.7-14.3-32-32-32H448c-17.7 0-32 14.3-32 32v36.7L309.5 7c-6-5-14-7-21-7s-15 1-22 8L10 231.5c-7 7-10 15-10 24c0 18 14 32.1 32 32.1h32v69.7c-.1 .9-.1 1.8-.1 2.8V472c0 22.1 17.9 40 40 40h16c1.2 0 2.4-.1 3.6-.2c1.5 .1 3 .2 4.5 .2H160h24c22.1 0 40-17.9 40-40V448 384c0-17.7 14.3-32 32-32h64c17.7 0 32 14.3 32 32v64 24c0 22.1 17.9 40 40 40h24 32.5c1.4 0 2.8 0 4.2-.1c1.1 .1 2.2 .1 3.3 .1h16c22.1 0 40-17.9 40-40V455.8c.3-2.6 .5-5.3 .5-8.1l-.7-160.2h32z"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import HospitalBase from '@/components/pages/home/HospitalBase.vue';
import ZipVehicle from '@/components/pages/home/ZipVehicle.vue';

export default {
  name: 'FlightObserver',
  components: {
    HospitalBase,
    ZipVehicle,
  },
  props: {
    flights: Array,
  },
  data() {
    return {
      hospitals: [
        { name: 'Bigogwe', y: 50316, x: -39610 },
        { name: 'Butaro', y: 74007, x: 6631 },
        { name: 'Byumba', y: 54174, x: 30570 },
        { name: 'Gakoma', y: -44557, x: 15403 },
        { name: 'Gikonko', y: -44743, x: 8420 },
        { name: 'Gitwe', y: -18412, x: -10076 },
        { name: 'Kabaya', y: 36907, x: -27111 },
        { name: 'Kabgayi', y: -2684, x: -3192 },
        { name: 'Kaduha', y: -28009, x: -28261 },
        { name: 'Kibilizi', y: -62872, x: 304 },
        { name: 'Kigeme', y: -44124, x: -28249 },
        { name: 'Kinihira', y: 45540, x: 19857 },
        { name: 'Kirinda', y: -11765, x: -22484 },
        { name: 'Mugonero', y: -11198, x: -54232 },
        { name: 'Muhororo', y: 15998, x: -17276 },
        { name: 'Murunda', y: 19145, x: -45205 },
        { name: 'Nemba', y: 48732, x: 646 },
        { name: 'Nyanza', y: -30251, x: -3422 },
        { name: 'Ruhango', y: -12721, x: 13960 },
        { name: 'Ruli', y: 27664, x: 7710 },
        { name: 'Shyira', y: 41871, x: -16456 },
      ],
    };
  },
  methods: {
    range(start, end) {
      return Array(end - start + 1).fill().map((_, idx) => start + idx);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.observer-pane {
  background-color: $color-light-5;
  padding: 20px 20px 0px 20px;
  border-radius: 10px;

  display: flex;
  flex-direction: row;

  .grid {
    position: relative;
    .grid-border {
      border: 1px solid black;
      .grid-row {
        display: flex;
        flex-direction: row;

        .grid-box {
          width: 40px;
          height: 40px;
          border: 1px solid black;
        }
      }
    }
  }

  .y-labels {
    position: relative;
    left: 0;
    width: 40px;
    height: 100%;

    display: flex;
    flex-direction: column-reverse;
    justify-content: start;
    margin-left: -10px;

    .label {
      height: 42px;
      width: 42px;
      line-height: 0;
      text-align: center;
    }
  }

  .x-labels {
    position: relative;
    bottom: 0;
    width: 100%;

    display: flex;
    flex-direction: row;
    justify-content: start;
    height: 40px;

    .label {
      width: 42px;
      line-height: 42px;
      rotate: 45deg;
    }
  }
}

.home {
  position: absolute;
  height: 30px;
  width: 30px;

  top: calc(42px * 7.7);
  left: calc(42px * 5.67);

  z-index: 1;
}
</style>
