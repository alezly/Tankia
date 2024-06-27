<template>
  <div class="card_container">
    <img
      v-if="title == 'Tiempo de llenado'"
      class="card_img"
      src="../assets/clock-svgrepo-com.png"
    />
    <img
      v-if="title == 'Tasa de flujo'"
      class="card_img"
      src="../assets/clock-lines-svgrepo-com.png"
    />
    <img
      v-if="title == 'Volumen de agua' || title == 'Capacidad máxima general' || title == 'Altura del agua' || title == 'Porcentaje de agua'"
      class="card_img"
      src="../assets/water-drop.png"
    />
    <h2 style="margin: 0.5rem">{{ title }}</h2>
    <p style="color: #6e6e6e">{{ value }}</p>
  </div>
</template>

<script>
export default {
  name: "MainCard",
  props: {
    title: String,
    value: String,
  },
};
</script>

<style>
.card_container {
  width: 100%;
  height: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f3f4f6;
  border-radius: 1rem;
  margin: 0.5rem;
}
.card_img {
  height: 3rem;
  margin-top: 1rem;
}
</style>
