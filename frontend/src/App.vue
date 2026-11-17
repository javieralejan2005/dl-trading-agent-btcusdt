<script setup lang="ts">
import { useAgenteStore } from '@/stores/agente'

const agente = useAgenteStore()
</script>

<template>
  <header class="encabezado">
    <h1>Agente BTC/USDT</h1>
    <span class="etiqueta-modo" data-test="modo">{{ agente.modo }}</span>
  </header>
  <main>
    <p>Simulación con dinero virtual. No se envían órdenes reales.</p>
  </main>
</template>

<style scoped>
.encabezado {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0 1rem;
}
.etiqueta-modo {
  background: #9a6700;
  color: #fff;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}
main {
  padding: 0 1rem;
}
</style>
