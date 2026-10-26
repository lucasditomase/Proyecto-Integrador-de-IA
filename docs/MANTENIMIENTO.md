# Mantener documentación, entrega y publicación

## Orden de lectura y fuentes

Para retomar: README → ESTADO_Y_CONTINUIDAD → ALCANCE_DE_LA_PROPUESTA → PLAN_DEL_PROYECTO. Consultar DECISIONES_Y_OPCIONES para alternativas y CLASIFICADOR_TEMATICO para el experimento previsto. AGENTS.md contiene instrucciones de trabajo, no una nueva especificación del producto.

La documentación vigente describe lo que se propone y lo que está implementado por separado. Git conserva estados históricos. Ante una discrepancia, verificar la evidencia e instrucciones recientes del estudiante, registrar la decisión y alinear los documentos; no elegir silenciosamente una versión. Las preguntas progresivas de los HTML no tienen respuestas personales confirmadas por el solo hecho de que un asistente haya redactado una propuesta.

## Actualizar una decisión

1. Registrar fecha, procedencia (estudiante/cátedra/recomendación/experimento), motivo, estado y pendientes en ESTADO_Y_CONTINUIDAD.
2. Si cambia el compromiso funcional, actualizar ALCANCE_DE_LA_PROPUESTA y revisar plan, decisiones, informe y guion. Incrementar la versión de presentación cuando corresponda y actualizarla en README, HTML y empaquetador.
3. Si solo mejora la documentación de continuidad sin cambiar el alcance, conservar v0.3 y registrar esa revisión. Evitar regenerar un PDF cuyo Markdown no cambió.
4. Actualizar el resumen privado de la materia si cambia un acuerdo transversal. Las prácticas y experimentos enlazan al integrador en lugar de duplicar todo su plan.

## Archivos derivados

Desde la raíz del repo, con Python 3 y las dependencias de `scripts/requirements-informe.txt` disponibles:

```bash
python3 scripts/generar_informe.py
```

Solo hace falta si cambió PROPUESTA_PARA_ENTREGA.md o el generador. Revisar texto y renderizado del PDF; actualmente son dos páginas. No confundir ejecución sin errores con una composición legible.

Si cambia un archivo incluido en ARCHIVOS de `scripts/preparar_presentacion.py`, regenerar al final:

```bash
python3 scripts/preparar_presentacion.py
```

El script usa biblioteca estándar y comprueba ZIP y hashes. VERSION_PRESENTACION.json y AULA_PRESENTACION_HOY.zip deben corresponder a los archivos fuente actuales. Si cambia la demo, recorrer el flujo y actualizar `demo/preview.png` antes de empaquetar. No editar el ZIP como fuente ni guardar claves, datos privados o archivos temporales en él. El original del compañero no forma parte del paquete público.

## Verificación proporcionada

Para cambios documentales: revisar enlaces relativos, títulos/fechas, decisiones actuales frente a históricas, concordancia de alcance y manifiesto/ZIP. No requiere entrenamientos ni ejecutar notebooks docentes. Para cambios funcionales de la demo: comprobar configuración, edición, etiquetas, aprobación/descarte y exportación sin revelar clave docente; verificar que los avisos de simulación siguen siendo visibles. Para modelos futuros: registrar datos/particiones, parámetros, métricas y errores; evitar fuga y test usado para ajustar.

## Git y Pages

Antes de editar/commitear, consultar `git status --short --branch` y revisar el diff. Comitear solo cambios propios pertinentes; respetar trabajo ajeno. Tras un push, verificar el estado remoto cuando se informe que quedó sincronizado; una referencia origin local puede estar desactualizada. No cambiar visibilidad ni copiar fuentes privadas como parte de una actualización documental.

Este repo es público. `.github/workflows/pages.yml` despliega **solo `demo/`** al pushear `main` con cambios en `demo/**` o en el workflow. También admite ejecución manual. Cambios únicamente en Markdown/PDF/ZIP no disparan Pages ni la necesitan. Los documentos se publican en el repositorio, no en la raíz del sitio Pages.

Si se modificó la demo, comprobar el resultado de Actions y el contenido público antes de afirmar que está publicado. Un push no prueba que el despliegue terminó. Pages aloja HTML/JS estático; la futura IA deberá usar los métodos locales o externos efectivamente implementados.

## Skills y alcance de las instrucciones

Por ahora bastan AGENTS.md y esta guía: no hay una tarea recurrente independiente que justifique una skill propia. No crear un SKILL.md que duplique decisiones mutables o instale un flujo global sin necesidad. Si aparece un procedimiento reutilizable, diseñarlo separado de los datos y decisiones de este proyecto, siguiendo las instrucciones vigentes del entorno.
