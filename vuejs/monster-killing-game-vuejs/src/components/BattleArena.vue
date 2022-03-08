<template>
  <div class="arena">
    <h1>{{ msg }}</h1>
    <p>
      Think in your strategy and click the correspondent button.<br />
      Defeat the monster.
    </p>
    <div class="panel scores">
      <div class="score">
        <h1>Player</h1>
        <img
          src="https://img.icons8.com/color/96/000000/iron-age-warrior.png"
        />
        <div class="life-bar">
          <div
            class="life"
            :class="{ danger: playerLife < 20 }"
            :style="{ width: playerLife + '%' }"
          ></div>
        </div>
        <div>{{ playerLife }}%</div>
      </div>
      <div class="score">
        <h1>Monster</h1>
        <img src="https://img.icons8.com/color/96/000000/monster-face.png" />
        <div class="life-bar">
          <div
            class="life"
            :class="{ danger: monsterLife < 20 }"
            :style="{ width: monsterLife + '%' }"
          ></div>
        </div>
        <div>{{ monsterLife }}%</div>
      </div>
    </div>

    <div v-if="hasResult" class="panel result">
      <div class="win" v-if="monsterLife == 0">You Win!!! :)</div>
      <div class="lose" v-else>You Lose! :(</div>
    </div>
    <div class="panel buttons">
      <template>
        <button class="btn attack">Attack</button>
        <button class="btn especial-attack">Especial Attack</button>
        <button class="btn heal">Heal</button>
        <button class="btn give-up">Give Up</button>
      </template>
      <button class="btn new-game">New Game</button>
    </div>
    <div class="panel logs">
      <ul>
        <li></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BattleArena',
  data() {
    return {
      playerLife: 0,
      monsterLife: 10
    }
  },
  props: {
    msg: String
  },
  computed: {
    hasResult() {
      return this.playerLife == 0 || this.monsterLife == 0
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
