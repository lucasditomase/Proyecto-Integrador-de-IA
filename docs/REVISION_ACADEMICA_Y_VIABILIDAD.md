# Revisión académica, de alcance y viabilidad

**26 de octubre de 2026 · propuesta v0.3 · revisión previa a implementación.**

## Dictamen y nivel de evidencia

La idea es pertinente para un integrador de IA y el mínimo tiene una implementación técnicamente plausible con herramientas gratuitas y procesamiento liviano. **Todavía no demuestra aprendizaje experimental realizado ni compatibilidad final:** eso requerirá construir y evaluar los métodos, justificar decisiones y mostrar errores. La demo prueba un flujo de interacción con ejemplos preparados.

No se identificó una promesa técnicamente imposible en el mínimo si se respetan sus límites: texto sencillo, corpus acotado, edición manual sin API, clasificador de tres temas, intercambio externo manual y API directa solo condicional. Dos semanas son un objetivo de planificación, no una estimación garantizada: faltan horas y reparto reales.

Se revisaron nuevamente estructura y contenidos pertinentes de las 16 clases HTML originales incluidas en el ZIP del índice teórico, las prácticas HTML y la estructura de los 13 scripts, y especialmente los ejemplos de representación, clasificación/logística y NLP/TF-IDF de C3A. Se contrastaron alcance, informe, plan, guion, código HTML y artefactos de presentación. Esta revisión es focalizada; no reejecuta entrenamientos ni certifica cada diapositiva, notebook o resultado docente.

## 1. Contenidos de la cátedra y evidencia que debe producir el grupo

Las referencias de clases corresponden a los HTML originales conservados en el repositorio privado de teoría. No se copian aquí esos materiales.

| Material y concepto | Aplicación concreta en Aula | Evidencia pendiente para la defensa |
|---|---|---|
| Clases 1–2 y prácticas de representación/primer modelo | Definir docente, entrada, salida y necesidad; convertir fragmentos y consultas en vectores. | Un ejemplo calculado de producto, norma y coseno; explicar qué información pierde la representación. |
| Clase 3 y práctica de calidad | Procedencia, duplicados, etiquetas, cobertura, particiones y fuga. | Dataset descrito, desacuerdos de anotación y partición por grupos antes del ajuste. |
| Clase 5; scripts de umbral y logística | Clasificador temático TF-IDF + regresión logística; decisión corregible. | Palabras clave y clase mayoritaria como referencias; matriz de confusión, macro-F1 y errores por clase con cantidad de casos. |
| Clase 8 | Distinguir ajuste, configuración y evaluación; controlar generalización. | Configuración registrada y prueba reservada. No afirmar que se implementó una red, Adam o backprop por entrenar logística con una biblioteca. |
| Clase 10 y notebook C3A, bloque de clasificación de opiniones | TF-IDF para recuperar fragmentos y representar preguntas. | Comparar recuperación por coincidencia simple frente a TF-IDF/coseno sobre las mismas consultas; clasificador separado de recuperación. |
| Clase 11 | Seleccionar contexto para un asistente generativo y evaluar respaldo. | Si se usa asistencia externa: conservar pedido, fragmentos, salida y correcciones. Un intercambio manual aplica la idea, sin ser un pipeline automático de RAG. |
| Clase 14 | Decidir procesamiento local/externo, costo, privacidad y supervisión. | Qué queda local, qué se envía si el docente lo decide, errores y límites. No tratar documentos cargados como instrucciones del sistema. |
| Clase 15 | Artefactos, contratos, versiones y coherencia entrenamiento/inferencia. | Formato de proyecto, versión del modelo/datos y concordancia Python/JavaScript; no exigir infraestructura MLOps completa. |
| Clase 16 | Relacionar necesidad, baseline, experimento, sistema y utilidad. | Demostración normal y límite, reproducibilidad, análisis de fallos y límites del valor aportado. |

