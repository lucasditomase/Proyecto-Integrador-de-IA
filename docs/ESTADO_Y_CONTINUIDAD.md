# Estado, decisiones y continuidad de Aula

Actualizado: 26 de octubre de 2026. Presentación vigente **v0.3**. Este archivo permite retomar sin el chat; el detalle del mínimo está en [el alcance común](../ALCANCE_DE_LA_PROPUESTA.md). Es un registro del estado conocido, no evidencia de resultados futuros.

## Punto de partida

Trabajo integrador de Inteligencia Artificial · Ingeniería en Informática · 2026, de dos estudiantes. Se busca demostrar aprendizaje aplicando conocimientos de la cátedra a una necesidad útil. Es más elaborado que una tarea práctica, sin alcance de tesis. No se exige usar todas las técnicas ni entrenar desde cero; se permiten preentrenados.

La idea inicial fue generar exámenes multiple choice personalizables a partir de material docente, por ejemplo configurando respuestas correctas. El alcance actual distingue creación/organización local y asistencia generativa externa. La posibilidad de otras ideas se discutió, pero no se registra como elegido un proyecto diferente. Los casos docentes de microinvernaderos, letras, TSP o mini LLM no son elecciones del grupo.

## Qué está acordado y qué se recomienda

| Estado | Contenido |
|---|---|
| Requisito del estudiante | Presupuesto del grupo cero; no pagar servidores, suscripciones ni API. |
| Requisito del estudiante | Profesores con sistemas y hardware diversos; requisitos mínimos, sin dependencia de Mac, GPU o LLM local. |
| Requisito del estudiante | Modo útil sin clave y offline; una clave propia puede ampliar funciones sin ser obligatoria. |
| Requisito del estudiante | Revisar y explicar resultados; conservar coherencia entre propuesta, demo e implementación. |
| Autorizado en esta fase | Planificación, informe, demo simulada, datos exploratorios y documentación; repos públicos/privado y Pages según su función. |
| Dirección recomendada | HTML/JavaScript descargable y publicable, texto sencillo primero, recuperación liviana, editor y archivos de proyecto. Falta confirmación detallada del grupo y devolución docente. |
| Incorporado a la propuesta | Clasificador temático pequeño del compañero adaptado al banco de preguntas, con tres categorías iniciales, corrección humana y evaluación. |
| Mínimo de asistencia externa propuesto | Exportar un pedido estructurado e importar manualmente preguntas de otro asistente. |
| Condicionado a prueba | API directa con clave del usuario, un proveedor inicial. No hay proveedor elegido ni acceso validado. |
| Ampliaciones | Plantillas automáticas, embeddings, consola para docentes, agentes, PWA, varios proveedores, PDF/OCR y formatos complejos. |

La consola puede servir para experimentos durante el desarrollo. Haber elegido Pages para la demo no obliga a implementar un backend allí: Pages sirve archivos estáticos y no ejecuta inferencia Python. Tampoco se construirán simultáneamente todas las interfaces exploradas.

Un acceso externo puede tener costo o límites aunque el usuario aporte su clave. No hay promesa de gratuidad universal. No reutilizar automáticamente sesiones de aplicaciones ni asumir que una suscripción incluye API; OpenCode/Cline son herramientas distintas de un proveedor de inferencia. Las referencias fechadas y alternativas están en [decisiones](../DECISIONES_Y_OPCIONES.md); verificar condiciones antes de escoger un servicio.

## Qué funciona hoy

La demo de `demo/index.html` está publicada en [Pages](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/) y se puede abrir descargada. Incluye un apunte, seis preguntas con variantes y opciones para configurar, editar, revisar, aprobar/descartar y descargar examen y clave separados. Las etiquetas precargadas pueden corregirse manualmente. No guarda el trabajo al recargar.

No hay procesamiento real de material propio, recuperación TF-IDF, clasificador entrenado, API ni generación nueva. La selección básico/asistido explica recorridos; usa los mismos ejemplos. Previsualizar texto propio no demuestra comprensión ni generación. No hay claves ni envío de contenido en la demo.

