# Aula: plan consolidado del integrador

**Revisión:** 15 de noviembre de 2026, tras contrastar el alcance v0.3 con los 22 laboratorios.

**Estado:** planificación previa a la implementación.

## 1. Punto de partida

El [documento de decisiones y opciones](DECISIONES_Y_OPCIONES.md) es la referencia para requisitos y alternativas. El [alcance de presentación v0.3](ALCANCE_DE_LA_PROPUESTA.md) se comparte con el informe, PDF, demo y paquete. La [verificación previa a implementar](docs/VERIFICACION_PREVIA_A_IMPLEMENTAR.md) vincula los hitos con las evidencias de la cátedra.

Objetivo: herramienta para elaborar exámenes multiple choice con material docente, revisión y exportación. Dos personas, dos semanas como objetivo, máximo orientativo de tres. Cero gastos del grupo y un recorrido gratuito sin clave para los docentes.

La demo pública actual usa preguntas preparadas. No representa una implementación de procesamiento real, recuperación ni IA.

## 2. Alcance recomendado

### Primera versión

1. Interfaz HTML/JavaScript utilizable desde navegador y como copia descargada.
2. Material propio mediante TXT/Markdown o texto pegado.
3. Fragmentos con procedencia y búsqueda liviana mediante TF-IDF/coseno.
4. Editor de preguntas con cuatro opciones y una/dos respuestas correctas.
5. Organizador temático de preguntas con un clasificador pequeño propuesto y corrección manual. Tres categorías iniciales; prueba de datos/modelo antes de prometer resultados.
6. Guardado e importación de un proyecto, y examen/clave separados.
7. Preparación e importación de un intercambio manual con un asistente externo; una integración API directa solo si pasa la prueba de viabilidad.
8. Casos de evaluación y explicación del procedimiento.

### Ampliaciones condicionadas

Plantillas extractivas automáticas, PDF con texto seleccionable, embeddings, consola de usuario, integración con agentes, PWA y más proveedores. Elegir solo lo que tenga utilidad comprobable y tiempo disponible.

### Fuera del objetivo

Entrenar un LLM, exigir hardware potente, servidor pago, cuentas de alumnos, corrección automática de estudiantes, predicción de dificultad pedagógica, OCR y una plataforma educativa completa.

## 3. Prueba de viabilidad antes de fijar arquitectura

Primer trabajo de desarrollo: comprobar que el HTML descargado abre con los recursos incluidos, que admite texto propio y que permite leer y descargar un archivo sin red. Acordar en paralelo el corpus y los contratos de archivo.

| Comprobación | Resultado necesario | Si falla |
|---|---|---|
| Recorrido básico | Abrir texto propio y recuperar fragmentos sin servicios externos. | Simplificar formato y corpus. |
| Intercambio externo mínimo | El pedido y las preguntas importadas tienen un formato verificable y revisable. | Simplificar formato sin exigir una API. |
| API directa opcional | Solo si se intenta: acceso permitido desde navegador con clave propia y una prueba sin pago del grupo. | Conservar intercambio manual y documentar que no hay conexión directa. |
| Presupuesto | La prueba no requiere pagos del grupo; existe una vía de evaluación sin gasto. | No contratar ni consumir una API paga; revisar alcance conectado. |
| Salida | Un candidato de prueba válido entra en el editor y uno inválido deja intacto el proyecto abierto. | Simplificar el formato y conservar validación y revisión docente. |
| Portabilidad | El recorrido básico no depende de macOS ni de recursos específicos del equipo. | Quitar la dependencia o reconsiderar distribución. |

No intentar resolver una restricción de uso de un proveedor reutilizando credenciales de otra aplicación ni eludiendo sus condiciones. No hacer públicas claves ni pedirlas en el chat. La prueba deberá usar un acceso dispuesto específicamente para ella.

Decisión de salida: validar el núcleo local y el intercambio manual; la API directa es una ampliación condicionada y no bloquea la aceptación del mínimo. Por ahora ninguna conexión está comprobada.

## 4. Etapas y resultados revisables

