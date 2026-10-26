# Clasificador temático del banco de preguntas

**Integración propuesta v0.3 · 26 de octubre de 2026.**  
**Estado:** diseño y piloto de anotación; todavía no hay un modelo entrenado.

## 1. Aporte de la idea del compañero

La propuesta original del compañero consiste en aprender a clasificar frases cortas por temática a partir de ejemplos. El PDF original se conserva en el repositorio privado de la materia. No se copia a este repositorio público.

Se conserva ese problema de aprendizaje supervisado y se integra en Aula como **organizador temático de preguntas**. La entrada será el enunciado de una pregunta escrita o importada; la salida será una sugerencia de tema que el docente puede corregir. Su utilidad es ordenar preguntas que no vienen clasificadas, filtrar el banco y observar distribución temática. No se usará para redescubrir el título conocido de un capítulo.

El modelo no determina si la pregunta es buena, si la clave es correcta ni su dificultad. Tampoco se presenta como un clasificador universal de cualquier materia.

## 2. Alcance acotado

La prueba inicial usa tres categorías:

| Etiqueta | Conceptos centrales | Límites de anotación |
|---|---|---|
| Representación y vecinos | Vectores, producto escalar, norma, coseno, escalas/distancias y 1-NN/K-NN. | Si la pregunta evalúa cómo prevenir contaminación de test, predomina Datos y evaluación. |
| Datos y evaluación | Particiones, leakage, faltantes/atípicos, desbalance, métricas y matriz de confusión. | Si pide explicar dinámica del entrenamiento de una red, predomina Redes y aprendizaje. |
| Redes y aprendizaje | Neuronas, activaciones, forward/backprop, optimizadores y sobreajuste de redes. | La mera presencia de la palabra “modelo” no basta para asignar esta clase. |

Las categorías deben revisarse con el compañero antes de fijarlas. Son unidades de un caso de estudio de IA; no son clases suficientes para deportes, medicina o cualquier otra asignatura. El editor puede usarse con otros temas mediante etiquetas manuales, sin atribuir al clasificador conocimientos que no se entrenaron.

Si un ejemplo mezcla objetivos o no pertenece claramente a estas categorías, marcarlo para revisión. No forzar etiquetas ni eliminar casos difíciles para aparentar mejores resultados. Definir el concepto evaluado, no solo palabras superficiales.

## 3. Datos piloto preparados

[datos/piloto_clasificacion.json](datos/piloto_clasificacion.json) contiene **30 enunciados de ejemplo, diez por categoría**, redactados para explorar el diseño. Las etiquetas fueron propuestas por el asistente y están pendientes de revisión humana. No son exámenes reales ni etiquetas validadas.

Cada par de preguntas del mismo concepto comparte `grupo_conceptual`. Esto hace visible que una partición aleatoria por fila podría repartir paráfrasis relacionadas entre entrenamiento y prueba. La división posterior debe respetar grupos conceptuales y, cuando corresponda, documento/origen.

Este piloto sirve para revisar la anotación y comprobar el flujo técnico. No alcanza para afirmar que un modelo generaliza. Antes de evaluar el producto deben añadirse preguntas de formulación más diversa y casos independientes. Los ejemplos ya usados para explorar o corregir el procedimiento no se convierten después en un test independiente.

## 4. Primer experimento recomendado

1. Ambos integrantes revisan categorías y etiquetan por separado los ejemplos; registran desacuerdos y los resuelven por concepto.
2. Añaden ejemplos independientes, incluidos enunciados breves, palabras compartidas y casos mixtos.
3. Definen una partición por grupos antes de ajustar el modelo. Con tan pocos grupos, cualquier métrica se informa con su cantidad de casos y sus limitaciones.
4. Construyen una referencia por palabras clave.
5. Comparan esa referencia con **TF-IDF + regresión logística**. K-NN queda como alternativa si surge una razón concreta para compararlo, no como tercer modelo obligatorio.
6. Registran matriz de confusión, métricas por clase y macro-F1, además de ejemplos de error.
7. Comprueban inferencia sin internet y concordancia entre la versión de desarrollo y la del navegador.

El vocabulario y las estadísticas TF-IDF del experimento se ajustan solo con entrenamiento. No incluir el tema esperado, el encabezado del documento ni la etiqueta en el texto de entrada. No reutilizar el conjunto de prueba para seleccionar parámetros.

## 5. Implementación prevista, sin hardware especial

El entrenamiento se realizaría durante el desarrollo, con Python y herramientas clásicas. Se exportarían vocabulario, valores IDF, coeficientes, interceptos y etiquetas. El navegador ejecutaría la transformación del enunciado y el cálculo lineal de puntuaciones en JavaScript. El docente no necesita Python ni descargar un LLM para esa predicción.

Hay que fijar y reproducir tokenización, normalización y orden de vocabulario exactamente en ambos entornos. Esta exportación es una tarea pendiente, no una compatibilidad ya implementada. El tamaño y los tiempos se medirán antes de afirmar que son adecuados.

No mostrar “confianza” como certeza. Un valor de salida del modelo no garantiza calibración. Si una entrada no contiene términos conocidos, informar falta de evidencia en lugar de producir una sugerencia basada solo en el intercepto. Detectar todos los temas desconocidos es otro problema: se conserva corrección manual.

## 6. Relación con los ejercicios de la cátedra

- TF-IDF y clasificación de texto: ejemplos de NLP del notebook C3A.
- Regresión logística y fronteras: prácticas de clasificación y logística.
- K-NN: antecedente conceptual de clasificación por ejemplos, si se compara esa variante.
- Datos, etiquetas y particiones: prevención de fuga y definición de una referencia válida.
- Matriz de confusión y análisis de errores: evaluación por tema, sin reducir la conclusión a accuracy.

El sistema explicará qué parte se entrenó y qué parte usa reglas, búsqueda o modelos externos. La clasificación será una contribución propia identificable dentro del integrador.

## 7. Control de alcance

Se incorpora como módulo propuesto de IA offline. Para compensar, las plantillas automáticas de preguntas pasan a ampliación; el núcleo sigue permitiendo edición manual y recuperación. No se añaden embeddings, múltiples clasificadores o conectores por defecto.

La primera validación del módulo es revisar datos, entrenar un piloto cuando se autorice esa fase y medir la portabilidad. Si no existe señal útil o las categorías no se sostienen, se documenta y revisa el alcance con la cátedra antes de prometer una precisión o eliminar el módulo silenciosamente.

## 8. Estado de la demo

Las etiquetas temáticas de la demo son ejemplos precargados. La corrección manual puede mostrarse, pero no se ejecuta un clasificador entrenado. No confundir esa interacción con resultados del experimento futuro.
