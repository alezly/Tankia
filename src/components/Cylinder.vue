<template>
  <div class="cylinder">
    <div class="water">
      <div class="wave-01"></div>
      <div class="wave-02"></div>
      <div class="wave-03"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CylinderFill",
};
</script>

<style>
.cylinder {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60%;
  height: 70%;
  border-top: 2px solid transparent;
  border-radius: 15px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  box-shadow: 0 0 0 6px #fff, 0 20px 35px rgb(0 0 0 / 61%);
}
.water {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
  overflow: hidden;
}

.wave-01 {
  position: absolute;
  width: 300%;
  height: 300%;
  left: -100%;
  top: var(--nivel-tanque);
  background-color: #00adff2b;
  border-radius: 45%;
  animation: rotate 20s linear infinite;
}
.wave-02 {
  position: absolute;
  width: 300%;
  height: 300%;
  left: -100%;
  top: var(--nivel-tanque);
  background-color: #00adff5e;
  border-radius: 43%;
  animation: rotate 17s linear infinite;
}
.wave-03 {
  position: absolute;
  width: 300%;
  height: 300%;
  left: -100%;
  top: var(--nivel-tanque);
  background-color: #00adff69;
  border-radius: 40%;
  animation: rotate 15s linear infinite;
}
@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}
</style>
