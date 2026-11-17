# PLAN_V1 — Agente de trading BTC/USDT (Paper), versión 1

**Meta de v1:** un agente que corre el ciclo completo de 7 pasos sobre velas diarias cerradas de BTC/USDT, en Paper, con UI, riesgo determinista, persistencia y evidencia de los 9 escenarios de error, publicado en un repo público con README y tabla de versiones.

**Fuera de alcance en v1:** entrenar DQN/DDQN, múltiples activos, órdenes reales (nunca), despliegue en la nube.

## Definición de terminado (DoD) de v1
- [ ] ≥ 20 ciclos válidos de decisión demostrados (replay etiquetado si hace falta)
- [ ] 9 escenarios de error con prueba automatizada y evidencia en `docs/evidencia/`
- [ ] Ollama realmente local (consulta demostrada sin inferencia en la nube)
- [ ] API protegida: clave ausente/incorrecta rechazada; secretos solo en servidor
- [ ] Prueba que demuestra que **no existe** ruta de órdenes reales
- [ ] Reinicio del backend recupera estado sin duplicar operaciones
- [ ] Comparación sin LLM / con LLM / comprar y mantener (mismo periodo y costos)
- [ ] `make test` y `make lint` en verde; CI en GitHub Actions
- [ ] README con tabla de versiones generada por `scripts/versions.py` y pendientes honestos
- [ ] Repo público sin secretos (auditado)

## Fases (una a una; commit y verificación al cerrar cada una)

| # | Fase | Entregables | Verificación |
|---|---|---|---|
| 0 | Preparación | Leer `CLAUDE.md`; plan corto aprobado por el autor; `git init` (rama `main`) | Plan confirmado |
| 1 | Esqueleto + CI | `backend/` (FastAPI, pytest, ruff, mypy), `frontend/` (Vue3+TS+Vite+Pinia, vitest, eslint, vue-tsc), `Makefile` real, GitHub Actions | `make test` y `make lint` corren |
| 2 | Datos MEXC | Cliente `klines` (max 500 por petición, paginar con `endTime`), solo velas cerradas, validaciones, backoff, 429 | Pruebas con API simulada; mensaje útil ante fallo |
| 3 | Modelo y variables | Carga de modelo/escaladores desde `models/`, variables con el mismo contrato, `MODEL_CARD.md` (o `PROVISIONAL.md`) | Pronóstico reproducible sobre un caso conocido |
| 4 | Ollama + gateway + JSON | Cliente local, API key en el gateway, JSON validado con Pydantic, reintentos, "mantener" seguro | Pruebas: Ollama detenido, JSON inválido, clave incorrecta |
| 5 | Riesgo + Paper + SQLite | `risk.yaml`, motor determinista, simulador (saldo, costos, precisión, apertura t+1), persistencia | Pruebas: saldo insuficiente, límites, idempotencia |
| 6 | Ciclo + scheduler | Los 7 pasos, ejecución diaria + manual, replay etiquetado | ≥ 20 ciclos; evento duplicado no duplica |
| 7 | UI Vue | Pantalla de acceso (clave en memoria), panel (activo, fecha del dato, pronóstico, indicadores, acción, motivo, riesgo, posición, patrimonio), gráficas, tablas, Iniciar/Pausar/Detener con confirmación, etiqueta PAPER y replay/real | Capturas en `docs/capturas/` |
| 8 | Los 9 errores | `scripts/demo_errors.py` + pruebas: API sin respuesta/429 · dato atrasado · Ollama detenido · JSON inválido · clave incorrecta · saldo insuficiente · evento duplicado · reinicio · botón Detener | Evidencia en `docs/evidencia/` |
| 9 | Evaluación | Comparar (a) modelo sin LLM, (b) agente con LLM, (c) comprar y mantener: rendimiento neto, drawdown, Win Rate, operaciones, latencia, acciones rechazadas; ¿aporta el LLM? | `docs/resultados.md` + CSV |
| 10 | README y publicación | README completo, `make versions`, auditoría de secretos, repo **público** con `gh` | URL del repo, README renderizado |

## Riesgos y mitigación
- **Sin artefactos del modelo aún** → modelo provisional marcado; reemplazar antes de evaluar (Fase 9).
- **MEXC limita a 500 velas por petición** → paginar hacia atrás con `endTime`.
- **LLM alucina o es manipulado** → JSON estricto + lista blanca de acciones + riesgo determinista.
- **TensorFlow pesado en local** → si el modelo elegido es la regresión lineal, no cargar TF.
- **Colab/T4 no disponible para los notebooks** → no bloquea las Fases 1–2 y 4–8.

## Reglas de cambio
Cualquier cambio de alcance se anota aquí con fecha y motivo. Si se agrega una decisión de arquitectura, actualizar `CLAUDE.md` y `docs/ARQUITECTURA.md`.
