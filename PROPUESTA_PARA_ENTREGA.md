# Aula: asistente para preparar exámenes multiple choice

**Trabajo integrador · Inteligencia Artificial · Ingeniería en Informática · 2026**  
**Propuesta consolidada v0.3 · 26 de octubre de 2026 · Grupo de dos integrantes**

## Problema y objetivo

Preparar un examen requiere seleccionar contenidos, redactar preguntas y revisar opciones y claves. Proponemos una herramienta que ayude al docente a construir un examen multiple choice a partir de material textual propio. El objetivo es obtener preguntas revisables, con referencias al material y aprobación final del profesor.

La herramienta tendrá un núcleo gratuito que funcione sin conexión ni clave API. La asistencia de un modelo generativo será opcional. El proyecto no dependerá de la Mac de los integrantes, de hardware potente ni de un servidor pago.

## Qué proponemos implementar

Una interfaz HTML descargable, también publicable como página web, permitirá cargar TXT/Markdown o pegar texto, buscar contenido pertinente y crear un banco de preguntas. Cada pregunta tendrá cuatro opciones, una o dos respuestas correctas, fuente y un fundamento registrado durante la revisión.

El modo básico incluirá búsqueda, edición manual y un clasificador temático de preguntas, integrando la idea original de nuestro compañero: aprender categorías a partir de frases de ejemplo. Propondrá un tema para preguntas escritas o importadas y el docente podrá corregirlo. El piloto abarcará Representación y vecinos, Datos y evaluación, y Redes y aprendizaje; no clasificará cualquier materia automáticamente. No se promete generación libre offline.

Se podrá editar, aprobar, descartar, guardar e importar un proyecto, y exportar por separado el examen y la clave. Estas funciones no requerirán pagos ni una cuenta externa.

## Asistencia de IA opcional

La herramienta preparará un pedido estructurado con contenido seleccionado para utilizarlo en un asistente externo y permitirá importar preguntas en un formato definido. Este intercambio puede ser manual y no supone que la herramienta proporcione una cuenta o uso gratuito de un servicio externo.

También evaluaremos una conexión directa por API con una clave propia del usuario. Antes de comprometer un proveedor comprobaremos que permita el acceso desde navegador, sus condiciones, cuotas y la calidad de las respuestas. Si resulta viable, integraremos un proveedor inicial; si no, conservaremos la modalidad manual y lo explicaremos a la cátedra. No se promete soporte para cualquier modelo ni gratuidad ilimitada de terceros.

## Recorrido previsto

1. **Material:** preparar el texto, dividirlo en fragmentos y conservar su origen.
2. **Selección:** recuperar contenido pertinente para el tema solicitado.
3. **Preguntas:** redactarlas o importarlas y obtener una sugerencia temática revisable.
4. **Revisión:** comprobar contenido, opciones, claves y fuentes; aceptar, editar o descartar.
5. **Salida:** guardar el proyecto y exportar examen y clave separados.

## Qué contenidos de la materia aplicaremos

- **Representación y calidad de datos:** extracción, segmentación, términos, duplicados y procedencia de la información.
- **Vectores y similitud:** TF-IDF, producto escalar, norma y coseno para ordenar fragmentos respecto de una consulta.
- **NLP y recuperación:** comparar una búsqueda por coincidencia simple con TF-IDF y analizar resultados y limitaciones.
- **Aprendizaje supervisado:** entrenar y evaluar un clasificador pequeño TF-IDF/regresión logística frente a palabras clave, con etiquetas, particiones y matriz de confusión.
- **IA generativa y contexto:** preparar material seleccionado para un modelo preentrenado, comprender RAG y distinguir recuperación, generación e inferencia del entrenamiento.
- **Evaluación y supervisión:** establecer una referencia, analizar errores, verificar restricciones y mantener la decisión final en el docente.

Entrenaremos el clasificador durante el desarrollo y exportaremos sus parámetros para inferencia en el navegador, sin exigir Python al docente. Embeddings, plantillas automáticas y otros conectores quedan como ampliaciones. La prioridad es demostrar conocimientos aplicados y explicar resultados.

## Cómo evaluaremos el resultado

Usaremos material acotado de tres unidades y solicitudes con fragmentos relevantes identificados. Compararemos coincidencia de términos y TF-IDF/coseno sobre las mismas consultas, reservando algunas para prueba final. Observaremos pertinencia de resultados y ejemplos de fallos.

Revisaremos etiquetas de ejemplos antes de entrenar y reservaremos casos por grupos conceptuales para evitar repartir paráfrasis entre entrenamiento y prueba. Informaremos errores por clase, sin prometer precisión antes de medirla. Revisaremos una muestra pequeña de preguntas según claridad, corrección de la clave, correspondencia temática y respaldo documental. También comprobaremos cantidades de opciones/respuestas y que el examen no revele la clave. La revisión de ambos integrantes será una evaluación inicial, no una certificación pedagógica.

## Viabilidad y límites

Dos integrantes trabajarán durante dos semanas como objetivo, con presupuesto del grupo cero. Primero se verificará la arquitectura y se completará el núcleo básico; después, la asistencia externa viable y las pruebas. Una copia descargada incluirá los recursos necesarios para las funciones offline; abrir por primera vez la página publicada requiere internet.

No se incluyen en el mínimo OCR, imágenes, fórmulas, PDF, corrección de alumnos, dificultad pedagógica automática, cuentas ni una plataforma completa. No será obligatorio instalar un modelo de lenguaje local. Cualquier modificación sustancial del alcance se documentará para revisión de la cátedra.

## Qué muestra la demo de hoy

La demo v0.3 muestra material, configuración de modo básico/asistido, revisión, edición, aprobación y exportación. Las etiquetas de tema son precargadas y se pueden corregir; no hay un modelo entrenado. Usa un apunte y preguntas preparados: no genera contenido nuevo, no procesa material propio mediante IA ni solicita claves reales. La selección de modo explica el flujo previsto, pero ambos recorridos usan los mismos ejemplos.

El producto final aún no está implementado.
