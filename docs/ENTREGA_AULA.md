# Aula · Uso, resultados y entrega

Aula prepara exámenes sobre apuntes de texto con búsqueda local, sugerencias temáticas y revisión docente. El HTML incluye la interfaz y el modelo. Abrirlo requiere un navegador actual con JavaScript y permisos normales de lectura y descarga de archivos.

## Etapas de la cursada

La secuencia indicada por el estudiante es rendir el parcial, entregar el trabajo y esperar la corrección. Si la devolución es favorable, la defensa se realiza en el examen final. La prioridad de esta etapa es tener Aula completo y listo para entregar según la consigna del EVA.

Para la entrega están disponibles el HTML descargable, la versión publicada, las instrucciones de uso y los resultados reproducibles. Si la cátedra pide un paquete o el registro académico en JSON, preparar esos archivos según la consigna final.

## Usar Aula

1. Abrí `aula.html`. Pegá material o elegí un TXT o Markdown en UTF‑8 y pulsá **Agregar material**. Cada documento admite 200.000 caracteres y 500 fragmentos. El proyecto admite diez documentos y 200 preguntas.
2. Buscá términos del apunte. Elegí TF-IDF/coseno o coincidencia de términos. Pulsá **Usar en la pregunta** para copiar la referencia al editor.
3. Escribí el enunciado, cuatro opciones diferentes y un fundamento. Marcá una o dos opciones correctas. Podés pedir una sugerencia de tema y editarla. En el banco, revisá el fragmento y aprobá las preguntas que quieras exportar.
4. En el banco, pulsá **Aprobar** en cada pregunta que quieras incluir. Usá **Guardar proyecto** para descargar un archivo editable y **Abrir proyecto** para retomarlo. Guardá antes de cerrar la página. Descargá el examen para alumnos y guardá la clave docente por separado.
5. Si querés usar un asistente externo, marcá entre uno y doce fragmentos, descargá el pedido y compartí el archivo por tu cuenta. Guardá el proyecto si vas a cerrar Aula mientras esperás la respuesta. La importación valida el pedido vigente, las referencias y la estructura de todas las preguntas. Revisá si los fragmentos respaldan la clave antes de aprobarlas.

El JSON de Aula conserva material y claves del docente. El registro académico acumulativo de la cátedra se completa en los formularios de la materia. Confirmar en el EVA la fecha y formato final.

## Ejemplo de intercambio con un asistente externo

Probá con este texto breve: «La similitud coseno compara la orientación de dos vectores». Agregalo como material y buscá «similitud coseno».

1. En el resultado, marcá **Incluir en el pedido**. Abrí **Intercambio con un asistente externo** y pulsá **Descargar pedido**. Se guarda `aula-pedido.json` con el fragmento elegido y el formato que debe seguir la respuesta.
2. Adjuntá ese archivo al asistente que uses. Podés escribir: «Leé el pedido adjunto y devolveme una pregunta siguiendo las instrucciones del archivo. Entregá el resultado como `aula-respuesta.json`».
3. Descargá el archivo de respuesta. Si el asistente responde en el chat, copiá desde la primera llave hasta la última y guardá el texto como `aula-respuesta.json` en un editor de texto plano. El contenido del archivo empieza con `{` y termina con `}`.
4. Volvé al mismo proyecto en Aula y seleccioná **Importar candidatos**. Si cerraste la página, abrí primero el proyecto que guardaste **después** de descargar el pedido. La pregunta validada aparece en el banco como pendiente. Revisá su fuente y la respuesta correcta antes de aprobarla.

Esta es una respuesta de ejemplo para ese texto. `requestId` debe coincidir con el identificador del pedido que descargaste y `sourceId` con el `id` de uno de los fragmentos de ese archivo. `keys: [0]` marca la primera opción como correcta.

```json
{
  "kind": "aula-candidates",
  "version": 1,
  "requestId": "pedido-ejemplo",
  "questions": [
    {
      "text": "¿Qué compara la similitud coseno entre dos vectores?",
      "options": ["Su orientación", "Su cantidad de componentes", "Su suma", "Su promedio"],
      "keys": [0],
      "sourceId": "fragmento-ejemplo",
      "rationale": "El fragmento indica que la similitud coseno compara la orientación."
    }
  ]
}
```

