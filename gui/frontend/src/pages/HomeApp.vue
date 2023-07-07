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
      <PlaybackController @updateData="updateData"></PlaybackController>
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
    console.log('connecting to websocket server...');
    // eslint-disable-next-line no-undef
    this.connection = io(this.deriveWsURL());

    this.connection.on('connect', () => {
      this.connection.emit('message', { data: 'connected!' });
      console.log('connected to websocket server...');
    });

    this.connection.on('disconnect', () => {
      console.log('disconnected from the websocket server...');
    });

    this.connection.on('message_event', (message) => this.receiveMessage(message));
  },
  data() {
    return {
      flights: null,
      openOrders: null,
      connection: null,
    };
  },
  methods: {
    deriveWsURL() {
      if (window.location.protocol === 'https:') {
        return `wss://${window.location.host}/`;
      }
      return `ws://${window.location.host}/`;
    },
    updateData(timeInSec) {
      this.sendMessage(timeInSec);
    },
    // eslint-disable-next-line object-shorthand
    sendMessage: function (message) {
      this.connection.emit('message_event', { data: message });
      console.log('sent', message);
    },
    // eslint-disable-next-line object-shorthand
    receiveMessage: function (message) {
      const data = JSON.parse(message);
      console.log('got', data);

      this.flights = data.flights;
      this.openOrders = data.openOrders;
    },
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
