<template>
  <div id="app">
    <h1>Compteur</h1>
    <p>Valeur actuelle : {{ counter }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      counter: 0,
    };
  },
  async mounted() {
    const response = await axios.get('/api/counter/'); // Proxyé vers Django
    this.counter = response.data.value;
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
</style>
