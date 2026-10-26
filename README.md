# Aula · Proyecto Integrador de IA

Asistente para preparar exámenes multiple choice a partir de material docente. Trabajo integrador grupal de **Inteligencia Artificial · Ingeniería en Informática · 2026**.

## Demo pública

**[Abrir la demo en GitHub Pages](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/)**

La demo actual no tiene IA conectada: utiliza un apunte y un banco de preguntas preparados para mostrar el recorrido propuesto. Permite configurar preguntas, mostrar la clave y su fundamento, editar, aprobar, descartar y descargar un examen con su clave separada.

Los textos propios pueden previsualizarse, pero no se interpretan ni generan preguntas nuevas. Para simular el examen se utiliza el apunte incorporado. No se envían archivos a un servidor ni se guardan cambios después de recargar.

## Material del proyecto

- [Alcance común de presentación v0.3](ALCANCE_DE_LA_PROPUESTA.md).
- [Propuesta consolidada v0.3](PROPUESTA_PARA_ENTREGA.md).
- [Informe PDF de dos páginas](output/pdf/PROPUESTA_PARA_ENTREGA.pdf).
- [Clasificador temático: integración de la propuesta del compañero](CLASIFICADOR_TEMATICO.md).
- [Datos exploratorios para revisar etiquetas](datos/piloto_clasificacion.json).
- [Requisitos, opciones y decisiones](DECISIONES_Y_OPCIONES.md).
- [Plan consolidado, alcance y etapas](PLAN_DEL_PROYECTO.md).
- [Guía para presentar la idea](GUIA_PARA_PRESENTAR.md).
- [Contexto del integrador en la cátedra](docs/PROYECTO_INTEGRADOR_EN_LA_CATEDRA.md).
- [Paquete de presentación descargable](AULA_PRESENTACION_HOY.zip).
- [Código de la demo](demo/index.html).

## Uso local

Abrir `demo/index.html` en un navegador. Es un archivo independiente: no requiere instalación, servidor ni conexión a internet.

## Dirección propuesta

Se recomienda una herramienta web/HTML descargable con dos modos: una base gratuita y offline para trabajar con material propio, y generación opcional mediante una clave API del usuario. Debe funcionar en equipos comunes y no depender de la Mac del grupo ni de un modelo de lenguaje local. Presupuesto del grupo: cero.

La base prevista incluye preparación del texto, recuperación liviana, edición, clasificador temático propuesto y guardado/exportación. La asistencia externa contempla intercambio manual de solicitudes/preguntas y una API directa solo si se valida un proveedor. El clasificador incorpora la idea del compañero y requiere validar datos/modelo. Consola, embeddings y plantillas automáticas quedan como ampliaciones.

El informe, PDF, demo y paquete de presentación corresponden a la versión 0.3 y comparten [el alcance de referencia](ALCANCE_DE_LA_PROPUESTA.md). Las opciones exploratorias se distinguen de las funciones comprometidas. La conexión API requiere una prueba previa; el intercambio manual con un asistente no se presenta como una conexión automática.

La demo de presentación sigue usando preguntas preparadas. El procesamiento de material propio, el clasificador, el modo básico real y la conexión a IA todavía no se implementaron. No se eligió un proveedor definitivo.

## Publicación con GitHub Pages

El workflow [pages.yml](.github/workflows/pages.yml) publica únicamente `demo/` al actualizar `main`. Los documentos del integrador se consultan en el repositorio. La publicación se realiza con GitHub Actions y puede ejecutarse manualmente desde la pestaña Actions.

## Regenerar el informe (opcional)

El PDF se genera a partir de `PROPUESTA_PARA_ENTREGA.md` mediante `scripts/generar_informe.py`. Para regenerarlo en un entorno Python con las dependencias de `scripts/requirements-informe.txt`:

```bash
python scripts/generar_informe.py
```

Los archivos temporales de renderizado y los entornos locales se excluyen de Git.

## Mantener coherencia entre propuesta, demo y entrega

[ALCANCE_DE_LA_PROPUESTA.md](ALCANCE_DE_LA_PROPUESTA.md) distingue funciones mínimas, ampliaciones y lo que funciona hoy. Antes de presentar o cambiar el alcance, revisar informe, plan, demo y guion juntos. No atribuir una función prevista al prototipo actual.

Después de modificar el informe, regenerar PDF y paquete:

```bash
python scripts/generar_informe.py
python scripts/preparar_presentacion.py
```

Comprobar visualmente el PDF y la demo antes de empaquetar, y subir los cambios a GitHub para actualizar la demo pública. [VERSION_PRESENTACION.json](VERSION_PRESENTACION.json) registra versión y hashes de los archivos incluidos en el ZIP; no reemplaza la revisión de contenido.
