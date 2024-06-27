<template>
  <div class="container">
    <div class="Cylinder">
      <div class="ruler_values">
        <p v-for="(item) in rulerValues" :key="item">{{ item }}</p>
      </div>
      <ol id="rule">
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
      </ol>
      <Cylinder></Cylinder>
    </div>
    <div class="Navbar">
      <h2>Tankia App</h2>
    </div>
    <div class="Data">
      <MainCard title="Volumen de agua" :value="`${volumen} litros`" />
      <MainCard title="Tiempo de llenado" value="10 segundos" />
    </div>
    <div class="Data2">
      <MainCard title="Tiempo de vaciado" value="10 segundos" />
      <MainCard title="Tasa de flujo" value="10 segundos" />
    </div>
    <div class="Dashboar">
      <MainGraficas />
    </div>
  </div>
</template>

<script>
import Cylinder from "../components/Cylinder.vue";
import MainCard from "../components/Card.vue";
import MainGraficas from "../components/Graficas.vue";
import axios from "axios";

export default {
  name: "HomeView",
  data: function(){
    return {
      rulerValues: [],
      volumen: 0
    }
  },
  methods: {
    connectToSocket() {
      console.log("connectToSocket")
      this.socket = new WebSocket('ws://localhost:8000/ws');
      console.log("Daniel")
      this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        this.lastMessage = data.message;
        console.log(data.message)
      };

      this.socket.onerror = (error) => {
        console.error('WebSocket Error: ', error);
      };
    },
  },

  components: {
    Cylinder,
    MainCard,
    MainGraficas,
  },
  created(){
    this.connectToSocket();
    axios.get(`/getMax`,{
  withCredentials: true, // Incluye las credenciales en la solicitud
}).then((response) => {
      const values = [];
      let startValue = 0;
      let endValue = response.data.max;

      // Genera 6 valores intermedios
      for (let i = 0; i < 6; i++) {
        values.push(startValue.toFixed(2));
        startValue += (endValue - startValue) / 5; // Ajusta este cálculo según tus necesidades
      }

      values.push(response.data.max)

      this.rulerValues = values.reverse()
      this.volumen = (0.50 * 1.25 * response.data.max * 1000).toFixed()
    }).catch((error) => {
      console.error(error);
    });
  }
};
</script>
<style scoped>
.container {
  width: 100%;
  height: 100vh;
  font-family: "Figtree", sans-serif;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 0.3fr 1fr 1fr 1.7fr;
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "Navbar Navbar"
    "Cylinder Data"
    "Cylinder Data2"
    "Cylinder Dashboar";
}

.Cylinder {
  grid-area: Cylinder;
  width: 100%;
  height: 100%;
  position: relative;
}
.ruler_values{
  height: 73.5%;
  width: 2rem;
  position: absolute;
  top: 13.5%;
  left: 12%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.ruler_values p{
  margin: 0;
}
#rule{
  margin-top: 13%;
}
ol,
li {
  list-style-type: none;
}
ol {
  counter-reset: marker;
}
li {
  height: 0.65cm;
  border-top: 1px solid #000;
  box-sizing: border-box;
  width: 2.5em;
  counter-increment: marker;
  position: relative;
  border-left: 2px solid #000;
}
li:last-child {
  height: 0;
}
li:first-child::after,
li:nth-child(5n)::after {
  position: absolute;
  top: -0.5em;
  left: 100%;
  height: 1em;
  line-height: 1em;
  width: 2em;
  text-align: center;
}

.Navbar {
  grid-area: Navbar;
  text-align: center;
}

.Data {
  grid-area: Data;
  display: flex;
  gap: 1rem;
}

.Data2 {
  grid-area: Data2;
  display: flex;
  gap: 1rem;
}

.Dashboar {
  grid-area: Dashboar;
}
</style>
