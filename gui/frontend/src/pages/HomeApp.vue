<template>
  <PreauthBackground>
    <div class="content-pane">
      <div class="title">Zipline Flight Visualizer</div>
      <div class="display">
        <FlightObserver :flights="flights"></FlightObserver>
        <div class="orders-and-flights">
          <FlightDisplay :flights="flights"></FlightDisplay>
          <OrderDisplay :openOrders="openOrders"></OrderDisplay>
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
  data() {
    return {
      /* eslint-disable */
      flights: [
        { id: '38206', status: 'deployed', destination: 'Kibilizi', x: 38907, y: -31610 },
        { id: '99519', status: 'deployed', destination: 'Gitwe', x: 57316, y: -16810 },
        { id: '25483', status: 'standby', destination: 'N/A', x: 0, y: 0 },
        { id: '94273', status: 'deployed', destination: 'Muhororo', x: 27555, y: 11922 },
        { id: '07213', status: 'deployed', destination: 'Murunda', x: 11111, y: -2240 },
        { id: '05521', status: 'standby', destination: 'N/A', x: 0, y: 0 },
        { id: '56821', status: 'deployed', destination: 'Ruhango', x: 22316, y: -19610 },
        { id: '77250', status: 'deployed', destination: 'Shyira', x: 18316, y: -29610 },
        { id: '96216', status: 'standby', destination: 'N/A', x: 0, y: 0 },
        { id: '21708', status: 'standby', destination: 'N/A', x: 0, y: 0 },
        
      ],
      openOrders: [
        {id: 541593,destination: 'Kaduha', status: 'Emergency'},
        {id: 977270, destination: 'Butaro', status: 'Resupply'},
        {id: 242305, destination: 'Butaro', status: 'Resupply'},
        {id: 472570, destination: 'Nemba', status: 'Resupply'},
        {id: 980971, destination: 'Gakoma', status: 'Emergency'},
        {id: 195494, destination: 'Nyanza', status: 'Resupply'},
        {id: 342927, destination: 'Kabaya', status: 'Emergency'},
        {id: 208383, destination: 'Gitwe', status: 'Resupply'},
        {id: 211016, destination: 'Kinihira', status: 'Resupply'},
        {id: 592009, destination: 'Nyanza', status: 'Resupply'},
        {id: 566721, destination: 'Byumba', status: 'Resupply'},
        {id: 156866, destination: 'Kigeme', status: 'Emergency'},
        {id: 484164, destination: 'Kibilizi', status: 'Emergency'},
        {id: 787468, destination: 'Gakoma', status: 'Resupply'},
        {id: 663124, destination: 'Kaduha', status: 'Resupply'},
        {id: 934182, destination: 'Nemba', status: 'Emergency'},
        {id: 236886, destination: 'Butaro', status: 'Emergency'},
        {id: 270704, destination: 'Ruhango', status: 'Emergency'},
        {id: 822831, destination: 'Nyanza', status: 'Resupply'},
        {id: 322248, destination: 'Nemba', status: 'Emergency'},
        {id: 254645, destination: 'Gitwe', status: 'Emergency'},
        {id: 301460, destination: 'Ruhango', status: 'Resupply'},
        {id: 874800, destination: 'Kibilizi', status: 'Resupply'},
        {id: 116225, destination: 'Murunda', status: 'Resupply'},
        {id: 633397, destination: 'Muhororo', status: 'Emergency'},
        {id: 343038, destination: 'Nemba', status: 'Resupply'},
        {id: 508746, destination: 'Kabaya', status: 'Emergency'},
        {id: 131769, destination: 'Kaduha', status: 'Emergency'},
        {id: 699781, destination: 'Shyira', status: 'Emergency'},
        {id: 162189, destination: 'Kabgayi', status: 'Emergency'}
      ]
      /* eslint-enable */
    };
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
