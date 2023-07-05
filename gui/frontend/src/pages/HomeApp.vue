<template>
  <PreauthBackground>
    <div class="content-pane">
      <div class="title">Zipline Flight Visualizer</div>
      <div class="display">
        <FlightObserver></FlightObserver>
        <div class="orders-and-flights">
          <FlightDisplay></FlightDisplay>
          <OrderDisplay></OrderDisplay>
        </div>
      </div>
      <PlaybackController></PlaybackController>
    </div>
  </PreauthBackground>
</template>

<script>
import PreauthBackground from '@/components/base/PreauthBackground.vue';
import FlightDisplay from '@/components/pages/home/FlightDisplay.vue';
import FlightObserver from '@/components/pages/home/FlightObserver.vue';
import OrderDisplay from '@/components/pages/home/OrderDisplay.vue';
import PlaybackController from '@/components/pages/home/PlaybackController.vue';

export default {
  components: {
    PreauthBackground,
    FlightDisplay,
    FlightObserver,
    OrderDisplay,
    PlaybackController,
  },
  created() {
    document.title = 'Hack a Bit | Dashboard';
  },
};
</script>

<style scoped lang="scss">
@import "@/scss/core.scss";

.content-pane {
  display: flex;
  flex-direction: column;
  margin-top: 15px;

  .title {
    font-size: 26px;
    text-align: center;
    font-weight: 650;
  }

  .display {
    display: flex;
    flex-direction: row;

    .orders-and-flights {
      flex-direction: row;
      margin-left: 15px;
      flex-direction: column;
      border-radius: 10px;
    }
  }
}
</style>