| Etapa | Trabajo | Criterio de finalización |
|---|---|---|
| A. Organizar | Acordar reparto y disponibilidad. Consultar el EVA o la cátedra por el formato y la fecha final. | Responsables acordados y estado de la entrega registrado. |
| B. Viabilidad | Probar HTML local y fijar formato de proyecto, preguntas y fuentes. En paralelo, revisar etiquetas y preparar casos reservados. | Prueba local registrada y datos/contratos descritos antes del ajuste. |
| C. Base offline | Texto propio, búsqueda, editor, configuración, guardado y exportación. | Crear y terminar un examen nuevo sin clave y sin conexión. |
| D. Clasificador temático | Revisar etiquetas, comparar palabras clave con TF-IDF/regresión logística y preparar inferencia liviana. | Categorías delimitadas, evaluación por grupos y predicción revisable; sin exigir Python al docente. |
| E. Asistencia externa | Pedido e importación manual estructurada; API con clave de sesión solo si se valida. | Añadir preguntas externas revisables sin bloquear el modo básico; documentar si el intercambio es manual o conectado. |
| F. Evaluar | Probar casos reservados, revisar preguntas y explicar errores. | Comparación pequeña y resultados trazables. |
| G. Entregar | Instrucciones, versión descargable, demo y exposición. | Otra persona puede recorrer el flujo sin ayuda técnica extensa. |

No se trabaja primero en conectores múltiples ni en una interfaz elaborada. La versión offline completa es el primer resultado útil; el contenido académico de búsqueda y selección no debe quedar reducido a un editor genérico.

## 5. Contenidos y evidencia académica

| Contenido | Aplicación | Evidencia |
|---|---|---|
| Representación y calidad | Texto, fragmentos y metadatos. | Ejemplos de extracción/segmentación correcta e incorrecta. |
| Álgebra vectorial | TF-IDF, producto escalar, norma y coseno. | Ejemplo calculado y ranking de fragmentos. |
| Baseline y evaluación | Comparar coincidencia simple de términos con TF-IDF/coseno. | Mismas consultas, referencias relevantes y análisis de errores. |
| NLP y RAG | Seleccionar contexto antes de generar con un modelo preentrenado. | Fragmentos enviados, preguntas y respaldo observado. |
| Clasificación temática propuesta | Organizar preguntas de tres temas con TF-IDF/regresión logística. | Revisión de etiquetas, partición por grupos, baseline y matriz de confusión. |
| Sistema y supervisión | Controles estructurales, edición y conservación del trabajo ante fallas. | Matriz de riesgos, casos inválidos o sin respaldo, control docente y acción ante cambios en las entradas. |

La comparación TF-IDF/embeddings explorada inicialmente queda como ampliación posible. No es obligatorio incluir embeddings si ello contradice el modo offline liviano o el presupuesto. Una comparación sencilla bien realizada sigue siendo valiosa.

## 6. Evaluación proporcionada

Usar material acotado de tres unidades. Identificar de antemano los fragmentos pertinentes y reservar consultas literales, paráfrasis y un caso sin respaldo. Comparar coincidencia de términos y TF-IDF/coseno con las mismas consultas y el mismo valor de k. Reportar Precision@k o MRR, ejemplos de error y la decisión que se tomó a partir de ellos.

Revisar una muestra pequeña de preguntas, inicialmente del orden de 20 entre los modos disponibles. Registrar corrección de clave, claridad, tema, respaldo y cambios necesarios. Ambos integrantes revisan y contrastan discrepancias con el material. No presentar esta revisión como validación pedagógica general ni atribuir confianza estadística a una muestra pequeña.

El [diseño del clasificador](CLASIFICADOR_TEMATICO.md) y sus 30 ejemplos piloto están preparados para revisión; no hay un modelo entrenado. Revisar etiquetas y añadir ejemplos independientes. Acordar particiones por grupos antes de ajustar vocabulario y modelo. Comparar palabras clave y regresión logística en los mismos casos reservados, con matriz de confusión, macro-F1 y cantidad de casos por clase. Comprobar que Python y JavaScript coinciden sobre entradas de prueba.

Para la defensa, guardar versión de datos y código, particiones, configuración, comando de reproducción, resultados, un error representativo y su límite. El JSON acumulativo de la cátedra registra avances académicos. El archivo de Aula guarda el examen en edición.

