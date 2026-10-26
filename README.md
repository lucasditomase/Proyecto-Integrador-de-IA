# Aula · Proyecto Integrador de IA

Asistente para preparar exámenes multiple choice a partir de material docente. Trabajo integrador grupal de **Inteligencia Artificial · Ingeniería en Informática · 2026**.

## Demo pública

**[Abrir la demo en GitHub Pages](https://lucasditomase.github.io/Proyecto-Integrador-de-IA/)**

La demo actual no tiene IA conectada: utiliza un apunte y un banco de preguntas preparados para mostrar el recorrido propuesto. Permite configurar preguntas, mostrar la clave y su fundamento, editar, aprobar, descartar y descargar un examen con su clave separada.

Los textos propios pueden previsualizarse, pero no se interpretan ni generan preguntas nuevas. Para simular el examen se utiliza el apunte incorporado. No se envían archivos a un servidor ni se guardan cambios después de recargar.

## Material del proyecto

- [Propuesta para presentar](PROPUESTA_PARA_ENTREGA.md).
- [Informe PDF de dos páginas](output/pdf/PROPUESTA_PARA_ENTREGA.pdf).
- [Plan, alcance y diagrama](PLAN_DEL_PROYECTO.md).
- [Guía para presentar la idea](GUIA_PARA_PRESENTAR.md).
- [Contexto del integrador en la cátedra](docs/PROYECTO_INTEGRADOR_EN_LA_CATEDRA.md).
- [Paquete de presentación descargable](AULA_PRESENTACION_HOY.zip).
- [Código de la demo](demo/index.html).

## Uso local

Abrir `demo/index.html` en un navegador. Es un archivo independiente: no requiere instalación, servidor ni conexión a internet.

## Alcance previsto

La versión con IA recibirá material textual, recuperará fragmentos pertinentes y utilizará un modelo preentrenado para proponer preguntas con referencias. El docente conservará la aprobación final. Se prevé trabajar representación del texto, similitud coseno, TF-IDF, embeddings, RAG y una evaluación pequeña de resultados. No se entrenará un modelo desde cero.

La demo de presentación está implementada. El procesamiento real de documentos y la conexión con modelos de IA todavía no están implementados.

## Publicación con GitHub Pages

El workflow [pages.yml](.github/workflows/pages.yml) publica únicamente `demo/` al actualizar `main`. Los documentos del integrador se consultan en el repositorio. La publicación se realiza con GitHub Actions y puede ejecutarse manualmente desde la pestaña Actions.

## Regenerar el informe (opcional)

El PDF se genera a partir de `PROPUESTA_PARA_ENTREGA.md` mediante `scripts/generar_informe.py`. Para regenerarlo en un entorno Python con las dependencias de `scripts/requirements-informe.txt`:

```bash
python scripts/generar_informe.py
```

Los archivos temporales de renderizado y los entornos locales se excluyen de Git.
