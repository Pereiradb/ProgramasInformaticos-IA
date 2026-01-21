# Benchmark: Bucle Python vs NumPy vectorizado

## Configuración del experimento
- **Fecha**: 21/01/2026
- **Hardware**: CPU: Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz (3.41 GHz) ; RAM: 16GB 2400MHz
- **Tamaño de datos**: 10 millones de números float64
- **Operación**: `sum((x - mean)^2)` (cálculo de suma de cuadrados para varianza)

## Resultados de tiempos

| Versión | Ejecución 1 (s) | Ejecución 2 (s) | Ejecución 3 (s) | Promedio (s) |
|---------|-----------------|-----------------|-----------------|--------------|
| Bucle Python | | | | |
| NumPy vectorizado | | | | |

**Ratio de mejora**: NumPy es **X veces** más rápido que el bucle Python.

## Perfilado (cProfile)
