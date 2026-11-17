import { defineStore } from 'pinia'

/** Estado global de la UI. El modo es siempre PAPER: no existe modo real. */
export const useAgenteStore = defineStore('agente', {
  state: () => ({
    modo: 'PAPER' as const,
  }),
})
