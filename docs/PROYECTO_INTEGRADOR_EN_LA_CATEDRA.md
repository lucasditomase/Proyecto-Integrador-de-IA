# Proyecto integrador

## Sentido y procedencia

El estudiante explicó que las secciones del proyecto en los HTML guían gradualmente la elección del trabajo final mediante pequeñas preguntas. El propósito es implementar una solución que use inteligencia artificial e integre los contenidos de la cátedra.

Es un trabajo propio que se desarrolla a lo largo de la cursada. Los ejercicios del repositorio `Inteligencia-Artificial` permiten fortalecer la teoría experimentando y sirven como antecedentes técnicos. Sus dominios no constituyen una elección del proyecto final.

El recorrido del integrador combina elegir un problema, investigar viabilidad, disponer de datos, construir una referencia, experimentar, evaluar e integrar una solución que pueda explicarse y defenderse.

## Estado confirmado

- El trabajo será de dos integrantes: el estudiante y un amigo.
- La propuesta vigente v0.3 es un asistente de exámenes con base gratuita/offline y asistencia externa opcional. La comparación mínima es búsqueda por coincidencia simple frente a TF-IDF/coseno. Se incorpora un clasificador temático pequeño propuesto; embeddings y modelos de lenguaje locales quedan como ampliaciones. La propuesta se presentará para revisión de la cátedra.
- La fase actual es diagramar, planear, discutir y opinar. La implementación real sigue pendiente; autorizó una demo HTML sin IA para presentar hoy.
- No hay respuestas personales confirmadas del estudiante a las preguntas del integrador. El documento nuevo propone una formulación revisable.
- Hay un alcance y diagrama propuestos; faltan corpus exacto, modelos disponibles, horas semanales. El estudiante confirmó que no hay requisito de entrenar desde cero y se permiten preentrenados.
- No corresponde asumir que el integrador será sobre microinvernaderos, letras, un chatbot o algún otro ejemplo docente.

## Primera formulación en la introducción teórica

La introducción independiente plantea comenzar con una necesidad verificable. Propone explorar dominios como industria, educación, salud, finanzas, comercio, ambiente, agricultura, ciudades o gestión pública.

Su plantilla vincula usuario, problema, datos disponibles, salida esperada, mejora observable y restricciones. La entrega inicial enumera:

1. Nombre tentativo.
2. Dominio y situación problemática.
3. Usuario o destinatario principal.
4. Proceso actual y dificultad observada.
5. Datos potencialmente disponibles.
6. Salida esperada.
7. Tipo de problema de IA tentativo.
8. Métrica de éxito.
9. Riesgo inicial.
10. Dudas de viabilidad.

El trabajo posterior propone revisar la formulación, investigar dos antecedentes y sus fuentes, localizar una fuente de datos y sus condiciones de uso, y explicar el problema sin empezar por la tecnología.

## Preguntas y campos en los ocho HTML iniciales de práctica

Estos campos se verificaron en las páginas individuales disponibles. Son parte del acompañamiento progresivo; su numeración corresponde a la serie inicial de ocho prácticas.

| Etapa | Campos o cuestiones del proyecto |
|---|---|
| Práctica 1: necesidad y representación | Nombre tentativo, dominio, problema verificable, usuario, información disponible, salida, criterio preliminar de éxito y riesgo o duda inicial. |
| Práctica 2: formulación evaluable | Problema, usuario, entrada disponible, salida esperada, tipo de problema, criterio de éxito y límites/dudas de viabilidad. |
| Práctica 3: auditoría de datos | Fuente, variables, faltantes, atípicos, desbalance o representatividad, riesgo de fuga y plan de preparación. |
| Práctica 4: baseline | Objetivo, entradas, baseline elegido, métrica, resultado inicial, costo del error y próximo experimento. |
| Práctica 5: decisión | Clases, puntaje o evidencia, umbral preliminar, costo de FP, costo de FN, métrica principal y justificación. |
| Práctica 6: pertinencia de redes | Entradas, significado de los pesos, activación posible, pertinencia de una red, razones para no usarla y decisión preliminar. |
| Práctica 7: experimento controlado | Hipótesis, parámetro observado, resultado anterior, cambio, resultado posterior, interpretación y próximo paso. |
| Práctica 8: configuración y generalización | Configuración, métrica, comportamiento de entrenamiento y validación, señal de sobreajuste, configuración elegida y síntesis denominada «Entrega 2». |

Las páginas permiten exportar/importar avances como JSON y algunas ofrecen guardado local del navegador. No se encontró un archivo con respuestas del estudiante durante esta revisión. La presencia de un campo llamado «Entrega 2» no permite deducir por sí sola fechas ni ponderaciones oficiales.

