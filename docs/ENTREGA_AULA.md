# Aula · Uso, resultados y defensa

Aula prepara exámenes sobre apuntes de texto con búsqueda local, sugerencias temáticas y revisión docente. El HTML incluye la interfaz y el modelo. Abrirlo requiere un navegador actual con JavaScript y permisos normales de lectura y descarga de archivos.

## Usar Aula

1. Abrí `aula.html`. Pegá material o elegí un TXT o Markdown en UTF‑8 y pulsá **Agregar material**. Cada documento admite 200.000 caracteres y 500 fragmentos. El proyecto admite diez documentos y 200 preguntas.
2. Buscá términos del apunte. Elegí TF-IDF/coseno o coincidencia de términos. Pulsá **Usar en la pregunta** para copiar la referencia al editor.
3. Escribí el enunciado, cuatro opciones diferentes, una o dos respuestas correctas y un fundamento. Podés pedir una sugerencia de tema y editarla. En el banco, revisá el fragmento y aprobá las preguntas que quieras exportar.
4. Usá **Guardar proyecto** para descargar un JSON editable. Reabrilo con **Abrir proyecto**. Descargá el examen para alumnos y guardá la clave docente por separado.
5. Si querés usar un asistente externo, marcá entre uno y doce fragmentos, descargá el pedido y compartí el archivo por tu cuenta. Guardá el proyecto si vas a cerrar Aula mientras esperás la respuesta. La importación valida el pedido vigente, las referencias y la estructura de todas las preguntas. Revisá si los fragmentos respaldan la clave antes de aprobarlas.

El JSON de Aula conserva material y claves del docente. El registro académico acumulativo de la cátedra se completa en los formularios de la materia. Confirmar en el EVA la fecha y formato final.

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

## Pruebas y defensa

En navegador integrado sobre macOS y localhost se cargó texto propio, se buscó un fragmento, se redactó una pregunta, se obtuvo una sugerencia de tema y se aprobó. Se descargaron el proyecto, el examen, la clave y el pedido. Se inspeccionaron los HTML exportados, se importaron casos válido e inválido y se reabrió el proyecto guardado. Windows y Linux quedan pendientes de verificación en equipo propio. La preparación de un examen con el archivo abierto directamente puede comprobarse siguiendo los pasos 1 a 4 sin red.

Para defenderlo, empezar por el problema del docente, mostrar un examen sobre texto propio, contrastar ambos experimentos y terminar con el caso sin respaldo. Explicar por qué costo y revisión docente pesaron en la decisión de procesar localmente.

| Riesgo | Control |
|---|---|
| Aprobar una clave con una fuente que no la respalda | Mostrar texto y posición del fragmento. Exigir fundamento y aprobación explícita. |
| Compartir material sensible con terceros | El recorrido usa procesamiento local. El usuario elige los fragmentos del archivo de pedido y decide si lo comparte. |
| Sugerir un tema incorrecto para otra materia | Mantener edición manual. Registrar errores por clase y revisar el modelo antes de ampliar sus temas. |
| Reemplazar trabajo al abrir un archivo | Validar primero y pedir confirmación si hay un proyecto o un borrador en edición. |