Las clases 4 (regresión de valores continuos), 6–7 (redes y backprop), 9 (visión), 12–13 (AG/TSP) no son módulos propios comprometidos. La regresión logística aquí resuelve clasificación; no equivale a implementar regresión de consumo, una red profunda o un algoritmo genético. Que las preguntas del examen mencionen esos temas no demuestra haberlos aplicado en el sistema.

**Suficiencia académica:** el proyecto puede defenderse por dos tareas medibles (recuperación y clasificación), incluso sin generación externa. Usar una API o construir un editor por sí solos serían evidencia insuficiente de haber estudiado los métodos. La aceptación definitiva corresponde a la cátedra; no consta aprobación.

## 2. Experimentos pequeños y útiles

- **Recuperación:** preparar consultas y fragmentos relevantes identificados; fijar k, por ejemplo 3, y medir Precision@k y/o MRR sobre los mismos casos para coincidencia simple y TF-IDF. Reservar consultas antes de ajustar. Incluir paráfrasis, negaciones y una consulta sin respaldo; no declarar semántico un método que falla con sinónimos.
- **Clasificación:** revisar y ampliar los 30 ejemplos provisionales. Comparar palabras clave y mayoría con TF-IDF/logística usando una partición común por grupos conceptuales/origen. Ajustar vocabulario e IDF del clasificador solo con entrenamiento. Informar errores y tamaños por clase; no garantizar mejora frente al baseline ni precisión mínima sin medirla.
- **Contextos distintos de TF-IDF:** en recuperación se puede indexar el documento completo que el usuario proporciona porque ese documento estará disponible al buscar. Eso no autoriza incluir etiquetas o preguntas de prueba al ajustar el clasificador. Explicar ambos corpus por separado.
- **Utilidad:** contrastar búsqueda/etiquetado manual y asistido en una pequeña tarea comparable; registrar correcciones y tiempo si se mide. No afirmar ahorro de tiempo o mejora pedagógica a partir de una interfaz atractiva.
- **Contenido:** verificar una muestra de preguntas contra fuentes, claridad y clave. Una clasificación temática acertada no demuestra que la pregunta o su respuesta sean correctas.

Un resultado negativo honesto puede justificar preferir el baseline. Lo que se promete es estudiar, comparar y explicar, no que logística gane siempre. Los datos explorados al diseñar el sistema no se transforman después en una prueba independiente.

## 3. Propuesta frente a demo y desarrollo pendiente

| Función propuesta | Demo v0.3 y código actual | Ruta de implementación prevista |
|---|---|---|
| Material propio TXT/Markdown/texto | Previsualiza texto; bloquea el borrador si difiere del apunte. HTML se acepta solo en la previsualización; no añade soporte HTML/PDF al mínimo. | Leer archivo seleccionado o texto pegado, normalizar y fragmentar conservando referencias. |
| Recuperación real | No implementada; banco preparado. | Índice TF-IDF/coseno y baseline léxico en JavaScript, con resultados y límites visibles. |
| Clasificación temática | Etiquetas precargadas y corrección manual. | Entrenar en desarrollo, exportar vocabulario/IDF/pesos/sesgos/etiquetas y reproducir transformación e inferencia en navegador. |
| Configuración y revisión | Funciona con variantes, cuatro opciones y una/dos correctas, edición y aprobación. | Aplicar las mismas validaciones a preguntas propias/importadas; fuente y fundamento requieren revisión. |
| Guardar/retomar proyectos | No implementado; al recargar se pierde el estado. | Exportar/importar JSON versionado con validación de estructura; sin claves API. |
| Examen/clave separados | Descarga HTML de ejemplos aprobados; la función de exportación excluye claves y explicaciones del archivo del alumno. | Reutilizar ese contrato con preguntas reales. Imprimir un borrador docente no equivale a exportar el examen del alumno. |
| Asistencia externa | Modos explicativos con los mismos ejemplos; no hay API. | Pedido e importación estructurada manual primero; rechazar salidas inválidas y mantener revisión docente. |
| API directa | No implementada ni proveedor elegido. | Solo si un acceso permitido, gratuito para la prueba del grupo, resulta viable y queda tiempo. No es condición de aceptación del núcleo. |

