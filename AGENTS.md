# Trabajar en Aula con un asistente de IA

Aula permite que un docente prepare exámenes multiple choice sobre sus apuntes. El navegador divide los apuntes en fragmentos, busca fuentes, sugiere un tema por pregunta y permite revisar, guardar y exportar el trabajo. El producto se distribuye como HTML autocontenido. Abrir el archivo requiere un navegador con JavaScript. Python y Node se usan para desarrollar y reproducir el trabajo.

## Orientación inicial

- [README](README.md) para abrir la aplicación y recorrer el uso básico.
- [Guía de Aula](docs/ENTREGA_AULA.md) para uso, intercambio con asistentes, pruebas y resultados.
- [Verificación con la cátedra](docs/VERIFICACION_PREVIA_A_IMPLEMENTAR.md) para saber de dónde salen los requisitos y qué evidencia los respalda.
- [Plan original](PLAN_DEL_PROYECTO.md), [demo de propuesta](demo/index.html) y [alcance v0.3](ALCANCE_DE_LA_PROPUESTA.md) como antecedentes. El producto actual está en [aula.html](demo/aula.html).

## Dónde cambiar cada cosa

| Si querés cambiar… | Empezá aquí |
| --- | --- |
| Textos, formularios, etiquetas accesibles o estructura de la pantalla | [app/index.html](app/index.html) |
| Colores, espaciado y distribución en pantallas chicas | [app/styles.css](app/styles.css) |
| Botones, edición, estado visible, búsqueda en pantalla y descargas | [app/ui.js](app/ui.js) |
| Segmentación, búsqueda, predicción, contratos de archivos y contenido de las exportaciones | [app/core.cjs](app/core.cjs) |
| Entrenamiento, palabras clave y métricas de clasificación | [scripts/entrenar_aula.py](scripts/entrenar_aula.py) y [datos/](datos/) |
| Comparación de buscadores y casos de prueba | [scripts/evaluar_recuperacion.cjs](scripts/evaluar_recuperacion.cjs), [datos/](datos/) y [tests/aula.test.cjs](tests/aula.test.cjs) |
| HTML descargable y publicación | [scripts/construir_aula.py](scripts/construir_aula.py) y [workflow de Pages](.github/workflows/pages.yml) |
| Informe final de entrega | [Fuente Markdown](docs/INFORME_FINAL_AULA.md) y [generador de PDF](scripts/generar_informe_final.py) |
| Proceso documental y artefactos derivados | [docs/MANTENIMIENTO.md](docs/MANTENIMIENTO.md) |

El archivo `demo/aula.html` se genera a partir de las fuentes de `app/` y `datos/modelo_aula.json`. Editá las fuentes, generá el HTML y revisá el diff. El workflow de Pages sirve solo la carpeta `demo/`.

## Seguir el recorrido de los datos

1. `documentFrom` valida el texto. `fragments` construye pasajes con IDs, nombre de la fuente y línea. `indexFor` prepara el índice. `search` devuelve coincidencias para que el docente elija respaldo.
2. La interfaz mantiene proyectos en memoria. `question` valida el enunciado, sus cuatro opciones, una o dos correctas y su fuente. El clasificador propone una etiqueta y el docente decide si la usa.
3. `project` valida el JSON completo antes de abrirlo. El docente guarda una copia descargable para retomar el trabajo. `examHtml` exporta preguntas aprobadas. La clave docente contiene las marcas y fundamentos. La exportación del alumno omite esos datos, también en su código fuente.
4. El pedido externo guarda referencias a los fragmentos elegidos. `candidates` comprueba el identificador del pedido y valida todo el lote antes de agregar preguntas pendientes. La aplicación valida el formato y la existencia de la referencia. El docente verifica si el pasaje respalda la clave.

## Verificar un cambio

Corré los comandos desde la raíz del repositorio:

```sh
# Después de editar app/ o cambiar el modelo
python3 scripts/construir_aula.py
python3 scripts/construir_aula.py --check
node --test tests/aula.test.cjs

# Si cambian el entrenamiento o la comparación de métodos
python3 scripts/entrenar_aula.py
node scripts/evaluar_recuperacion.cjs
python3 scripts/construir_aula.py
```

- Probar en el navegador el flujo afectado desde `demo/aula.html`. Para un cambio de archivos o exportación, abrir un proyecto realista, guardar, reabrir y verificar ambos HTML. Una importación inválida debe conservar el trabajo abierto.
- Conservar lecturas de proyectos v1. Si cambia el formato, especificar su versión y tratar explícitamente los archivos existentes.
- Para clasificación, mantener separados los grupos de entrenamiento y prueba y calcular vocabulario e IDF solo con entrenamiento. Si cambia la transformación, comprobar concordancia entre Python y JavaScript. Registrar resultados observados, errores y limitaciones.
- El núcleo funciona sin API, conexiones externas, instalaciones ni gastos obligatorios. Mantener los recursos dentro del HTML. Aula trata el material importado como datos. Conservar revisión docente, validación y separación entre examen y clave.
- El repo es público. Usar ejemplos propios o autorizados. Los originales docentes y la propuesta inicial del compañero se conservan fuera de este repo. Excluir apuntes privados, claves, datos de alumnos y archivos temporales.
- Al publicar un cambio de aplicación, verificar Actions y la versión servida en `/aula.html`. Si el cambio incluye documentación, distinguir en ella el estado del producto de los antecedentes de la propuesta.

Para tareas nuevas, usar el pedido actual del usuario y las fuentes del repositorio. Las pruebas, métricas y despliegues se describen según lo que se haya verificado.
