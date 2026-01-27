import time
import numpy as np
import cProfile
import pstats
from io import StringIO

# --- Configuración del experimento ---
N = 10_000_000  # 5–20 millones según enunciado
DTYPE = np.float64
RERUNS = 3

def generar_datos(n=N, dtype=DTYPE):
    """Genera un array grande de números aleatorios."""
    return np.random.randn(n).astype(dtype)

# --- Operación a medir: sum((x - mean)**2) ---
def version_bucle_python(arr: np.ndarray) -> float:
    mean_val = float(np.mean(arr))  # calcular la media fuera del bucle
    total = 0.0
    for x in arr:
        dx = x - mean_val
        total += dx * dx
    return total

def version_numpy_vectorizado(arr: np.ndarray) -> float:
    mean_val = np.mean(arr)
    return np.sum((arr - mean_val) ** 2)

def medir_tiempos(func, arr, nombre: str):
    """Ejecuta 3 veces y devuelve lista de tiempos y promedio."""
    tiempos = []
    _ = func(arr)  # calentamiento
    for i in range(RERUNS):
        t0 = time.perf_counter()
        res = func(arr)
        t1 = time.perf_counter()
        tiempos.append(t1 - t0)
        print(f"{nombre} - Ejecución {i+1}: {t1 - t0:.4f}s")
    promedio = float(np.mean(tiempos))
    print(f"{nombre} - Promedio: {promedio:.4f}s\n")
    return tiempos, promedio, res

def perfilado_bucle(arr, n_mostrar=10):
    """Perfilado opcional con cProfile sobre un subconjunto."""
    print("== Perfilado (cProfile) bucle Python sobre 100.000 elementos ==")
    subset = arr[:100_000]
    pr = cProfile.Profile()
    pr.enable()
    version_bucle_python(subset)
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("tottime")
    ps.print_stats(n_mostrar)
    print(s.getvalue())

def main():
    print("=== Benchmark: bucle Python vs NumPy vectorizado ===")
    arr = generar_datos()
    print(f"Datos: {len(arr):,} elementos, dtype={arr.dtype}\n")

    tiempos_bucle, prom_bucle, res_bucle = medir_tiempos(version_bucle_python, arr, "Bucle Python")
    tiempos_numpy, prom_numpy, res_numpy = medir_tiempos(version_numpy_vectorizado, arr, "NumPy")

    assert np.isclose(res_bucle, res_numpy, rtol=1e-05, atol=1e-08), "Los resultados no coinciden"

    ratio = prom_bucle / prom_numpy
    print("=== Resumen ===")
    print(f"Bucle Python (promedio): {prom_bucle:.4f}s")
    print(f"NumPy (promedio):        {prom_numpy:.4f}s")
    print(f"Mejora: NumPy es {ratio:.1f}× más rápido")

    # Perfilado opcional
    perfilado_bucle(arr)

if __name__ == "__main__":
    main()