En la nueva comprobación de interfaz sobre macOS/navegador integrado y localhost: el material propio deshabilitó preparar el borrador; restaurar el apunte lo habilitó; el modo mixto produjo una y dos respuestas correctas; el modo asistido siguió indicando simulación sin conexión. La revisión estática confirmó ausencia de scripts/estilos externos y de llamadas de inferencia en la demo. No es una prueba en todos los navegadores, de modo avión ni de la aplicación final.

No hay una implementación final contra la cual ejecutar aceptación completa. La comparación actual es **propuesta ↔ prototipo ↔ diseño pendiente**, y no puede certificar funciones que aún no existen.

## 4. Ruta técnica viable y tamaño del problema

El núcleo puede usar operaciones numéricas y texto en JavaScript, sin GPU ni un LLM. El entrenamiento clásico se hace en las computadoras del grupo con herramientas gratuitas; los docentes reciben solo la inferencia exportada. El tamaño y latencia reales están pendientes.

Como presupuesto de diseño inicial, no como benchmark: con vocabulario limitado a 2.000 términos y tres clases, una matriz de pesos tiene 6.000 coeficientes (48.000 bytes de valores float64 sin contar vocabulario, IDF, serialización ni objetos JavaScript). Eso es distinto de distribuir miles de millones de parámetros. No demuestra rendimiento ni exactitud; hay que medir el artefacto final y el caso de uso.

Empezar con documentos acotados y bancos pequeños; ensayar un material de hasta 1 MB y algunos cientos de fragmentos antes de ampliar. Definir límites y mensajes al validar, sin prometer tamaño ilimitado. Preferir representaciones dispersas; no generar todas las comparaciones entre pares ni cargar un modelo por pregunta.

El riesgo principal del clasificador es la calidad/cantidad de datos y reproducir tokenización, pesos e IDF en ambos entornos. El riesgo de cronograma es intentar a la vez PDF/OCR, varios proveedores y generación offline. Esas ampliaciones siguen fuera del mínimo. No se requiere migrar a servidor para las tareas locales descritas.

Para conservar apertura de HTML descargado sin servidor: incluir código, recursos y parámetros en el artefacto final, evitando fetch obligatorio de JSON local, imports externos o CDN. Guardar mediante archivos que el usuario descarga/importa; no depender de permisos avanzados del sistema de archivos ni de almacenamiento ligado a un origen. La construcción del artefacto puede usar herramientas del desarrollador, sin trasladarlas al docente. MDN documenta restricciones de módulos cargados desde file://; por eso servir la demo por localhost en QA no prueba por sí solo la versión descargada. [Módulos JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

## 5. Costo monetario

| Componente | ¿Requiere pago obligatorio en este diseño? | Condición |
|---|---|---|
| Núcleo HTML/JS, recuperación e inferencia clásica | No | Equipo/navegador existentes, sin servicios remotos obligatorios. |
| Desarrollo y entrenamiento pequeño | No se prevé licencia, nube o GPU paga | Usar herramientas gratuitas y corpus permitido; trabajo y electricidad son recursos existentes, no costo total nulo. |
| Publicación de demo en Pages | No, con repo público y GitHub Free | Mantener límites del servicio, dominio github.io y workflow estándar; no comprar dominio ni runners ampliados. |
| Copia descargada | No necesita hosting durante el uso | Descargarla inicialmente o recibirla por archivo; incluir los recursos del núcleo. |
| Asistente externo o API aportada por el usuario | No se garantiza gratuidad | Opcional, sujeto a sus condiciones y cuotas; el núcleo y la evaluación local deben poder completarse sin él. |

