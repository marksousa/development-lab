new Vue({
  el: "#app",
  data: {
    running: 0,
    playerLife: 100,
    monsterLife: 100,
  },
  computed: {
    hasResult: {
      return this.playerLife == 0 || this.monsterLife == 0;
    }
  },
  methods: {
    startGame() {
      this.running = true,
        this.monsterLife = 100,
        this.playerLife = 100
    }
  },
  watch: {},
});