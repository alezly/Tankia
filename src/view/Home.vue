<template>
  <div class="container">
    <div class="Cylinder">
      <div class="medidas_container">
        <button
          :style="medida == 'liters' ? { 'background-color': '#00adff69', 'color': 'white', 'border-color': 'white' } : {}"
          @click="()=>{medida = 'liters'; getintervals()}">L</button>
        <button
          :style="medida == 'cm' ? { 'background-color': '#00adff69', 'color': 'white', 'border-color': 'white' } : {}"
          @click="()=>{medida = 'cm'; getintervals()}">cm</button>
        <button
          :style="medida == 'percent' ? { 'background-color': '#00adff69', 'color': 'white', 'border-color': 'white' } : {}"
          @click="()=>{medida = 'percent'; getintervals()}">%</button>
      </div>
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
      <MainCard
        :title="medida == 'liters' ? 'Volumen de agua' : medida == 'cm' ? 'Altura del agua' : 'Porcentaje de agua'"
        :value="`${volumen_agua} ${medida == 'liters' ? 'Litros' : medida == 'cm' ? 'cm' : '%'}`" />
      <MainCard title="Tiempo de llenado" :value="`${tiempoEstimado} minutos`" />
    </div>
    <div class="Data2">
      <MainCard title="Capacidad máxima general"
        :value="`${volumen_tanque} ${medida == 'liters' ? 'Litros' : medida == 'cm' ? 'cm' : '%'}`" />
      <MainCard title="Tasa de flujo" :value="`${litroxminuto} litros por minuto`" />
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
  data: function () {
    return {
      rulerValues: [],
      volumen: 0,
      distancia: 0,
      medida: 'liters',
      altura: 142,
      diametro: 95
    }
  },

  components: {
    Cylinder,
    MainCard,
    MainGraficas,
  },
  methods: {
    getintervals() {
        const values = [];
        let startValue = 0;
        let endValue = this.medida == 'liters' ? this.volumen_tanque : this.medida == 'cm' ? this.altura : 100;

        // Genera 6 valores intermedios
        for (let i = 0; i < 6; i++) {
          values.push(startValue.toFixed(2));
          startValue += (endValue - startValue) / 5; // Ajusta este cálculo según tus necesidades
        }

        values.push(endValue)

        this.rulerValues = values.reverse()
    }
  },
  computed:{
    volumen_tanque(){
      if(this.medida == "cm"){
        return this.altura
      }else if(this.medida == "liters"){
        return (Math.PI*(Math.pow((this.diametro/2),2))*this.altura/1000).toFixed(0)
      }else{
        return 100
      }
    },
    volumen_agua(){
      if(this.medida == "cm"){
        return this.distancia
      }else if(this.medida == "liters"){
        return (Math.PI*(Math.pow((this.diametro/2),2))*this.distancia/1000).toFixed(0)
      }else{
        return this.distancia*100/this.altura
      } 
    },
  },
  created() {
    this.getintervals()
  },
  mounted() {
    setInterval(() => {
      axios.get(`/api/getDistance`).then((response) => {
        this.distancia = response.data.distancia
        this.tiempoEstimado = response.data.tiempo.toFixed(0)
        this.litroxminuto = response.data.litroxminuto.toFixed(0)

        let percentageDistance = this.distancia *100/this.altura
        document.documentElement.style.setProperty('--nivel-tanque', `${percentageDistance}%`);
      })
    }, 1000);
  }
};
</script>
<style>
:root {
  --nivel-tanque: 50%;
}

.medidas_container {
  position: absolute;
  top: 5%;
  right: 20%;
}

.medidas_container button {
  background: transparent;
  border: 1px solid #7e7e7e;
  color: #7e7e7e;
  padding: 0.2rem 1rem;
  border-radius: 1rem;
  margin-left: 0.2rem;
  cursor: pointer;
}

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

.ruler_values {
  height: 73.5%;
  width: 2rem;
  position: absolute;
  top: 13.5%;
  left: 12%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.ruler_values p {
  margin: 0;
}

#rule {
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
