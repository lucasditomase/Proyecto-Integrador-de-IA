# Aula
## Asistente para preparar exámenes multiple choice

@institution Universidad Católica Argentina (UCA)
@course Ingeniería Informática · Inteligencia Artificial
@term Trabajo integrador · Segundo semestre de 2026
@authors Lucas Di Tomase y Pablo Margewka

### Resumen

Aula es una aplicación web para preparar evaluaciones a partir de material docente. Permite localizar pasajes en apuntes, redactar preguntas con respaldo, revisarlas y exportar un examen y su clave por separado. Su núcleo funciona en el navegador con un archivo HTML autocontenido, sin cuentas, claves, instalaciones ni gastos obligatorios. Se evaluaron dos formas de buscar fragmentos y dos formas de clasificar preguntas por tema.

### 1. Problema y alcance

Al preparar un examen, un docente necesita localizar qué parte del material respalda cada pregunta y revisar las respuestas antes de compartirlo. Aula conserva esa referencia junto al enunciado y su fundamento. El profesor decide qué preguntas aprobar. Puede mezclar preguntas con una y dos respuestas correctas entre cuatro opciones y elegir la cantidad final al aprobarlas.

La herramienta acepta texto pegado, TXT y Markdown. Está pensada para profesores que usan un navegador habitual y quieren conservar el control sobre sus materiales. La revisión del producto se concentra en un flujo reproducible, desde un apunte propio hasta los archivos para el estudiante y para el docente.

### Material de entrega

