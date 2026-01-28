# Comprension De La Eficiencia De Numpy

## Bloque A — Observación inicial (qué pasa)
**1. Si implementas el mismo cálculo con un for en Python y con una operación vectorizada en NumPy, ¿qué esperas que ocurra con el tiempo de ejecución cuando el tamaño del array pasa de 1.000 a 10.000.000 elementos?**  
Al pasar de 1.000 a 10.000.000 elementos, el bucle Python crece casi linealmente y se vuelve muy lento; NumPy sigue siendo rápido porque opera en C.   

**2. ¿En qué punto (tamaño aproximado) crees que la diferencia empieza a ser clara? ¿Por qué?**  
A partir de ~50.000–100.000 elementos ya se nota una diferencia clara; NumPy escala mucho mejor.

**3. ¿Qué parte del programa crees que consume más tiempo: el cálculo matemático o el “mecanismo” de recorrer y operar elemento a elemento?**  
Lo que más tiempo consume es recorrer elemento a elemento en Python, no el cálculo matemático.

## Bloque B — Representación de datos (qué estás procesando realmente)
**4. ¿Cómo almacena Python una lista de números? ¿Es una lista de valores o una lista de referencias a objetos?**  
Una lista de Python almacena referencias a objetos, no valores contiguos.

**5. ¿Qué implica para la CPU acceder a datos dispersos en memoria (objetos separados) frente a datos contiguos?**  
Acceder a datos dispersos hace que la CPU falle más en caché → más lento.

**6. ¿Qué significa que un array NumPy sea “homogéneo” (mismo dtype) y por qué podría ayudar al rendimiento?**  
NumPy es homogéneo (un único dtype): memoria contigua, sin objetos → más eficiente.

**7. ¿Qué coste adicional tiene Python al operar con tipos dinámicos en cada iteración?**  
Python debe resolver tipos dinámicamente en cada iteración → mucho overhead.

## Bloque C — Overhead del intérprete (por qué el bucle Python pesa tanto)
**8. En un bucle Python, por cada iteración, ¿qué operaciones “extra” ocurren además de sumar o multiplicar? (pista: resolución de tipos, llamadas, objetos, etc.)**  
En cada iteración se hacen: lookup de variables, comprobaciones de tipo, creación de objetos temporales, gestión del GC, llamadas a funciones…

**9. ¿Por qué una llamada a math.sin() dentro de un bucle puede ser especialmente cara repetida millones de veces?**  
math.sin() es caro porque cada llamada cruza el intérprete y crea objetos → millones de llamadas = muy lento.

**10. ¿Qué crees que significa realmente “overhead del intérprete” en términos de tiempo por elemento?**  
“Overhead del intérprete” = el tiempo extra por cada elemento solo para ejecutar la infraestructura de Python, no la operación en sí.

## Bloque D — Dónde se ejecuta el bucle (Python vs C)
**11. Cuando escribes np.sin(x), ¿quién recorre el array: tu bucle Python o un bucle interno compilado?**  
Con np.sin(x) el bucle lo ejecuta C/Fortran, no Python.

**12. ¿Por qué un bucle en C/Fortran puede ser mucho más eficiente que el mismo bucle escrito en Python?**  
Un bucle en C es mucho más eficiente: compilado, sin objetos, sin comprobaciones, sin intérprete.

**13. ¿Qué cambia en el número de “entradas” al intérprete entre estas dos versiones?  
    - Bucle Python con for  
    - Vectorización NumPy**  
Con bucle Python hay una entrada al intérprete por elemento; con NumPy hay una sola llamada para procesar todo el array.

## Bloque E — Cachés, contigüidad y SIMD (por qué la CPU “vuela” con NumPy)
**14. ¿Qué es la caché de CPU y por qué importa en cálculos sobre arrays grandes?**  
La caché de CPU guarda datos cercanos para no ir a RAM; si los datos son contiguos, las operaciones vuelan.

**15. ¿Qué es el “prefetching” y por qué funciona mejor con memoria contigua?**  
El “prefetching” anticipa qué memoria leer — funciona mejor si los datos son contiguos.

**16. ¿Qué tipo de operaciones crees que se benefician más de SIMD (vectorización a nivel CPU): sumas/multiplicaciones, o lógica con muchos if? ¿Por qué?**  
SIMD acelera operaciones numéricas repetitivas (sumas, multiplicaciones), no lógica con muchos if.

