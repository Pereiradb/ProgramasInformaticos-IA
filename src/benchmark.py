import time
import numpy as np
import math
import cProfile
import pandas as pd  # Para la extensión opcional

def generar_datos(n=10_000_000, dtype=np.float64):
    """Genera un array de números aleatorios"""
    return np.random.randn(n).astype(dtype)

def version_bucle_python(arr):
    """Versión A: cálculo con bucle Python puro"""
    total = 0.0
    mean_val = np.mean(arr)  # Calculamos la media fuera del bucle para ser justos
    
    for x in arr:
        total += (x - mean_val) ** 2
    return total

def version_numpy_vectorizado(arr):
    """Versión B: cálculo vectorizado con NumPy"""
    mean_val = np.mean(arr)
    return np.sum((arr - mean_val) ** 2)

def medir_tiempo(func, arr, nombre="Función"):
    """Mide el tiempo de ejecución de una función"""
    tiempos = []
    
    # Calentamiento (opcional, para evitar sesgos)
    _ = func(arr)
    
    # Medir 3 ejecuciones
    for i in range(3):
        inicio = time.perf_counter()
        resultado = func(arr)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        print(f"{nombre} - Ejecución {i+1}: {fin-inicio:.4f} segundos")
    
    promedio = np.mean(tiempos)
    print(f"{nombre} - Tiempo promedio: {promedio:.4f} segundos\n")
    return promedio, resultado

def main():
    print("=== Benchmark: Cálculo de varianza (suma de cuadrados de diferencias) ===")
    print("Generando 10 millones de números...")
    
    # Datos para las pruebas principales
    datos = generar_datos(10_000_000)
    print(f"Datos generados: {len(datos):,} elementos, tipo: {datos.dtype}\n")
    
    # Medir versión bucle Python
    print("1. Versión con bucle Python:")
    tiempo_bucle, resultado_bucle = medir_tiempo(version_bucle_python, datos, "Bucle Python")
    
    # Medir versión NumPy
    print("2. Versión vectorizada NumPy:")
    tiempo_numpy, resultado_numpy = medir_tiempo(version_numpy_vectorizado, datos, "NumPy")
    
    # Calcular ratio de mejora
    ratio = tiempo_bucle / tiempo_numpy
    print(f"RESUMEN:")
    print(f"- Bucle Python: {tiempo_bucle:.4f} segundos")
    print(f"- NumPy vectorizado: {tiempo_numpy:.4f} segundos")
    print(f"- NumPy es {ratio:.1f} veces más rápido")
    print(f"- Resultados coinciden: {np.isclose(resultado_bucle, resultado_numpy)}\n")
    
    # Perfilado opcional con cProfile
    print("Perfilando versión bucle (primeros 10 resultados)...")
    cProfile.run('version_bucle_python(datos[:100000])', sort='time')
    
    # EXTENSIÓN 1: Comparar float32 vs float64
    print("\n=== EXTENSIÓN: float32 vs float64 ===")
    
    datos_f64 = generar_datos(5_000_000, np.float64)
    datos_f32 = generar_datos(5_000_000, np.float32)
    
    _, tiempo_f64 = medir_tiempo(version_numpy_vectorizado, datos_f64, "NumPy float64")
    _, tiempo_f32 = medir_tiempo(version_numpy_vectorizado, datos_f32, "NumPy float32")
    
    print(f"Float64: {tiempo_f64:.4f}s, Float32: {tiempo_f32:.4f}s")
    print(f"Float32 es {tiempo_f64/tiempo_f32:.1f}x más rápido (aproximadamente)")
    
    # EXTENSIÓN 2: Versión con pandas (opcional)
    print("\n=== EXTENSIÓN: Versión con Pandas ===")
    def version_pandas(arr):
        """Versión usando pandas Series"""
        series = pd.Series(arr)
        mean_val = series.mean()
        return ((series - mean_val) ** 2).sum()
    
    # Usar menos datos para pandas (puede ser más lento)
    datos_pandas = generar_datos(1_000_000)
    _, tiempo_pandas = medir_tiempo(version_pandas, datos_pandas, "Pandas")
    
    # Comparar con NumPy en los mismos datos
    _, tiempo_numpy_peq = medir_tiempo(version_numpy_vectorizado, datos_pandas, "NumPy (1M)")
    
    print(f"\nComparación en 1M elementos:")
    print(f"- Pandas: {tiempo_pandas:.4f}s")
    print(f"- NumPy: {tiempo_numpy_peq:.4f}s")
    print(f"- NumPy es {tiempo_pandas/tiempo_numpy_peq:.1f}x más rápido que Pandas")

if __name__ == "__main__":
    main()
