# Presentación de Aula · versión 0.2

## Alcance que vamos a presentar

Usar [ALCANCE_DE_LA_PROPUESTA.md](ALCANCE_DE_LA_PROPUESTA.md) como referencia común. El informe, PDF, demo y ZIP deben llevar la versión 0.2. La propuesta es una herramienta con base gratuita/offline y asistencia externa opcional, no un generador ilimitado gratuito.

## Archivos

- [Informe editable](PROPUESTA_PARA_ENTREGA.md) y [PDF](output/pdf/PROPUESTA_PARA_ENTREGA.pdf).
- [Demo HTML](demo/index.html), abrible como archivo local.
- [Demo pública](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/).
- [Plan de implementación](PLAN_DEL_PROYECTO.md) y [opciones](DECISIONES_Y_OPCIONES.md).

## Guion de tres minutos

1. **Problema:** ayudar al docente a transformar su material en un examen revisable.
2. **Alcance básico:** texto propio, búsqueda, editor, plantillas simples, guardado e importación de proyectos y exportación. No necesita clave ni un modelo grande local.
3. **Demo:** mostrar el apunte incorporado y pasar a configuración. Elegir modo básico y luego asistido para explicar la diferencia. Ambos usan preguntas preparadas; no hay IA conectada.
4. **Revisión:** mostrar fundamentos, editar una pregunta, aprobarla y descargar el examen y clave separados.
5. **Asistencia externa:** se prepara contenido para utilizar en un asistente e importar preguntas. La conexión directa con una API se incorporará solo después de comprobar un proveedor, sus condiciones y acceso desde navegador.
6. **Cátedra:** representar texto, calcular similitud, comparar búsqueda simple y TF-IDF, explicar contexto/RAG y analizar errores. Embeddings y un modelo propio son ampliaciones, no requisitos.
7. **Viabilidad:** dos personas, dos semanas como objetivo, hardware común y cero gastos del grupo.

## Qué funciona y qué no en la demo

Funciona la selección de variantes de seis preguntas, configuración, visualización de claves, edición, aprobación/descarte y descarga de ejemplos. Cada tema tiene dos preguntas disponibles.

La selección de modo es explicativa, no una ejecución de distintos motores. No ingresar claves reales: la demo no tiene un campo de credenciales. El texto propio solo se previsualiza y hay que restaurar el ejemplo para preparar el borrador simulado.

Todavía no funcionan TF-IDF, propuestas sobre material propio, guardar/importar proyectos, intercambio estructurado ni API. Abrir un archivo propio no demuestra comprensión ni generación real. La captura incluida es de esta demo, no del producto final.

## Frases que no debemos prometer

- “Funciona con cualquier modelo o cualquier documento”.
- “La IA es gratis e ilimitada”.
- “Genera cualquier examen offline”.
- “Las claves son correctas porque lo dice la IA”.
- “Ya tenemos implementadas las funciones propuestas”.

## Preguntas para la devolución

¿Es adecuado el mínimo propuesto para el integrador? ¿La recuperación y evaluación muestran de forma suficiente los conocimientos aplicados? ¿Es aceptable el intercambio manual con un asistente mientras se valida una API directa? ¿Conviene reducir alguna función?

No se registró aún una devolución docente ni se subió material a la entrega de la cátedra. Agregar nombres completos de los integrantes si se requieren.
