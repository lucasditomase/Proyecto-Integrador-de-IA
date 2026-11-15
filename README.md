# Aula · Proyecto Integrador de IA

Asistente para preparar exámenes multiple choice a partir de material docente. Trabajo integrador grupal de **Inteligencia Artificial · Ingeniería en Informática · 2026**.

## Empezá a usar Aula

**[Abrir la aplicación final](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/aula.html)**. Para usarla sin conexión, pulsá **Descargar Aula** y abrí el archivo `aula.html` con el navegador. Para preparar un examen solo necesitás ese archivo o el enlace.

1. Pegá tu apunte o elegí un archivo TXT o Markdown. Pulsá **Agregar material**.
2. Buscá un término del apunte y pulsá **Usar en la pregunta** en el fragmento que respalda lo que querés preguntar.
3. Redactá la pregunta con cuatro opciones, marcá una o dos correctas y escribí un fundamento. Pulsá **Guardar pregunta** y después **Aprobar** en el banco.
4. Usá **Guardar proyecto** para descargar el trabajo editable y **Abrir proyecto** para retomarlo. Bajá el examen y la clave por separado con **Descargar examen** y **Descargar clave**.

El [manual de uso](docs/ENTREGA_AULA.md#usar-aula) incluye un [ejemplo de intercambio con un asistente externo](docs/ENTREGA_AULA.md#ejemplo-de-intercambio-con-un-asistente-externo). El [apartado de reproducción](docs/ENTREGA_AULA.md#reproducir) reúne los comandos para repetir los experimentos.

## Documentación académica y de mantenimiento

Consultá [estado y continuidad](docs/ESTADO_Y_CONTINUIDAD.md), [mantenimiento](docs/MANTENIMIENTO.md) e [instrucciones para agentes](AGENTS.md). La revisión de costo y compatibilidad documenta las decisiones de diseño previas a implementar. [Revisión académica y de viabilidad](docs/REVISION_ACADEMICA_Y_VIABILIDAD.md)

La verificación previa relaciona el alcance con las consignas de los 22 laboratorios. [Verificación previa a implementar](docs/VERIFICACION_PREVIA_A_IMPLEMENTAR.md)

## Demo pública de presentación v0.3

**[Abrir el prototipo de la propuesta en GitHub Pages](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/)**

El prototipo de la propuesta utiliza un apunte y un banco de preguntas preparados para mostrar el recorrido propuesto. Permite configurar preguntas, mostrar la clave y su fundamento, editar, aprobar, descartar y descargar un examen con su clave separada.

Los textos propios pueden previsualizarse, pero no se interpretan ni generan preguntas nuevas. Para simular el examen se utiliza el apunte incorporado. No se envían archivos a un servidor ni se guardan cambios después de recargar.

## Material del proyecto

- [Informe final de entrega](output/pdf/INFORME_FINAL_AULA.pdf) y [fuente editable](docs/INFORME_FINAL_AULA.md).
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

Abrí `demo/aula.html` en un navegador para trabajar offline. Para consultar el prototipo de la propuesta, abrí `demo/index.html`.

## Decisiones de la propuesta v0.3

Se recomienda una herramienta web/HTML descargable con dos modos: una base gratuita y offline para trabajar con material propio, y generación opcional mediante una clave API del usuario. Debe funcionar en equipos comunes y no depender de la Mac del grupo ni de un modelo de lenguaje local. Presupuesto del grupo: cero.

La base prevista incluye preparación del texto, recuperación liviana, edición, clasificador temático propuesto y guardado/exportación. La asistencia externa contempla intercambio manual de solicitudes/preguntas y una API directa solo si se valida un proveedor. El clasificador incorpora la idea del compañero y requiere validar datos/modelo. Consola, embeddings y plantillas automáticas quedan como ampliaciones.

El informe, PDF, demo y paquete de presentación corresponden a la versión 0.3 y comparten [el alcance de referencia](ALCANCE_DE_LA_PROPUESTA.md). Las opciones exploratorias se distinguen de las funciones comprometidas. La conexión API requiere una prueba previa; el intercambio manual con un asistente no se presenta como una conexión automática.

La aplicación incluye material propio, búsqueda y clasificación locales, editor e intercambio manual. El acceso directo a un proveedor de IA queda fuera de esta entrega.

## Publicación con GitHub Pages

El workflow [pages.yml](.github/workflows/pages.yml) publica únicamente `demo/` al actualizar `main` con cambios en `demo/**` o en el propio workflow. Los cambios solo documentales no disparan ese despliegue. Los documentos del integrador se consultan en el repositorio. La publicación se realiza con GitHub Actions y puede ejecutarse manualmente desde la pestaña Actions.

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
