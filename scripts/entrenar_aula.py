"""Entrena regresión logística multiclase con TF-IDF y genera evidencia reproducible."""
from collections import Counter
import json
import math
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
STOP = set('como cuando cual cuales que quien para por con las los una uno unos del desde esta este esto esa ese eso sus son hay tiene usar entre ante sobre sin mas muy donde cada que al de un y o el la en se su lo es a'.split())
RULES = [
    'vector vectores escalar coseno norma euclidiana distancia vecinos vecino k-nn representacion escala unidades'.split(),
    'particion validacion prueba fuga faltantes faltante atipico desbalance desbalanceado accuracy confusion falsos falso'.split(),
    'neurona pesos sesgo preactivacion relu activacion activaciones backpropagation gradiente gradientes optimizador capas red sobreajuste'.split(),
]
EPOCHS = 450
RATE = 1.0
L2 = 0.025


def words(text):
    decomposed = unicodedata.normalize('NFD', text)
    clean = re.sub(r'[\u0300-\u036f]', '', decomposed).lower()
    return [token for token in re.findall(r'[a-z0-9]+', clean) if token not in STOP]


def vector(text, idf):
    values = {term: (1 + math.log(n)) * idf[term]
              for term, n in Counter(words(text)).items() if term in idf}
    norm = math.sqrt(sum(value * value for value in values.values()))
    return {term: value / norm for term, value in values.items()} if norm else {}


def scores(features, weights, biases):
    result = biases.copy()
    for term, value in features.items():
        for i, weight in enumerate(weights[term]):
            result[i] += weight * value
    return result


def train(rows, labels):
    df = Counter(term for row in rows for term in set(words(row['enunciado'])))
    idf = {term: 1 + math.log((1 + len(rows)) / (1 + df[term])) for term in sorted(df)}
    samples = [(vector(row['enunciado'], idf), labels.index(row['tema_propuesto'])) for row in rows]
    weights, biases = {term: [0.0] * len(labels) for term in idf}, [0.0] * len(labels)
    for _ in range(EPOCHS):
        gradient = {term: [L2 * weight for weight in coefficients] for term, coefficients in weights.items()}
        bias_gradient = [0.0] * len(labels)
        for features, expected in samples:
            logits = scores(features, weights, biases)
            exp = [math.exp(logit - max(logits)) for logit in logits]
            for i, probability in enumerate(exp):
                error = (probability / sum(exp) - int(i == expected)) / len(samples)
                bias_gradient[i] += error
                for term, value in features.items():
                    gradient[term][i] += error * value
        for i, derivative in enumerate(bias_gradient):
            biases[i] -= RATE * derivative
        for term in weights:
            for i, derivative in enumerate(gradient[term]):
                weights[term][i] -= RATE * derivative
    return {'version': 1, 'labels': labels, 'idf': idf, 'weights': weights, 'biases': biases}


def classify(text, model):
    features = vector(text, model['idf'])
    if not features:
        return '', []
    logits = scores(features, model['weights'], model['biases'])
    return model['labels'][logits.index(max(logits))], logits


def baseline(text, labels):
    terms = set(words(text))
    hits = [len(terms.intersection(word for rule in rules for word in words(rule))) for rules in RULES]
    return labels[hits.index(max(hits))] if max(hits) else ''


def evaluate(rows, key, labels):
    matrix = {expected: {pred: 0 for pred in labels + ['abstencion']} for expected in labels}
    for row in rows:
        matrix[row['expected']][row[key] or 'abstencion'] += 1
    f1 = {}
    for category in labels:
        tp = matrix[category][category]
        total = sum(matrix[category].values()) + sum(row[category] for row in matrix.values())
        f1[category] = 2 * tp / total if total else 0
    return {'matrix': matrix, 'f1': f1, 'macroF1': sum(f1.values()) / len(labels)}


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    pilot = json.loads((ROOT / 'datos/piloto_clasificacion.json').read_text(encoding='utf-8'))
    evaluation = json.loads((ROOT / 'datos/evaluacion_clasificacion.json').read_text(encoding='utf-8'))
    labels = list(pilot['categorias'])
    training = pilot['ejemplos']
    train_groups = {row['grupo_conceptual'] for row in training}
    test_groups = {label + '/' + group for label, group, _ in evaluation['ejemplos']}
    assert train_groups.isdisjoint(test_groups), 'Un grupo aparece en entrenamiento y prueba'
    assert set(labels) == {row['tema_propuesto'] for row in training}
    assert set(labels) == {label for label, _, _ in evaluation['ejemplos']}
    assert {tuple(words(row['enunciado'])) for row in training}.isdisjoint(
        tuple(words(text)) for _, _, text in evaluation['ejemplos'])
    model = train(training, labels)
    rows = []
    for label, group, text in evaluation['ejemplos']:
        predicted, logits = classify(text, model)
        rows.append({'text': text, 'group': label + '/' + group, 'expected': label,
                     'baseline': baseline(text, labels), 'model': predicted, 'scores': logits})
    report = {'labels': labels, 'trainCount': len(training), 'testCount': len(rows),
              'parameters': {'epochs': EPOCHS, 'rate': RATE, 'l2': L2},
              'baseline': evaluate(rows, 'baseline', labels), 'model': evaluate(rows, 'model', labels),
              'cases': rows}
    save(ROOT / 'datos/modelo_aula.json', model)
    save(ROOT / 'datos/resultados_clasificacion.json', report)
    print(f'{len(training)} ejemplos de entrenamiento y {len(rows)} reservados')
    for key in ['baseline', 'model']:
        print(f'{key}: macro-F1 {report[key]["macroF1"]:.3f}')


if __name__ == '__main__':
    main()