**17. ¿Qué crees que pasa si tus datos no están contiguos (slicing raro, arrays no contiguos)? ¿Se mantiene la ventaja?**  
Si los datos no son contiguos, la CPU falla más en caché y NumPy pierde ventaja.

## Bloque F — Experimentación (preguntas para guiar un mini-lab)
**18. Si repites el benchmark con float32 en lugar de float64, ¿qué esperas que pase con:    
    - Velocidad  
    - Consumo de memoria**  
Velocidad: float32 suele ser más rápido; Memoria: consume la mitad.    

**19. ¿Qué ocurre si el array es muy pequeño (por ejemplo 100 o 1.000 elementos)? ¿Sigue ganando NumPy? ¿Por qué podría no compensar?**  
NumPy puede no ganar; el overhead de crear arrays supera la ganancia.

**20. Si tu cálculo vectorizado crea muchos arrays temporales (a+b+c+d), ¿qué coste oculto aparece?**  
El coste oculto es crear/copiar arrays intermedios.

**21. ¿Qué técnicas conoces para reducir temporales? (pista: operaciones in-place, out=, composición, etc.)**  
Operaciones in‑place (+=), out=, fusionar expresiones.

**22. Si haces np.sin(x) y luego np.sum(...), ¿qué parte esperas que sea el cuello de botella: el cálculo o el acceso a memoria?**  
En arrays grandes el cuello suele ser acceso a memoria, no el cálculo.

## Bloque G — Cuándo NO usar NumPy (o cuándo no es la mejor primera opción)
**23. Si tu operación por elemento incluye una lógica compleja con ramas (if/elif/else), ¿crees que NumPy seguirá siendo tan ventajoso? ¿Por qué?**  
Si la operación tiene lógica compleja con ramas → NumPy pierde eficiencia.

**24. Si el problema es principalmente de I/O (leer archivos, parsear JSON, llamadas a red), ¿tiene sentido optimizar con NumPy? ¿Qué optimizarías antes?**  
Si el problema es I/O (disco/red) → NumPy no soluciona nada; optimizas el I/O.

**25. Si necesitas estructuras heterogéneas (mezcla de tipos, objetos), ¿encaja NumPy o encaja mejor otra estructura? ¿Por qué?**  
Si necesitas datos heterogéneos (objetos distintos) → mejor listas, dicts o pandas.

**26. ¿Qué pasa si tu algoritmo es inherentemente secuencial y depende del resultado del paso anterior (no vectorizable)? ¿Qué opciones existen?**  
Si el algoritmo depende del paso anterior (no vectorizable) → usa bucles, Numba o Cython.

## Bloque H — Decisión técnica (reglas prácticas que deberían inferir)
**27. Completa esta frase con tu criterio: “Usaré NumPy cuando …” (mínimo 3 condiciones).**  
Los datos sean grandes y numéricos; La operación sea repetitiva y vectorizable; Importe el rendimiento y aprovechar C/SIMD.

**28. Completa esta frase: “No merece la pena usar NumPy cuando …” (mínimo 3 casos).**  
El array es pequeño; Hay lógica compleja por elemento; Trabajo principalmente de I/O.

**29. Si te piden acelerar un programa, ¿qué medirías primero para decidir si NumPy es la solución?**  
Un perfilado simple: saber si el cuello es CPU, memoria o I/O.

**30. Si el cuello de botella no es CPU sino memoria (RAM/cache), ¿qué estrategias aplicarías antes que “más vectorización”?  
Optimizar contigüidad, evitar temporales, usar tipos más pequeños (float32), revisar slicing.

## Bloque I — Preguntas de cierre (para consolidar conclusiones)
**31. Resume en una frase: ¿qué ventaja principal aporta NumPy frente a bucles Python?**  
Ventaja principal: procesa datos en C de forma vectorizada, mucho más rápido que Python.

**32. Resume en una frase: ¿cuál es el coste oculto típico al usar NumPy sin cuidado?**  
Coste oculto: crear arrays temporales gigantes sin necesidad.

**33. ¿Qué “señales” en un problema te indican que probablemente sea vectorizable?**  
Señales de vectorización: operaciones numéricas repetidas, sin dependencias entre elementos.

**34. ¿Qué “señales” te indican que probablemente no lo sea y requerirá otro enfoque?**  
Señales de no vectorización: lógica con ramas, dependencia secuencial, estructuras de objetos.
