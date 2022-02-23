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
    name: "BattleArena",
    props: {
      msg: String,
    },
    computed: {
      hasResult() {
        return this.playerLife == 0 || this.monsterLife == 0;
      },
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }

  /* Geral */

  html {
    font-family: "Montserrat", sans-serif;
  }

  #app {
    display: flex;
    flex-direction: column;
  }

  .panel {
    margin: 10px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  }

  /* Área dos Pontos */
  .scores {
    display: flex;
  }

  .score {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .score h1 {
    font-weight: 300;
    font-size: 1.6rem;
  }

  .life-bar {
    width: 80%;
    height: 20px;
    border: 1px solid #aaa;
  }

  .life-bar .life {
    display: flex;
    justify-content: center;
    height: 100%;
    background-color: green;
  }

  .life-bar .life.danger {
    background-color: red;
  }

  /* Área do Resultado */

  .result {
    display: flex;
    justify-content: center;
    font-size: 1.3rem;
    font-weight: 600;
  }

  .result .win {
    color: green;
  }

  .result .lose {
    color: red;
  }

  /* Área dos Botões (Controle do Jogo) */

  .buttons {
    display: flex;
    justify-content: center;
  }

  .btn {
    padding: 5px 10px;
    margin: 0px 10px;
    border-radius: 5px;
    text-transform: uppercase;
    font-size: 1.1rem;
  }

  .new-game {
    background-color: #4253af;
    color: #fff;
  }

  .attack {
    background-color: #e51c23;
    color: #fff;
  }

  .especial-attack {
    background-color: #ff9800;
    color: #000;
  }

  .heal {
    background-color: #259b24;
    color: #fff;
  }

  .give-up {
    background-color: #bbb;
    color: #000;
  }

  /* Área dos Logs */

  .logs ul {
    display: flex;
    flex-direction: column;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .logs ul li {
    display: flex;
    justify-content: center;
    margin: 4px 0px;
    padding: 3px 0px;
    font-weight: 600;
    font-size: 1.1rem;
    text-transform: uppercase;
    border-radius: 3px;
  }

  .player {
    background-color: #4253afaa;
    color: #fff;
  }

  .monster {
    background-color: #e51c23aa;
    color: #fff;
  }

  .game-title {
    font-weight: 800;
    font-family: "MedievalSharp", cursive;
    font-size: 2.5rem;
    margin: auto;
  }

  .game-brand {
    font-weight: 400;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
</style>