Hay informe Markdown/PDF de dos páginas, guion, plan, diseño del clasificador, 30 ejemplos exploratorios, captura, ZIP y manifiesto de hashes. El clasificador propuesto no determina corrección de preguntas, dificultad ni claves. Sus etiquetas piloto fueron redactadas por el asistente y requieren revisión del grupo; no son un test independiente ni métricas de precisión.

## Cronología de decisiones

| Paso | Evolución y motivo |
|---|---|
| Revisión de la materia | Teoría HTML, prácticas y experimentos se sintetizaron en Markdown en el repositorio privado de teoría. |
| Idea inicial | Exámenes con respaldo documental, personalización y revisión docente. Se exploró comparación TF-IDF/embeddings. |
| Alcance de entrega | Se pidió un informe y demo sencilla para el 26/10; se autorizó simular sin IA, manteniendo explícita la diferencia con el producto. |
| Organización | Todo el integrador pasó a este repo público y su demo a Pages; la teoría se publicó en repo privado. |
| Costo/acceso | Se descartó exigir un servidor del grupo o LLM local; se exploraron web, consola, agentes y clave propia. |
| v0.2 | Núcleo offline y asistencia externa opcional; API condicionada. Plantillas simples previstas y modelo propio como ampliación. |
| v0.3 | Se integra la idea del compañero como clasificador temático acotado; las plantillas pasan a ampliación para compensar trabajo. TF-IDF se compara con coincidencia simple; embeddings no son obligatorios. |
| Revisión documental | Se añadieron instrucciones por repo, continuidad y mantenimiento; no cambia el alcance v0.3 ni inicia implementación. |

Las versiones anteriores quedan en Git para explicar cambios, no como compromisos simultáneos. El PDF original del compañero permanece en el repositorio privado; aquí solo se documenta la adaptación conceptual.

## Fechas y pendientes

La propuesta debía estar presentable el **26 de octubre de 2026**. El aviso de la cátedra abre el 23/10 a las 00:00 y cierra el **30/10 a las 00:00**: preparar la subida antes del fin del jueves 29. Pide un archivo por grupo con trabajo seleccionado y contexto para revisión docente. No consta que se haya enviado a la plataforma ni que esté aprobado.

Objetivo interno de desarrollo: dos semanas desde el 26/10, hasta el 9/11; tercera semana solo como margen, hasta el 16/11. No son vencimientos oficiales del trabajo final. Faltan:

- Devolución docente y confirmación detallada del compañero sobre propuesta y dirección técnica.
- Nombres para el informe si se requieren, reparto y horas semanales reales.
- Corpus final, revisión de categorías y etiquetas, ejemplos independientes y partición por grupos antes de ajustar.
- Prueba de recuperación, baseline y clasificador; tiempos/tamaño y concordancia entre Python y navegador.
- Formato de intercambio externo y, si se intenta API directa, proveedor/acceso, condiciones, cuotas y costo cero para la evaluación del grupo.
- Inicio de la fase de implementación real. La autorización actual de documentar no implica entrenar ni contratar nada.

El siguiente paso útil de planificación es revisar el piloto con el compañero y registrar acuerdos; luego iniciar las pruebas de viabilidad cuando se pase a desarrollo. No prometer exactitud sin medirla ni eliminar una función presentada sin explicitar el cambio.

## Dónde vive cada cosa

| Repositorio | Función |
|---|---|
| [Inteligencia-Artificial-2026](https://github.com/lucasditomase/Inteligencia-Artificial-2026) | Privado: HTML, síntesis de la cátedra, referencias y PDF original del compañero. Requiere permisos. |
| [Practicos-de-IA](https://github.com/lucasditomase/Practicos-de-IA) | Trece scripts didácticos; no implementación del integrador. |
| [Inteligencia-Artificial](https://github.com/lucasditomase/Inteligencia-Artificial) | Fork de experimentos, presentaciones y notebooks para fortalecer teoría. |
| Este repositorio | Todo el material propio de Aula: propuesta, demo, planificación y futura implementación. |

El contexto curricular está en [Proyecto integrador en la cátedra](PROYECTO_INTEGRADOR_EN_LA_CATEDRA.md); los métodos del clasificador en [su diseño](../CLASIFICADOR_TEMATICO.md). No duplicar materiales privados ni la base completa de teoría aquí.
