"""Empaquetar la presentación vigente y registrar sus versiones. No conecta APIs."""
from pathlib import Path
import hashlib
import json
import zipfile

BASE = Path(__file__).resolve().parents[1]
ARCHIVOS = [
    "ALCANCE_DE_LA_PROPUESTA.md",
    "CLASIFICADOR_TEMATICO.md",
    "docs/ESTADO_Y_CONTINUIDAD.md",
    "docs/MANTENIMIENTO.md",
    "docs/REVISION_ACADEMICA_Y_VIABILIDAD.md",
    "datos/piloto_clasificacion.json",
    "PROPUESTA_PARA_ENTREGA.md",
    "output/pdf/PROPUESTA_PARA_ENTREGA.pdf",
    "PLAN_DEL_PROYECTO.md",
    "DECISIONES_Y_OPCIONES.md",
    "GUIA_PARA_PRESENTAR.md",
    "demo/index.html",
    "demo/preview.png",
]
LEEME = """# Aula · Presentación v0.3

1. Leer output/pdf/PROPUESTA_PARA_ENTREGA.pdf.
2. Abrir demo/index.html en un navegador para recorrer la simulación.
3. Consultar GUIA_PARA_PRESENTAR.md para explicar el alcance.

ALCANCE_DE_LA_PROPUESTA.md es la referencia común. El mínimo propuesto funciona sin API; la asistencia externa es opcional. La conexión API directa necesita validar un proveedor. El intercambio manual no es una conexión automática.

Se integra un clasificador temático propuesto para organizar preguntas. Los datos piloto son exploratorios, con etiquetas pendientes de revisión; no hay un modelo entrenado. Las etiquetas de la demo son precargadas y corregibles.

La demo usa preguntas preparadas. No procesa material propio ni tiene IA conectada. Los modos básico y asistido son explicativos y utilizan los mismos ejemplos.

El HTML incluye sus recursos y abre sin instalación. La aplicación final aún no está implementada. El modo básico previsto no requiere pagos; un servicio externo tiene sus propias condiciones y no está incluido.

VERSION_PRESENTACION.json permite comprobar que estos archivos coinciden con los empaquetados en esta edición. El informe Markdown es editable. Incorporar nombres de los integrantes si se requiere antes de entregar.
"""

def main():
    for name in ARCHIVOS:
        if not (BASE / name).is_file():
            raise FileNotFoundError(name)
    manifiesto = {
        "version": "0.3",
        "fecha": "2026-10-26",
        "estado": "propuesta y demo simulada; producto final no implementado",
        "alcance": "ALCANCE_DE_LA_PROPUESTA.md",
        "sha256": {name: hashlib.sha256((BASE / name).read_bytes()).hexdigest() for name in ARCHIVOS},
    }
    (BASE / "VERSION_PRESENTACION.json").write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2) + "\n")
    ruta = BASE / "AULA_PRESENTACION_HOY.zip"
    with zipfile.ZipFile(ruta, "w", zipfile.ZIP_DEFLATED) as archivo:
        for name in ARCHIVOS + ["VERSION_PRESENTACION.json"]:
            archivo.write(BASE / name, name)
        archivo.writestr("LEEME.md", LEEME)
    with zipfile.ZipFile(ruta) as archivo:
        assert archivo.testzip() is None
        for name, digest in manifiesto["sha256"].items():
            assert hashlib.sha256(archivo.read(name)).hexdigest() == digest
    print("Presentación v0.3 preparada y verificada:", ruta)

if __name__ == "__main__":
    main()
