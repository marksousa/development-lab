<template>
  <div class="container">
    <h1>Componente Usuário <span>PAI</span></h1>
    <p>Esse é um componente muito legal!</p>
    <button @click="alterarNome">Alterar Nome</button>
    <hr />
    <div class="componentes">
      <!-- <app-usuario-info nomeUsuario="Mark" /> se nome é fixo -->
      <app-usuario-info :nomeUsuario="nome" />
      <!-- se nome é variavel -->
      <app-usuario-editar />
    </div>
  </div>
</template>

<script>
import AppUsuarioInfo from './UsuarioInfo'
import AppUsuarioEditar from './UsuarioEditar'

export default {
  components: { AppUsuarioInfo, AppUsuarioEditar },
  data() {
    return {
      nome: 'Pedro'
    }
  },
  methods: {
    alterarNome() {
      if (this.nome == 'Pedro') {
        this.nome = 'Ana'
      } else {
        this.nome = 'Pedro'
      }
    }
  }
}
</script>

<style scoped>
.container {
  background-color: #27363b;
  color: #fff;
  padding: 10px;
}

.container hr {
  margin: 20px 10px;
}

.componentes {
  display: flex;
}

.componentes > * {
  margin: 10px;
}
</style>