| Recurso | Contenido |
| --- | --- |
| [Abrir Aula](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/aula.html) | Aplicación final. El botón «Descargar Aula» obtiene el HTML para abrirlo localmente. |
| [Repositorio del proyecto](https://github.com/lucasditomase/Proyecto-Integrador-de-IA) | Código fuente, HTML descargable, pruebas, datos y documentación. |
| [Guía de uso y reproducción](https://github.com/lucasditomase/Proyecto-Integrador-de-IA/blob/main/docs/ENTREGA_AULA.md) | Primer recorrido docente, ejemplo de intercambio externo y comandos del experimento. |
| [Datos y resultados](https://github.com/lucasditomase/Proyecto-Integrador-de-IA/tree/main/datos) | Corpus de ejemplo, modelo exportado, métricas y predicciones por caso. |
| [Demo de la propuesta v0.3](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/) | Prototipo inicial con preguntas preparadas, conservado como antecedente. |

<!-- pagebreak -->

## Fundamentos y diseño

### 2. Recuperación de información

Aula segmenta el texto y conserva el documento y la línea de origen de cada fragmento. La consulta y los fragmentos se tokenizan con el mismo criterio. El método de referencia cuenta los términos distintos que coinciden. El segundo método pondera cada término mediante TF-IDF. La frecuencia del término aumenta su peso dentro del fragmento, mientras que la frecuencia documental lo reduce si aparece en muchos fragmentos.

La similitud coseno se obtiene al dividir el producto escalar entre el producto de las normas. Con vectores normalizados, basta el producto escalar. Aula ordena los resultados con puntaje positivo y muestra cada pasaje junto a su referencia. Si la consulta carece de términos compartidos con el índice, informa que no encontró coincidencias. Un puntaje alto indica cercanía en la representación de términos y requiere que el docente compruebe el respaldo.

### 3. Clasificación temática supervisada

Los enunciados etiquetados del piloto alimentan una regresión logística multiclase. Se ajustan el vocabulario y los pesos IDF con los datos de entrenamiento. El entrenamiento compara las puntuaciones de las tres clases mediante softmax y ajusta los pesos por descenso por gradiente con regularización L2. La referencia cuenta coincidencias con listas de palabras clave. En la aplicación, los parámetros exportados permiten sugerir el tema desde JavaScript. Los temas del piloto son **Representación y vecinos**, **Datos y evaluación** y **Redes y aprendizaje**.

El modelo sugiere una etiqueta al recibir un enunciado ya escrito. Ante un enunciado sin términos conocidos se abstiene. El profesor puede corregir la sugerencia o asignar su propio tema. La etiqueta describe el contenido temático. La corrección pedagógica, la clave y la calidad del respaldo se revisan por separado.

### 4. Arquitectura y revisión docente

| Componente | Función y decisión de diseño |
| --- | --- |
| Navegador | Fragmenta, indexa, busca y clasifica localmente. El HTML incorpora el modelo y los recursos de la interfaz. |
| Proyecto guardado | Un archivo JSON versionado conserva material, preguntas, fuentes, claves y estados de revisión. Aula valida el archivo antes de abrirlo. |
| Exportación | Las preguntas aprobadas se convierten en un HTML para estudiantes y otro con la clave docente. El examen excluye las marcas de respuesta y los fundamentos. |
| Asistencia externa opcional | El docente exporta un pedido con los fragmentos elegidos y puede importar la respuesta de un asistente. Aula valida estructura y referencias. El envío lo decide el docente. |

Esta arquitectura aplica representación de texto, similitud vectorial, aprendizaje supervisado, comparación con una referencia y revisión humana. La asistencia externa reutiliza el contexto recuperado mediante intercambio manual. El entrenamiento ocurre durante el desarrollo y la inferencia se ejecuta en el navegador.

<!-- pagebreak -->

## Evaluación y resultados

### 5. Diseño experimental

**Recuperación.** Se usaron tres apuntes breves redactados para el ejercicio. Se anotó un fragmento pertinente por cada una de las doce consultas evaluadas, que incluyen formulaciones literales y paráfrasis. Los dos métodos recibieron el mismo corpus y las mismas consultas. Se midió Precision@3. Como se identificó un único fragmento pertinente por consulta, el máximo posible en este conjunto es 1/3. Se agregaron dos casos sin respaldo para observar las salidas fuera del dominio.

**Clasificación.** Se entrenó con 30 enunciados del piloto y se evaluó con 15 preguntas reservadas, cinco por categoría. Los grupos conceptuales del conjunto reservado son distintos de los del entrenamiento. Se compararon los métodos con macro-F1 y una matriz de confusión, registrando también abstenciones. Los casos son de elaboración propia con asistencia de IA y el conjunto es exploratorio.

| Tarea | Método de referencia | Método evaluado |
| --- | --- | --- |
| Recuperación · Precision@3 | Coincidencia de términos · 0,306 | TF-IDF y coseno · 0,306 |
| Clasificación · macro-F1 | Palabras clave · 0,857 | TF-IDF y regresión logística · 0,750 |

### 6. Interpretación y errores

Ambos buscadores obtuvieron el mismo promedio. La consulta sobre la órbita de un satélite quedó sin resultados cuando carecía de términos compartidos. Al agregar «vector», ambos devolvieron un fragmento sobre vectores que no respondía la consulta. Este caso muestra por qué Aula expone el pasaje y deja la decisión de respaldo en manos del profesor.

El método por palabras clave acertó 12 preguntas y se abstuvo en 3. La regresión logística acertó 11, se abstuvo en 1 y confundió 3. Por ejemplo, etiquetó como Datos y evaluación una pregunta sobre inicializar los pesos de una capa. En esta muestra, las reglas simples dieron mejor macro-F1. La regresión logística se mantuvo como sugerencia corregible y permite demostrar un ciclo completo de entrenamiento, exportación e inferencia. Haría falta una colección de preguntas reales, anotadas de forma independiente, para investigar generalización y utilidad docente.

### 7. Pruebas funcionales y reproducibilidad

Las seis pruebas automatizadas cubren segmentación, validación de proyectos, importación de candidatos, separación de examen y clave, búsqueda y concordancia entre Python y JavaScript. En el navegador se probó el flujo con texto propio y la reapertura de un proyecto. También se verificó el rechazo de una importación con referencia inválida y la conservación del banco abierto.

Se abrió el HTML como archivo local en Safari 27.3 sobre macOS. Se probó desde la búsqueda hasta la generación del examen, la clave y el proyecto editable. El inspector registró cero solicitudes de red con la conexión del equipo disponible. Quedan por probar directamente el recorrido en Windows y Linux y la apertura con la red del equipo desactivada. Los scripts y datos del repositorio permiten repetir ambos experimentos.

<!-- pagebreak -->

## Requisitos, límites y conclusión

### 8. Correspondencia con los objetivos de la materia

| Objetivo | Qué demuestra Aula |
| --- | --- |
| Representar un problema con datos | Convierte material en fragmentos con procedencia y representa fragmentos o preguntas como vectores de términos. |
| Justificar y comparar métodos | Contrasta coincidencia de términos con TF-IDF/coseno y palabras clave con regresión logística. Usa los mismos casos para cada par de métodos. |
| Evitar fuga y medir errores | Separa los grupos conceptuales y ajusta el vocabulario del clasificador con entrenamiento. Registra métricas, errores y abstenciones en datos reproducibles. |
| Integrar y verificar una solución | Valida entradas, guarda el examen editable, verifica la inferencia entre Python y JavaScript y separa la clave del examen. |
| Considerar riesgos, costo y supervisión | Procesa localmente. El docente verifica fuentes y claves, aprueba preguntas y controla qué fragmentos comparte al usar asistencia externa. |

### 9. Uso previsto y límites

El docente puede crear un examen completo sin conexión mediante redacción y revisión manual. Puede utilizar la web o descargar un HTML de aproximadamente 48 kB. El núcleo carece de pagos obligatorios y no requiere Python, una GPU ni una cuenta. Se probó directamente en Safari sobre macOS. La compatibilidad esperada abarca navegadores actuales con JavaScript y permiso para leer y descargar archivos.

El clasificador local organiza preguntas en tres temas iniciales. La generación automática requiere un asistente externo, cuyo uso y posibles costos son independientes de Aula. La aplicación intercambia archivos de forma manual. Acepta texto sencillo y excluye importación directa de PDF y reconocimiento de imágenes en esta versión. El guardado es manual y el archivo editable incluye la clave docente.

### 10. Conclusión

Aula integra recuperación de información, clasificación supervisada y revisión humana en una herramienta que produce un examen utilizable. Los experimentos muestran que, en la muestra de trabajo, TF-IDF no elevó Precision@3 y la referencia de palabras clave obtuvo mejor macro-F1. La entrega conserva los resultados para poder replicarlos y analizar cuándo aporta valor cada técnica. El siguiente paso técnico es evaluar con más material y docentes, medir el esfuerzo de revisión y completar las pruebas de portabilidad.

### Referencias del trabajo

El diseño se contrastó con los contenidos y las consignas de las prácticas de representación y evaluación, NLP y recuperación, riesgos, integración y defensa. La matriz del repositorio identifica las prácticas pertinentes y separa lo comprobado de los puntos que requieren evidencia adicional. [Verificación con las consignas de la cátedra](https://github.com/lucasditomase/Proyecto-Integrador-de-IA/blob/main/docs/VERIFICACION_PREVIA_A_IMPLEMENTAR.md)

La implementación, los resultados y la forma de repetir las pruebas se conservan junto con la aplicación. [Repositorio de Aula](https://github.com/lucasditomase/Proyecto-Integrador-de-IA)
