# models/ — modelo y transformaciones aprobados

Copia aquí los archivos que salen de tus notebooks (carpeta `datos/` de Colab). **No se reentrenan en este proyecto.**

| Archivo | Origen |
|---|---|
| `checkpoints/*.keras` | Avance 2 (MLP y LSTM, entrenados en T4) |
| `escaladores_avance2_TR.joblib` | Avance 2 |
| `escalador_TR.joblib` | Avance 1 |
| `regresion_lineal.joblib` | Avance 1 |
| `configuracion_congelada_A2.json` | Avance 2 |
| `regla_seleccionada_A3.json` | Avance 3 (modelo generador de señal y umbral δ) |

**Contrato de variables:** 20 rendimientos diarios `r_t = P_t/P_{t-1} − 1`, del más antiguo al más reciente, solo con velas **cerradas**. Salida: `ŷ = P_{t+1}/P_t − 1`.

Cuando los copies, completa `MODEL_CARD.md` (plantilla abajo) y haz commit.

## MODEL_CARD.md (plantilla)
- Versión del modelo / fecha:
- Modelo elegido (lineal / MLP / LSTM) y neuronas:
- Semillas promediadas:
- Umbral δ y regla:
- Métricas de VA (MAE, RMSE) y rendimiento neto de VA:
- Hardware de entrenamiento (T4) y versiones de TensorFlow/Keras/scikit-learn:
- Limitaciones conocidas:

> Mientras no tengas los archivos reales, Claude Code puede usar un modelo **provisional** claramente marcado (`models/PROVISIONAL.md`); sus resultados no se publican como resultado final.
