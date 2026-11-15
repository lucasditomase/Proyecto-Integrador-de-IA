"""Empaqueta JavaScript, CSS y el modelo en el HTML servido por Pages y usable offline."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
target = ROOT / 'demo/aula.html'
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
html = (ROOT / 'app/index.html').read_text(encoding='utf-8')
for token, path in [('/* STYLES */', 'app/styles.css'), ('/* CORE */', 'app/core.cjs'), ('/* UI */', 'app/ui.js')]:
    assert html.count(token) == 1
    html = html.replace(token, (ROOT / path).read_text(encoding='utf-8').strip())
model = json.loads((ROOT / 'datos/modelo_aula.json').read_text(encoding='utf-8'))
html = html.replace('__AULA_MODEL__', json.dumps(model, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'))
if args.check:
    if not target.is_file() or target.read_text(encoding='utf-8') != html:
        raise SystemExit('demo/aula.html está desactualizado. Ejecutá scripts/construir_aula.py.')
else:
    target.write_bytes(html.encode('utf-8'))
print(f'demo/aula.html: {len(html.encode())} bytes')