GitHub documenta Pages disponible con GitHub Free para repositorios públicos y como alojamiento estático; tiene límites de tamaño y tráfico. El workflow actual usa ubuntu-latest estándar. La documentación de Actions distingue ejecución gratuita en runners estándar de repos públicos de otros usos que pueden generar cargos. Esto valida una ruta sin hosting pago, no una auditoría de toda la facturación de la cuenta. [Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [límites](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), [Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions). Fuentes consultadas el 26/10/2026.

**Conclusión de costo:** el núcleo y su demostración académica pueden diseñarse sin pagos adicionales obligatorios. No es correcto prometer generación externa automática gratis, cuota ilimitada, cero consumo de energía o continuidad perpetua de terceros. Si no hay acceso gratuito permitido, no usar API para demostrar el núcleo ni contratar una para completar la entrega.

## 6. Software, sistemas y hardware de profesores

Objetivo verificable: navegador de escritorio actual con JavaScript, lectura de archivos elegidos por el usuario y descarga permitidas, sobre Windows, macOS o Linux. No exige instalar Python, Node, terminal, Docker, extensiones, cuentas ni un modelo. No se garantiza cualquier versión histórica de un sistema o navegador, teléfonos, navegadores embebidos o equipos con políticas que prohíban JavaScript/archivos.

La File API permite leer archivos seleccionados por el usuario y trabajar con Blob para descargas; el editor actual usa dialog, disponible en navegadores modernos. Es evidencia de viabilidad del enfoque, no una certificación del producto en todos ellos. [File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications), [dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog).

| Entorno de aceptación previsto | Estado en esta revisión |
|---|---|
| macOS + navegador integrado, localhost, demo | Flujo limitado comprobado; no sustituye Safari/Chrome/Firefox finales. |
| Windows + Edge/Chrome actual | Pendiente de prueba en ese sistema. |
| Linux + Firefox/Chromium actual | Pendiente de prueba en ese sistema. |
| macOS + Safari/Firefox/Chrome actual | Pendiente de matriz final. |
| HTML descargado sin red, modelo incluido, importar/exportar proyecto | Pendiente en la implementación final; no se probó aquí con file://. |
| Equipo común con memoria limitada | Pendiente de medir tiempos, tamaño y memoria; no fijar mínimos de RAM/CPU sin evidencia. |

Los docentes necesitarán conexión para abrir Pages por primera vez o usar un servicio externo; el núcleo descargado debe seguir funcionando sin ella. Si la institución bloquea descargas o ejecución local, se debe verificar una modalidad permitida con esa institución: no prometer eludir restricciones. Un archivo HTML tampoco puede compensar un navegador obsoleto sin soporte.

## 7. Condiciones antes de declarar terminado el integrador

1. Mostrar los dos experimentos con datos descritos, particiones correctas y errores, sin depender de una llamada paga.
2. Comprobar concordancia de predicción entre Python y JS en casos reservados, texto sin vocabulario conocido y categorías fuera del alcance con revisión manual. No prometer detección perfecta fuera de dominio.
3. Completar un examen con material propio, sin API; guardar, reabrir y exportar examen sin clave docente.
4. Probar copia descargada sin red y sin dependencias remotas. Registrar sistema, navegador/versión, corpus y resultado en la matriz de compatibilidad.
5. Medir al menos tamaño del artefacto, tiempos de indexación/consulta/clasificación y respuesta de la interfaz en un equipo común disponible.
6. Si se demuestra asistencia generativa, identificar qué asistente se usó, si el paso fue manual o API, sus condiciones y las correcciones necesarias. No hacer depender la defensa del acceso ajeno.
7. Pedir devolución de la cátedra sobre el alcance y registrar ajustes. No interpretar este informe como aprobación docente.

**Decisión recomendada:** mantener el mínimo v0.3 y validar primero datos, recuperación, clasificación y distribución local. La viabilidad es favorable; las garantías de exactitud, compatibilidad y rendimiento quedan sujetas a pruebas de implementación, no se inventan en esta fase.
