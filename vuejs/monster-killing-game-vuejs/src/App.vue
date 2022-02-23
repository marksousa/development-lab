<template>
  <div>
    <img class="logo" alt="Vue logo" src="./assets/monster.svg" />
    <BattleArena msg="Monster Killer Game App" />
  </div>
</template>

<script>
  import BattleArena from "./components/BattleArena.vue";

  export default {
    name: "App",
    components: {
      BattleArena,
    },
  };
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  .logo {
    max-width: 20%;
  }
</style>
