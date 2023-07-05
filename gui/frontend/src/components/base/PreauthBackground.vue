<template>
  <div class="background">
    <slot class="page-content"></slot>
    <PreauthFooter></PreauthFooter>
  </div>
</template>

<script>
import PreauthFooter from '@/components/base/PreauthFooter.vue';

export default {
  name: 'PreauthBackground',
  components: {
    PreauthFooter,
  },
};
</script>

<style lang="scss">
@import "@/scss/core.scss";
@import "@/scss/color.scss";

body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: $color-light-3;
}

.background {
  height: 100vh;

  display: flex;
  flex-direction: column;
  align-items: center;

  .center-content {
    width: min(1000px, 98%);
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-grow: 1;
  }

  .page-content {
    display: flex;
    flex-grow: 1;
  }
}
</style>
