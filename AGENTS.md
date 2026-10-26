# Instrucciones de trabajo en Aula

## Leer primero

README.md → docs/ESTADO_Y_CONTINUIDAD.md → ALCANCE_DE_LA_PROPUESTA.md. Consultar PLAN_DEL_PROYECTO.md y CLASIFICADOR_TEMATICO.md para el diseño; docs/MANTENIMIENTO.md para cambios y artefactos derivados. Las instrucciones recientes del usuario tienen prioridad; mantener la documentación al día si cambian decisiones.

## Propósito y fase

Integrador de IA de dos estudiantes. El valor es demostrar conocimientos de la cátedra con una necesidad útil, métodos justificados, comparación y errores; no hacer una plataforma extensa. La fase actual es propuesta/planificación y demo simulada. No iniciar entrenamiento o implementación real por una solicitud de revisar documentos. Una futura solicitud explícita de desarrollar cambia esa fase y debe registrarse, sin pedir nuevamente permisos ya otorgados.

Presupuesto del grupo cero. Debe existir un recorrido útil offline, sin clave, Mac, GPU, Python obligatorio para profesores o LLM local. HTML descargable es la dirección recomendada; consola de desarrollo no implica consola obligatoria para docentes. No contratar servicios ni asumir acceso gratuito universal.

## Estado y límites que deben preservarse

Demo v0.3 usa preguntas y etiquetas precargadas; no ejecuta TF-IDF, clasificador ni IA externa y no guarda proyectos al recargar. No presentar simulaciones como inferencia o generación real. La asistencia avanzada mínima propuesta es intercambio manual estructurado. API directa solo tras validar un proveedor y sus condiciones, costo y acceso desde navegador. No reutilizar sesiones de OpenCode/Cline como si fueran API ni atribuir acceso API a una suscripción de chat.

Clasificador propuesto: tres temas de IA, TF-IDF/regresión logística frente a palabras clave y corrección docente. Los 30 ejemplos son exploratorios, redactados por el asistente y pendientes de revisión. No hay modelo ni métricas. Separar por grupos conceptuales, ajustar vocabulario/IDF con entrenamiento y preservar prueba. No confundir etiqueta temática con corrección, dificultad o certeza calibrada. Plantillas y embeddings son ampliaciones, no compromisos mínimos.

## Documentación y evidencia

Mantener fuente común de alcance, informe Markdown/PDF, plan, opciones, guion, demo, captura, manifiesto y ZIP coherentes. Reemplazar frases obsoletas en el estado vigente y conservar motivos en cronología/Git. No atribuir a los estudiantes respuestas personales no confirmadas ni aprobación de la cátedra. No informar entrenamientos, métricas, pruebas o despliegues sin evidencia.

Los originales docentes y el PDF del compañero están en el repo privado de teoría. Este repo es público: no copiarlos aquí ni al ZIP sin autorización específica. No guardar claves en código, logs, repositorios o exportaciones; una futura API debe conservar trabajo ante fallas y no cambiar automáticamente a servicios pagos.

## Verificación y publicación

Usar la guía de mantenimiento. Solo regenerar PDF si cambió su fuente; revisar visualmente cuando se regenere. Regenerar paquete tras cambios en sus archivos incluidos y comprobar hashes. Probar lo adecuado al cambio; documentación no requiere ejecutar notebooks o entrenar modelos. Evitar artefactos temporales y cambios ajenos en commits. No hacer push a upstream de los otros repos como parte de este trabajo. Si cambia demo/, verificar Actions y contenido publicado; cambios solo documentales no requieren redeploy de Pages.
