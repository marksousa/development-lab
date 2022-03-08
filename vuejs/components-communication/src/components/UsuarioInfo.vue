<template>
  <div class="componente">
    <h2>As Informações de Usuário (Filho)</h2>
    <p>Vários detalhes...</p>
    <p>
      Nome do Usuário: <strong>{{ nomeUsuario }}</strong>
    </p>
    <p>
      Nome do Usuário Invertido:
      <strong>{{ inverterNome() }}</strong>
    </p>
  </div>
</template>

<script>
export default {
  //   props: ['nomeUsuario'], // direto, sem validacao

  // com validacao, mandar como objeto
  props: {
    // nomeUsuario: String // apenas um tipo permitido
    // nomeUsuario: [String, Array] // mais de um tipo (notação de array)
    nomeUsuario: {
      type: String,
      required: true,
      default: 'Anônimo'
    }
  },
  methods: {
    inverterNome() {
      return this.nomeUsuario.split('').reverse().join('')
    }
  }
}
</script>

<style scoped>
.componente {
  flex: 1;
  background-color: #ec485f;
  color: #fff;
}
</style>
