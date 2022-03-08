<template>
  <div id="contador">
    <span>{{ contador }}</span>
    <button @click="adicionar">+</button>
    <button @click="subtrair">-</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contador: 0
    }
  },
  methods: {
    adicionar() {
      this.contador++
    },
    subtrair() {
      this.contador--
    }
  }
}
</script>

<style scoped>
/* scoped aplica apenas aos elementos do componente */
span {
  border-bottom: 1px solid #ccc;
  height: 30px;
  padding: 5px 25px;
}
button {
  height: 30px;
  width: 30px;
  border-radius: 15px;
  border-color: black;
  background-color: chartreuse;
  color: black;
  margin-left: 10px;
  outline: none;
}
</style>