## Relación con el cierre de la materia

Las clases sobre arquitectura, MLOps e integración amplían el tipo de decisiones que una solución defendible debe justificar: contratos de entrada/salida, validaciones, versiones, monitoreo, riesgos, supervisión, limitaciones y comportamiento ante fallas.

La clase final propone sostener afirmaciones con evidencia: baseline y comparación, particiones adecuadas, métricas, análisis de errores, reproducibilidad y demostración funcional. Esta conexión orienta el trabajo; no implica que todas las técnicas vistas deban incorporarse al mismo proyecto.

## Forma de acompañar al estudiante

Trabajar las preguntas al ritmo de la cursada y conservar las respuestas anteriores. Una decisión puede revisarse cuando aparezca evidencia nueva; debe quedar claro qué cambió y por qué. Antes de seleccionar tecnología, precisar problema, usuario, información disponible y salida medible.

El estudiante autorizó documentar una elección y diagramarla, y luego construir una demo HTML sin IA para presentar hoy. La [propuesta para entrega](../PROPUESTA_PARA_ENTREGA.md) desarrolla una formulación revisable y el [plan de trabajo](../PLAN_DEL_PROYECTO.md) registra alcance, diagrama, experimento, calendario, riesgos y contingencias. Se creó una demo sin IA para presentar el recorrido; el sistema real sigue pendiente.

La propuesta debe estar presentable el 26 de octubre de 2026. El cierre del espacio de entrega es el 30 de octubre a las 00:00. El objetivo interno de desarrollo es el 9 de noviembre, con margen máximo hasta el 16; estas dos últimas fechas derivan del plazo de dos/tres semanas indicado por el estudiante y no son vencimientos oficiales.

## Prioridad académica confirmada

El estudiante remarcó que la asignatura no es de programación: el objetivo es aplicar conocimientos de la cátedra a una necesidad útil. Evaluar propuestas por su contenido de IA y por la evidencia que permitiría justificar su utilidad, no por la complejidad de desarrollo de la aplicación.

Si se continúa con evaluaciones educativas, explicitar qué tarea de IA se estudia y cómo se mide: representación de documentos/preguntas, recuperación de contenido pertinente, clasificación temática u otra tarea justificada, generación condicionada y análisis de errores. El alcance vigente selecciona recuperación y clasificación temática acotada, con asistencia generativa externa opcional. La correspondencia entre temas de la cátedra y componentes debe responder al problema; no es necesario usar todas las técnicas.

## Aclaración de alcance y presentación del 26 de octubre

El estudiante confirmó que no es una tesis: es un integrador, algo más elaborado que una tarea práctica. No se necesita un estudio extraordinario ni entrenar modelos desde cero. Se permite usar preentrenados. Para hoy solicitó un informe y un prototipo HTML sencillo e interactivo, aunque todavía no use IA. Se prepararon ambos; la demo está identificada como simulación y utiliza un banco de preguntas de ejemplo. El plan se redujo a un flujo útil y pruebas pequeñas. Consultar la propuesta y el plan en la raíz de este repositorio. La demo se publica en GitHub Pages. No se subió nada a la plataforma de entrega de la cátedra.

## Consolidación posterior de requisitos

Se confirmó presupuesto cero, uso en equipos comunes y ausencia de dependencia de la Mac del estudiante. Se discutieron web, consola, modelos pequeños, claves propias y un modo básico útil offline. La recomendación actual, aún para decidir con el grupo, es web/HTML descargable con núcleo offline y API opcional. No se implementaron esas funciones. Consultar [opciones y requisitos](../DECISIONES_Y_OPCIONES.md) y [plan consolidado](../PLAN_DEL_PROYECTO.md). El informe y PDF se actualizaron a v0.3, junto con la demo y el paquete. Consultar [el alcance común](../ALCANCE_DE_LA_PROPUESTA.md) para distinguir mínimo, opciones y estado real.

## Coherencia de presentación v0.3

El [alcance común](../ALCANCE_DE_LA_PROPUESTA.md) define las funciones propuestas para el mínimo y las dependencias pendientes. El informe, PDF, demo, guion y paquete se mantienen alineados. La demo sigue siendo una simulación; no implica que se haya implementado el producto final.

## Clasificador temático propuesto

Se integra la idea del compañero de clasificar frases como organizador temático de preguntas. El [diseño](../CLASIFICADOR_TEMATICO.md) incluye tres categorías iniciales y 30 ejemplos exploratorios con etiquetas pendientes de revisión. Todavía no hay modelo entrenado. Para mantener el alcance, las plantillas automáticas se postergan; embeddings y conectores adicionales siguen siendo ampliaciones.