Si Aula indica que la respuesta no corresponde al pedido vigente, reabrí el proyecto guardado con ese pedido o generá un pedido nuevo y pedile al asistente que use los identificadores de ese archivo.

## Resultados observados

| Tarea | Referencia | Método comparado | Casos reservados |
|---|---:|---:|---|
| Recuperación, Precision@3 | Coincidencia de términos 0,306 | TF-IDF/coseno 0,306 | 12 consultas con un fragmento pertinente por consulta. Se sumaron dos casos sin respaldo. |
| Clasificación, macro-F1 | Palabras clave 0,857 | TF-IDF/regresión logística 0,750 | 15 preguntas, cinco por tema, con grupos distintos del piloto. |

La recuperación empató en Precision@3. Como las anotaciones identifican un fragmento pertinente por consulta, el máximo de esa métrica en este corpus es 1/3. La consulta sobre la órbita de un satélite sin términos compartidos produjo una lista vacía. Agregar «vector» produjo un resultado léxicamente relacionado sin respaldo. Por eso se muestra el pasaje y el docente confirma la fuente.

Para clasificación se revisaron conceptualmente las etiquetas de los 30 enunciados piloto y se conservaron sus categorías. La revisión y la redacción de casos fueron asistidas. Falta validación independiente con enunciados reales anotados por docentes. En las 15 preguntas, la referencia acertó 12 y se abstuvo en 3. El modelo acertó 11, se abstuvo en 1 y confundió 3. Por ejemplo, clasificó una pregunta sobre inicializar pesos de una capa como Datos y evaluación. La muestra pequeña y los términos compartidos limitan cualquier generalización. La aplicación permite corregir la etiqueta y restringe la sugerencia a los tres temas del piloto.

Los resultados JSON incluyen predicciones por caso, matriz, puntuaciones o fragmentos recuperados. El modelo usa TF-IDF suavizado con norma L2 y regresión logística multiclase con descenso por gradiente en Python estándar. El vocabulario y el IDF de clasificación se obtienen solo del piloto de entrenamiento. En recuperación se indexan los fragmentos del material que se consulta.

## Reproducir

Desde la raíz del repositorio, con Python 3 y Node.js para desarrollo:

```sh
python3 scripts/entrenar_aula.py
node scripts/evaluar_recuperacion.cjs
python3 scripts/construir_aula.py
node --test tests/aula.test.cjs
python3 scripts/construir_aula.py --check
```

Los datos de evaluación y las salidas están en `datos/`. Las pruebas cubren origen y segmentación, validación de proyectos, intercambio, exportación estudiantil, recuperación y paridad de puntuaciones Python/JS en los casos reservados. El HTML pesa alrededor de 48 kB y sus recursos están incorporados.

## Pruebas de la aplicación

En navegador integrado sobre macOS y localhost se cargó texto propio, se buscó un fragmento, se redactó una pregunta, se obtuvo una sugerencia de tema y se aprobó. Se descargaron el proyecto, el examen, la clave y el pedido. Se inspeccionaron los HTML exportados, se importaron casos válido e inválido y se reabrió el proyecto guardado. También se abrió el HTML directamente como archivo local en Safari 27.3 con Safari MCP. Se probó la búsqueda, sugerencia temática, aprobación, generación de los tres archivos y reapertura del proyecto. El inspector registró cero solicitudes de red durante ese recorrido. La prueba capturó los archivos generados por el navegador y mantuvo la conexión del equipo disponible. Windows y Linux quedan pendientes de verificación.

| Riesgo | Control |
|---|---|
| Aprobar una clave con una fuente que no la respalda | Mostrar texto y posición del fragmento. Exigir fundamento y aprobación explícita. |
| Compartir material sensible con terceros | El recorrido usa procesamiento local. El usuario elige los fragmentos del archivo de pedido y decide si lo comparte. |
| Sugerir un tema incorrecto para otra materia | Mantener edición manual. Registrar errores por clase y revisar el modelo antes de ampliar sus temas. |
| Reemplazar trabajo al abrir un archivo | Validar primero y pedir confirmación si hay un proyecto o un borrador en edición. |

## Defensa en el examen final

Después de recibir la corrección, ajustar la presentación a la devolución. Para la defensa, explicar el problema del docente, mostrar un examen sobre texto propio, contrastar ambos experimentos y terminar con el caso sin respaldo. Justificar la decisión de procesar localmente por costo y revisión docente.
