<template>
  <PreauthBackground>
    <div class="not-found"><div class="text"><div class="number">404</div>Not Found</div></div>
  </PreauthBackground>
</template>

<script>
import PreauthBackground from '@/components/base/PreauthBackground.vue';

export default {
  components: {
    PreauthBackground,
  },
  created() {
    document.title = 'Zipline Code Challenge | 404';
  },
};
</script>

<style scoped lang="scss">
@import "@/scss/core.scss";
@import "@/scss/color.scss";

.not-found {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  .text {
    color: $color-red-3;
    font-size: 40px;
    font-weight: 700;
    text-align: center;

    .number {
      font-size: 120px;
      line-height: 100px;
    }
  }
}
</style>
