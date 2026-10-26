# Alcance común de la propuesta

**Versión de presentación: 0.2 · 26 de octubre de 2026.**

Este es el alcance de referencia del informe, la demo, el plan y el paquete de presentación. Una alternativa explorada en el documento de opciones no es automáticamente una función comprometida.

## Objetivo

Ayudar al docente a construir un examen multiple choice revisable a partir de material textual propio, con un núcleo gratuito y offline y asistencia externa de IA opcional.

## Mínimo que proponemos implementar

- Interfaz HTML descargable, usable en navegadores de escritorio comunes, sin depender de macOS, GPU o un modelo de lenguaje local.
- Entrada inicial de TXT/Markdown o texto pegado; preparación y segmentación con procedencia.
- Búsqueda y selección de fragmentos mediante TF-IDF y similitud coseno, comparadas con coincidencia simple de términos.
- Editor y banco de preguntas: cuatro opciones, una o dos respuestas correctas, fuente y fundamento registrado por el docente.
- Sugerencias extractivas sencillas mediante reglas/plantillas, revisables; no generación libre offline.
- Edición, aprobación/descarte, guardado/importación del proyecto y exportación del examen y clave por separado.
- Preparación de un pedido estructurado con fragmentos seleccionados y posibilidad de importar preguntas en un formato documentado desde un asistente externo. Es un intercambio manual, no una conexión automática ni un servicio gratuito incluido.
- Una evaluación pequeña que muestre los métodos aplicados, resultados y errores.

La generación avanzada no será necesaria para usar el núcleo. Que el programa funcione sin red no significa que pueda generar cualquier pregunta sin un modelo.

## Integración opcional que requiere una prueba previa

Conexión directa con un proveedor de IA mediante clave del usuario. Antes de comprometer un proveedor deben comprobarse autenticación, acceso desde navegador, condiciones de uso, cuota/costo y calidad de las respuestas. No prometer compatibilidad universal, acceso gratuito ilimitado ni un servidor financiado por el grupo.

Si la conexión directa resulta viable, se integrará un único proveedor inicial. Si no, se mantiene el intercambio manual y se explicará esa modalidad a la cátedra; no se presentará la conexión como implementada. Cualquier cambio al mínimo debe registrarse y revisarse, no hacerse silenciosamente al final.

## Ampliaciones que no forman parte del mínimo

Embeddings, clasificador propio, consola para docentes, conectores con OpenCode/Cline, PWA, varios proveedores, PDF, OCR, imágenes y fórmulas. No se descartan para siempre: no se prometen para la primera versión.

## Qué funciona hoy

La demo utiliza un apunte incorporado y seis preguntas preparadas con variantes. Permite configurar, editar, aprobar, descartar y descargar ejemplos. La selección de modo únicamente explica el recorrido previsto: no cambia el origen de las preguntas.

Todavía no implementa procesamiento real de documentos propios, TF-IDF, plantillas sobre texto propio, guardado/importación de proyectos, intercambio estructurado ni API de IA. Hoy se presenta una propuesta y una demostración de interacción, no el producto final.

## Presupuesto y plazo

Dos integrantes, objetivo de dos semanas, presupuesto del grupo cero. El modo básico no exige clave, tarjeta ni pagos. El acceso externo que un usuario decida usar tiene sus propias condiciones y costos; no lo aporta la aplicación.

## Criterio para considerar cumplido el trabajo

En la versión final, una persona debe poder terminar un examen nuevo con su propio texto sin API, guardar y retomar el proyecto y exportar un examen sin revelar la clave. Debe poder explicar la selección de fragmentos y sus errores. La modalidad avanzada se documentará según la conexión efectivamente verificada, sin atribuir funciones a una simulación.
