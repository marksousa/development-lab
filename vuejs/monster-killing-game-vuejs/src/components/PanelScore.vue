<template>
  <div class="panel scores">
    <div class="score">
      <h1>Player</h1>
      <img src="https://img.icons8.com/color/96/000000/iron-age-warrior.png" />
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
</template>

<script>
export default {
  name: 'Panel Score',
  data() {
    return {
        user:
    }
  },
  methods() {}
}
</script>

<style></style>
