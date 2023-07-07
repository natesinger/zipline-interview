<template>
  <div class="control-pane">
    <div class="control-button" @click="playPause">
      <svg v-if="runStatus === 'running'" class="pause" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM224 192V320c0 17.7-14.3 32-32 32s-32-14.3-32-32V192c0-17.7 14.3-32 32-32s32 14.3 32 32zm128 0V320c0 17.7-14.3 32-32 32s-32-14.3-32-32V192c0-17.7 14.3-32 32-32s32 14.3 32 32z"/></svg>
      <svg v-else class="play" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zM188.3 147.1c-7.6 4.2-12.3 12.3-12.3 20.9V344c0 8.7 4.7 16.7 12.3 20.9s16.8 4.1 24.3-.5l144-88c7.1-4.4 11.5-12.1 11.5-20.5s-4.4-16.1-11.5-20.5l-144-88c-7.4-4.5-16.7-4.7-24.3-.5z"/></svg>
    </div>
    <div class="label-float">
      <input id="playback-speed" class="text-input" placeholder=" " value="15"
      :disabled="runStatus === 'running'">
      <label class="non-selectable">Playback (min/s)</label>
    </div>
    <div class="slidecontainer">
      <input type="range" min="0" max="86340" value="25200" class="slider" id="myRange">
      <label for="myRange"></label>
    </div>
    <div class="output" id="output"></div>
  </div>
</template>

<script>
export default {
  name: 'FlightControl',
  components: {},
  data() {
    return {
      runStatus: 'paused',
      runObject: null,
    };
  },
  mounted() {
    const slider = document.getElementById('myRange');
    const output = document.getElementById('output');
    output.innerText = this.formatTime(slider.value);

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = () => {
      output.innerHTML = this.formatTime(slider.value);
    };

    this.$emit('updateData', slider.value);
  },
  methods: {
    formatTime(seconds) {
      const hours = Math.floor(seconds / 3600);
      const minutes = Math.floor((seconds % 3600) / 60);

      const formattedHours = String(hours).padStart(2, '0');
      const formattedMinutes = String(minutes).padStart(2, '0');

      return `${formattedHours}:${formattedMinutes}`;
    },
    runSimulation() {
      const slider = document.getElementById('myRange');
      const currentSec = parseInt(document.getElementById('myRange').value, 10);
      const minsPerSec = parseInt(document.getElementById('playback-speed').value, 10);

      // check if at max time
      if (currentSec === 86340) {
        this.runStatus = 'paused';
        return;
      }

      // 60 seconds * x
      slider.value = currentSec + (minsPerSec * 60);
      document.getElementById('output').innerHTML = this.formatTime(slider.value);
      this.$emit('updateData', slider.value);
    },
    playPause() {
      if (this.runStatus === 'paused') {
        this.runObject = setInterval(this.runSimulation, 1000);
        this.runStatus = 'running';
      } else {
        clearInterval(this.runObject);
        this.runStatus = 'paused';
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/core.scss";
@import "@/scss/color.scss";
@import "@/scss/floating_input.scss";

.control-pane {
  width: 100%;
  background-color: $color-light-5;
  height: 75px;
  margin: 0;
  margin-top: 15px;
  border-radius: 10px;

  display: flex;
  flex-direction: row;
  align-content: center;
  align-items: center;

  .control-button {
    height: 50px;
    width: 50px;
    margin-left: 20px;
    display: flex;
    align-items: center;
    justify-content: center;

    filter: saturate(0.6);

    .play { fill: #2B9449;}
    .pause { fill: #E63946;}
  }

  .control-button:hover {
    cursor: pointer;
    filter: brightness(110%);
  }

  .label-float {
    width: 140px;
  }

  .slidecontainer {
    flex-grow: 1;
    height: 65px;
    display: flex;
    align-items: center;
  }

  .slider {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 10px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
    margin: 0 20px;
    border-radius: 5px;
  }

  .slider:hover {
    opacity: 1;
  }

  /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge)
  and -moz- (Firefox) to override default look) */
  .slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 50px;
    background: #333333;
    cursor: pointer;
  }

  .slider::-moz-range-thumb {
    width: 20px;
    height: 50px;
    background: #333333;
    cursor: pointer;
  }

  .output {
    font-size: 20px;
    line-height: 20px;

    color: #474747;
    margin-right: 20px;
  }
}
</style>