## 7. Criterios de aceptación del producto

- Con un documento propio se puede construir, revisar, guardar y exportar un examen sin API.
- La copia descargada permite completar el recorrido sin red con los recursos incorporados. Registrar sistema, navegador, tamaño del archivo y tiempos al probar Windows, macOS y Linux.
- Cambiar la cantidad de respuestas correctas se refleja en instrucciones y validaciones estructurales.
- El archivo del alumno excluye las respuestas marcadas y los fundamentos, también en el código fuente del HTML.
- Reabrir el archivo de proyecto conserva las preguntas, claves y referencias; las claves API no se exportan.
- Un candidato válido se puede importar y revisar mediante el intercambio manual. Una importación inválida conserva el proyecto abierto. Ambos casos se pueden probar con archivos preparados.
- Si se incorpora una API directa, el docente puede decidir qué enviar al proveedor identificado. Ante una falla se conserva el proyecto y queda disponible el recorrido offline.
- Se distingue una referencia existente de una referencia que realmente respalda una afirmación.
- Hay un conjunto pequeño de ejemplos que permite explicar qué se aplicó y qué limitaciones existen.

## 8. Orden de trabajo y calendario

El 9 de noviembre y el margen hasta el 16 fueron estimaciones internas de octubre. El cierre del 30 de octubre correspondía a la propuesta inicial. Acordar un calendario desde el inicio efectivo según la disponibilidad de ambos y confirmar la fecha final de la cátedra.

- **Primer hito:** completar un examen con texto propio, recuperación por términos, editor, guardado, reapertura y exportación desde el HTML descargado. En paralelo, ambos revisan el piloto y reservan casos de evaluación.
- **Segundo hito:** incorporar TF-IDF/coseno y el clasificador temático, ejecutar las comparaciones y comprobar la inferencia en navegador.
- **Tercer hito:** completar el intercambio manual, probar casos límite y portabilidad, y preparar una defensa reproducible. La conexión API puede evaluarse después de cerrar el mínimo, si hay acceso viable y tiempo disponible.

Reparto propuesto: una persona trabaja en recuperación y clasificación. La otra se ocupa del editor, archivos y exportación. Ambas revisan etiquetas, reproducen las pruebas y preparan la defensa.

## 9. Política de recorte

Conservar: material real, recuperación explicable, banco editable, referencias, guardado/exportación y evaluación.

Recortar primero: apariencia avanzada, PDF, conectores de agentes, múltiples proveedores, PWA y plantillas automáticas. El clasificador se valida temprano para no recortarlo silenciosamente al final.

Si la integración externa no funciona bajo las condiciones de costo/acceso, documentarlo y revisar con la cátedra qué alcance demuestra suficientemente la aplicación de IA. No sustituir una función prometida por una simulación sin explicitarlo.

## 10. Siguiente decisión

Acordar con el compañero el reparto, el corpus inicial y los casos reservados. Confirmar en el EVA fecha y formato de entrega. El recorrido previsto combina HTML descargable, núcleo offline e intercambio manual. La elección de proveedor queda para el caso en que se decida probar una API directa.

## Integración acordada para planificar

Se adopta la propuesta del compañero como organizador temático, con [protocolo y datos piloto](CLASIFICADOR_TEMATICO.md). Las plantillas automáticas pasan a ampliación: se reemplaza una función prevista por un módulo de aprendizaje supervisado más vinculado a los ejercicios, sin ampliar indiscriminadamente la lista de tareas. No se inicia implementación real en esta actualización.

## Revisión académica y de viabilidad

La [auditoría del 26 de octubre](docs/REVISION_ACADEMICA_Y_VIABILIDAD.md) vincula métodos con material original, define evidencia experimental y distingue costo monetario obligatorio de uso externo opcional. Compatibilidad objetivo: navegadores actuales en Windows, macOS y Linux, pendiente de pruebas en los sistemas finales. No prometer cualquier equipo/navegador ni rendimiento sin medir. Mantener un artefacto local con recursos/modelo incluidos, sin servidor ni Python obligatorio para docentes.
