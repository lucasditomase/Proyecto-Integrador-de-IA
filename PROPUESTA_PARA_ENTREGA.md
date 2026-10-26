# Aula: asistente para preparar exámenes multiple choice

**Trabajo integrador · Inteligencia Artificial · Ingeniería en Informática · 2026**  
**Propuesta inicial · 26 de octubre de 2026 · Grupo de dos integrantes**

## Problema y contexto

Preparar un examen requiere seleccionar contenidos, redactar preguntas y construir opciones de respuesta claras. Además, el docente debe comprobar que las respuestas sean correctas y que las preguntas correspondan al material enseñado.

Proponemos un asistente que reciba material del profesor y prepare un borrador de examen multiple choice configurable. Cada pregunta incluirá respuestas sugeridas, una explicación y una referencia al contenido utilizado. El docente podrá revisar, editar, aceptar o descartar las preguntas antes de obtener el examen final.

## Qué vamos a hacer

El docente cargará material textual, seleccionará un tema y configurará la cantidad de preguntas. La primera versión tendrá cuatro opciones por pregunta y permitirá elegir una o dos respuestas correctas. Se obtendrán por separado el examen para estudiantes y la clave con fundamentos para el docente.

La herramienta buscará contenido pertinente dentro del material y lo proporcionará como contexto a un modelo de lenguaje preentrenado para generar las preguntas. Este procedimiento corresponde a generación aumentada por recuperación, o RAG. No se entrenará un modelo desde cero.

## Cómo funcionará

1. **Material:** extraer el texto y conservar la identificación del documento y sus secciones.
2. **Representación:** dividir el contenido en fragmentos y representarlos numéricamente.
3. **Recuperación:** comparar el tema solicitado con los fragmentos para seleccionar los pertinentes.
4. **Generación:** utilizar esos fragmentos y la configuración para proponer preguntas con un modelo preentrenado.
5. **Revisión:** mostrar opciones, clave, explicación y fuente para que el docente decida cuáles conservar.
6. **Salida:** exportar las preguntas aprobadas y una clave docente separada.

**Recorrido:** material del profesor → selección de contenido → preguntas configurables → revisión docente → examen y clave.

## Qué contenidos de la materia aplicaremos

- **Representación, vectores y similitud:** utilizar producto escalar, norma y similitud coseno para comparar solicitudes y fragmentos. Se relaciona con las prácticas de vectores, embeddings y vecindad.
- **Calidad de datos:** revisar la extracción, evitar duplicados y conservar la procedencia. Un texto incompleto o mal segmentado puede producir preguntas deficientes.
- **Lenguaje natural:** trabajar con TF-IDF y embeddings para representar el material y recuperar contenido pertinente.
- **IA generativa y RAG:** utilizar un modelo preentrenado con contexto documental y comprender la diferencia entre generación, recuperación y entrenamiento.
- **Evaluación y análisis de errores:** comparar una referencia sencilla con otra alternativa y explicar los casos donde el sistema acierta o falla.
- **Supervisión y límites:** mantener la aprobación del examen en el docente y no presentar una respuesta generada como garantía de corrección.

La programación permitirá llevar estas ideas a un prototipo. El objetivo académico será demostrar que comprendemos las representaciones, la selección de información y la evaluación de una solución de IA útil.

## Cómo comprobaremos que funciona

Usaremos inicialmente material acotado de tres unidades de la materia. Prepararemos pequeñas solicitudes de prueba y señalaremos qué fragmentos contienen información pertinente.

Compararemos dos formas de seleccionar contenido: **TF-IDF con similitud coseno**, como referencia inicial, y **embeddings preentrenados con similitud coseno**. Mantendremos el mismo generador e instrucciones para observar las diferencias. Si la alternativa sencilla resulta suficiente, también será una conclusión válida.

La evaluación tendrá dos partes: comprobar si se recuperan fragmentos pertinentes y revisar una muestra pequeña de preguntas. En esa revisión observaremos corrección de la clave, claridad, correspondencia con el tema y respaldo de la explicación. También verificaremos automáticamente la cantidad de opciones y de respuestas marcadas. El cumplimiento del formato no garantiza la corrección conceptual.

## Alcance y organización

El desarrollo está previsto para dos semanas entre dos integrantes. La primera semana se dedicará a material, representación y búsqueda; la segunda, a generación, revisión y pruebas. Se priorizará un flujo completo y sencillo.

Comenzaremos con HTML o texto y, si el tiempo lo permite, PDF con texto seleccionable. No incluiremos OCR, interpretación de imágenes o fórmulas, corrección de alumnos, cuentas de usuario ni una plataforma educativa completa. Tampoco intentaremos determinar automáticamente la dificultad pedagógica de una pregunta.

## Prototipo para esta presentación

Se acompaña una demo HTML local que permite recorrer carga de material, configuración, revisión, edición, aprobación y exportación de preguntas. Utiliza un apunte y un banco de preguntas preparados de antemano: **no tiene IA conectada ni genera preguntas nuevas**. Su propósito es comunicar cómo se usaría la herramienta y recibir una devolución temprana de la cátedra.

El resultado final previsto es un prototipo funcional con IA, una comparación breve de los métodos y ejemplos que permitan explicar las decisiones, los errores y las limitaciones encontradas.
