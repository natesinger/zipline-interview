<template>
  <div class="observer-pane">
    <div class="y-labels">
      <div v-for="i in range(-6,6)" :key="i" class="label">{{ i*10 }}k</div>
    </div>
    <div class="grid">
      <div class="grid-border">
        <!-- need to accomedate (-80 to +80) and (-60 to + 40) so 16x to 12y-->
        <div v-for="i in 12" :key="i" class="grid-row">
          <div v-for="q in 16" :key="q" class="grid-box"></div>
        </div>
      </div>
      <div class="x-labels">
        <div v-for="i in range(-8, 7)" :key="i"
        class="label">{{ i*10 }}k</div>
      </div>
      <HospitalBase v-for="hospital in hospitals" :key="hospital.name"
      :name="hospital.name" :x="hospital.x" :y="hospital.y"></HospitalBase>
    </div>
  </div>
</template>

<script>
import HospitalBase from '@/components/pages/home/HospitalBase.vue';

export default {
  name: 'FlightObserver',
  components: {
    HospitalBase,
  },
  data() {
    return {
      hospitals: [
        { name: 'Bigogwe', x: 50316, y: -39610 },
        { name: 'Butaro', x: 74007, y: 6631 },
        { name: 'Byumba', x: 54174, y: 30570 },
        { name: 'Gakoma', x: -44557, y: 15403 },
        { name: 'Gikonko', x: -44743, y: 8420 },
        { name: 'Gitwe', x: -18412, y: -10076 },
        { name: 'Kabaya', x: 36907, y: -27111 },
        { name: 'Kabgayi', x: -2684, y: -3192 },
        { name: 'Kaduha', x: -28009, y: -28261 },
        { name: 'Kibilizi', x: -62872, y: 304 },
        { name: 'Kigeme', x: -44124, y: -28249 },
        { name: 'Kinihira', x: 45540, y: 19857 },
        { name: 'Kirinda', x: -11765, y: -22484 },
        { name: 'Mugonero', x: -11198, y: -54232 },
        { name: 'Muhororo', x: 15998, y: -17276 },
        { name: 'Murunda', x: 19145, y: -45205 },
        { name: 'Nemba', x: 48732, y: 646 },
        { name: 'Nyanza', x: -30251, y: -3422 },
        { name: 'Ruhango', x: -12721, y: 13960 },
        { name: 'Ruli', x: 27664, y: 7710 },
        { name: 'Shyira', x: 41871, y: -16456 },
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
          width: 50px;
          height: 50px;
          border: 1px solid black;
        }
      }
    }
  }

  .y-labels {
    position: relative;
    left: 0;
    width: 50px;
    height: 100%;

    display: flex;
    flex-direction: column-reverse;
    margin-left: -10px;

    .label {
      height: 52px;
      width: 52px;
      line-height: 0;
      text-align: center;
    }
  }

  .x-labels {
    position: relative;
    bottom: 0;
    width: 100%;
    margin-bottom: -10px;

    display: flex;
    flex-direction: row;
    justify-content: start;
    height: 50px;

    .label {
      width: 52px;
      line-height: 52px;
      rotate: 45deg;
    }
  }
}
</style>
