# Benchmark: Bucle Python vs NumPy vectorizado

**Fecha**: 21/01/2026 
**Hardware**: CPU: Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz (3.41 GHz) ; RAM: 16GB 2400MHz
**Tamaño de datos**: 10.000.000 `float64`  
**Operación**: `sum((x - mean)**2)`  
**Ejecuciones por versión**: 3 (promedio)

## Resultados de tiempos

### Bucle Python
- Ejecución 1: … s  
- Ejecución 2: … s  
- Ejecución 3: … s  
**Promedio**: **… s**

### NumPy vectorizado
- Ejecución 1: … s  
- Ejecución 2: … s  
- Ejecución 3: … s  
**Promedio**: **… s**

**Ratio de mejora**: NumPy es **…×** más rápido que el bucle Python.

## Perfilado (opcional)
Salida abreviada de `cProfile` (top 10 por `tottime`):
