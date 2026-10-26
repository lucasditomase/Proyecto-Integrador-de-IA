# Aula: plan consolidado del integrador

**Versión:** 26 de octubre de 2026, después de acordar presupuesto cero y explorar web, consola, modelos pequeños y claves propias.  
**Estado:** plan recomendado para decidir. No se inició la implementación real.

## 1. Punto de partida

El [documento de decisiones y opciones](DECISIONES_Y_OPCIONES.md) es la referencia para requisitos y alternativas. El [alcance de presentación v0.3](ALCANCE_DE_LA_PROPUESTA.md) se comparte con el informe, PDF, demo y paquete. La versión inicial queda en el historial de Git.

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

Duración propuesta: una sesión corta de desarrollo, una vez autorizado ese paso.

| Comprobación | Resultado necesario | Si falla |
|---|---|---|
| Recorrido básico | Abrir texto propio y recuperar fragmentos sin servicios externos. | Simplificar formato y corpus. |
| Acceso API | Un proveedor permite una solicitud desde el navegador con clave de usuario y devuelve salida utilizable. | Probar una alternativa autorizada o exportación/importación; evaluar consola/intermediario mínimo solo si es necesario. |
| Presupuesto | La prueba no requiere pagos del grupo; existe una vía de evaluación sin gasto. | No contratar ni consumir una API paga; revisar alcance conectado. |
| Salida | Las preguntas pueden convertirse al formato común y corregirse en el editor. | Reducir estructura solicitada o elegir otro modelo. |
| Portabilidad | El recorrido básico no depende de macOS ni de recursos específicos del equipo. | Quitar la dependencia o reconsiderar distribución. |

No intentar resolver una restricción de uso de un proveedor reutilizando credenciales de otra aplicación ni eludiendo sus condiciones. No hacer públicas claves ni pedirlas en el chat. La prueba deberá usar un acceso dispuesto específicamente para ella.

Decisión de salida: confirmar web + API directa, o documentar una alternativa antes de construir el sistema completo. Por ahora ninguna conexión está comprobada.

## 4. Etapas y resultados revisables

| Etapa | Trabajo | Criterio de finalización |
|---|---|---|
| A. Decidir | Revisar este documento con el compañero y la devolución de la cátedra. | Interfaz principal, alcance mínimo y reparto acordados. |
| B. Viabilidad | Comprobar procesamiento local liviano y una conexión de IA posible. | Registro de resultados y decisión de arquitectura. |
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
| Sistema y supervisión | Controles estructurales, edición y conservación del trabajo ante fallas. | Casos inválidos, errores de API y límites documentados. |

La comparación TF-IDF/embeddings explorada inicialmente queda como ampliación posible. No es obligatorio incluir embeddings si ello contradice el modo offline liviano o el presupuesto. Una comparación sencilla bien realizada sigue siendo valiosa.

## 6. Evaluación proporcionada

Usar material acotado de tres unidades y algunas consultas literales y paráfrasis. Preparar referencias de fragmentos pertinentes antes de comparar métodos. Reservar consultas para evaluación final y evitar ajustar todo sobre ellas.

Revisar una muestra pequeña de preguntas, inicialmente del orden de 20 entre los modos disponibles. Registrar corrección de clave, claridad, tema, respaldo y cambios necesarios. Ambos integrantes revisan y contrastan discrepancias con el material. No presentar esta revisión como validación pedagógica general ni atribuir confianza estadística a una muestra pequeña.

El [diseño del clasificador](CLASIFICADOR_TEMATICO.md) y sus 30 ejemplos piloto están preparados para revisión; no hay un modelo entrenado. Separar su evaluación de la del generador: identificar el tema no demuestra que una pregunta sea correcta. Si los datos no sostienen la tarea, revisar el alcance antes de comprometer resultados.

## 7. Criterios de aceptación del producto

- Con un documento propio se puede construir, revisar, guardar y exportar un examen sin API.
- La copia descargada funciona sin red para el recorrido básico y no solicita recursos externos obligatorios.
- Cambiar la cantidad de respuestas correctas se refleja en instrucciones y validaciones estructurales.
- El examen para estudiantes no revela la clave ni explicaciones docentes.
- Reabrir el archivo de proyecto conserva las preguntas, claves y referencias; las claves API no se exportan.
- Una falla de IA no borra el trabajo ni obliga a contratar un servicio.
- El modo conectado identifica el proveedor y obtiene aprobación antes de enviar contenido.
- Se distingue una referencia existente de una referencia que realmente respalda una afirmación.
- Hay un conjunto pequeño de ejemplos que permite explicar qué se aplicó y qué limitaciones existen.

## 8. Organización de las dos semanas

Fechas orientativas: objetivo interno 9 de noviembre de 2026, margen hasta el 16. La entrega de la propuesta inicial cierra el 30 de octubre a las 00:00, según el aviso recibido. No son fechas oficiales nuevas del trabajo final.

- **Primer tramo:** revisar el piloto de etiquetas con el compañero y probar viabilidad; no instalar componentes ni comprometer gastos sin necesidad.
- **Semana 1:** núcleo offline, datos/etiquetas, referencia de palabras clave y primer clasificador, búsqueda y banco editable.
- **Semana 2:** inferencia del clasificador en navegador, revisión, exportación, intercambio externo, evaluación e instrucciones. API directa solo si se valida y queda tiempo.
- **Margen:** correcciones y devolución; no añadir funciones por defecto.

Reparto propuesto: una persona trabaja en datos/búsqueda/evaluación y otra en editor/exportación/conexión. Ambas participan en diseño, pruebas y defensa. Los nombres, responsabilidades y horas reales todavía deben acordarse.

## 9. Política de recorte

Conservar: material real, recuperación explicable, banco editable, referencias, guardado/exportación y evaluación.

Recortar primero: apariencia avanzada, PDF, conectores de agentes, múltiples proveedores, PWA y plantillas automáticas. El clasificador se valida temprano para no recortarlo silenciosamente al final.

Si la integración externa no funciona bajo las condiciones de costo/acceso, documentarlo y revisar con la cátedra qué alcance demuestra suficientemente la aplicación de IA. No sustituir una función prometida por una simulación sin explicitarlo.

## 10. Siguiente decisión

Recomendación: **web/HTML descargable + base offline + una conexión API opcional**. Confirmar esta dirección con el grupo antes de pasar a la prueba de viabilidad. La consola queda disponible como herramienta para experimentos, no como instalación obligatoria para docentes.

Pendientes: devolución de la cátedra, dedicación del compañero, proveedor viable y validación del clasificador temático propuesto. No se seleccionó proveedor ni se implementaron estas funciones al escribir este plan.

## Integración acordada para planificar

Se adopta la propuesta del compañero como organizador temático, con [protocolo y datos piloto](CLASIFICADOR_TEMATICO.md). Las plantillas automáticas pasan a ampliación: se reemplaza una función prevista por un módulo de aprendizaje supervisado más vinculado a los ejercicios, sin ampliar indiscriminadamente la lista de tareas. No se inicia implementación real en esta actualización.
