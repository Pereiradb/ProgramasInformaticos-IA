# Benchmark: Bucle Python vs NumPy vectorizado

**Fecha**: 21/01/2026 
**Hardware**: CPU: Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz (3.41 GHz) ; RAM: 16GB 2400MHz
**Tamaño de datos**: 10.000.000 `float64`  
**Operación**: `sum((x - mean)**2)`  
**Ejecuciones por versión**: 3 (promedio)

## Resultados de tiempos

### Bucle Python
- Ejecución 1: 1.7695 s
- Ejecución 2: 1.7187 s
- Ejecución 3: 1.7237 s 
**Promedio**: **1.7373 s**

### NumPy vectorizado
- Ejecución 1: 0.0651 s  
- Ejecución 2: 0.0792 s  
- Ejecución 3: 0.0746 s  
**Promedio**: **0.0730 s**

**Ratio de mejora**: NumPy es **23.8×** más rápido que el bucle Python.


== Perfilado (cProfile) bucle Python sobre 100.000 elementos ==
         13 function calls in 0.018 seconds

   Ordered by: internal time
   List reduced from 12 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.018    0.018    0.018    0.018 benchmark.py:17(version_bucle_python)
        1    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.000    0.000    0.000 numpy/_core/_methods.py:118(_mean)


El perfilado muestra que casi todo el tiempo se consume en la función `version_bucle_python`,
confirmando que el cuello de botella está en el bucle de Python y no en NumPy. Las demás funciones
(consumo de media, reduce, etc.) tienen un coste despreciable en comparación.
``
