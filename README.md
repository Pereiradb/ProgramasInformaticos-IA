# ProgramasInformaticos-IA


A) Entrenar un modelo y desplegarlo como API para predicciones.

## Matriz 1 — Lenguaje para ENTRENAMIENTO del modelo


| Criterio                               | Peso | Python | R | Java | Node |
|----------------------------------------|------|--------|---|------|------|
| Ecosistema IA/ML                       | 5    | 5      | 4 | 2    | 1    |
| Productividad / prototipado            | 5    | 5      | 4 | 2    | 3    |
| Rendimiento / latencia                 | 3    | 3      | 2 | 4    | 1    |
| Concurrencia / I-O / servicios         | 2    | 2      | 1 | 5    | 5    |
| Integración Big Data                   | 4    | 4      | 3      | 5    | 3    |
| Despliegue y portabilidad              | 2    | 4      | 3      | 5    | 4    |
| Mantenibilidad / tipado / tooling      | 3    | 3      | 2 | 5    | 4    |
| Talento disponible                     | 4    | 5      | 3 | 4    | 4    |
| Coste de operación / infraestructura   | 3    | 4      | 3 | 3    | 4    |
| **TOTAL ponderado**      



## Matriz 2 — Despliegue de la API (criterios unificados)

| Criterio                               | Peso | Python | R | Java | Node |
|----------------------------------------|------|--------|---|------|------|
| Ecosistema IA/ML                       | 2    | 5      | 4 | 2    | 1    |
| Productividad / prototipado            | 2    | 5      | 4 | 2    | 3    |
| Rendimiento / latencia                 | 5    | 2      | 1 | 5    | 4    |
| Concurrencia / I-O / servicios         | 5    | 2      | 1 | 5    | 5    |
| Integración Big Data                   | 3    | 3      | 2 | 5    | 3    |
| Despliegue y portabilidad              | 4    | 4      | 3 | 5    | 5    |
| Mantenibilidad / tipado / tooling      | 3    | 3      | 2 | 5    | 4    |
| Talento disponible                     | 3    | 5      | 3 | 4    | 4    |
| Coste de operación / infraestructura   | 4    | 3      | 2 | 4    | 5    |
| **TOTAL ponderado**                    |      | **66** | 42 | **109** | 102 |


## Conclusión


Para la fase de entrenamiento, el lenguaje más adecuado es **Python**, dado su ecosistema de librerías para Machine Learning (PyTorch, TensorFlow, scikit‑learn), su rapidez para prototipar y la gran disponibilidad de talento. Además, ofrece un coste razonable de infraestructura durante el desarrollo y el uso de contenedores ligeros.

Sin embargo, para el despliegue como API de predicciones, el lenguaje con mejor puntuación es **Java**, que destaca por su alto rendimiento, baja latencia, capacidad de concurrencia y portabilidad a nivel empresarial. Node.js también es eficiente, pero queda por detrás en cálculos intensivos.  

El principal riesgo técnico es emplear **dos lenguajes distintos** (Python para entrenar y Java para desplegar), lo que podría aumentar la complejidad de mantenimiento y operaciones. La mitigación recomendada consiste en exportar los modelos de Python a un formato estándar como ONNX, permitiendo servirlos eficientemente desde Java con ONNX Runtime. Así se combinan las fortalezas de ambos mundos: productividad en el entrenamiento y rendimiento en producción.
