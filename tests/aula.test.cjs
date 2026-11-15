'use strict';

const assert = require('node:assert/strict');
const {test} = require('node:test');
const Aula = require('../app/core.cjs');
const model = require('../datos/modelo_aula.json');
const report = require('../datos/resultados_clasificacion.json');
const recovery = require('../datos/evaluacion_recuperacion.json');

const doc = Aula.documentFrom('material', 'Notas <privadas>', 'Una prueba mide rendimiento.\r\n\r\nEl ajuste emplea entrenamiento.');
const sourceIds = new Set(['material-1', 'material-2']);
const candidate = {text: '<img src=x> ¿Qué se reserva?', options: ['Prueba', 'Ajuste', 'Imágenes', 'Pesos'],
  keys: [0], sourceId: 'material-1', rationale: 'solo-docente & respaldo'};
const approved = Aula.question(candidate, sourceIds, 'q1', 'approved');
const raw = {kind: 'aula-project', version: 1, title: 'Repaso', documents: [doc],
  questions: [approved, Aula.question({...candidate, text: 'EXCLUIR BORRADOR'}, sourceIds, 'q2')],
  request: {id: 'pedido', sourceIds: ['material-1']}};

test('fragmentos reproducibles conservan origen y línea, y acotan la entrada', () => {
  const passages = Aula.fragments([doc]);
  assert.deepEqual(passages.map(({id, line}) => [id, line]), [['material-1', 1], ['material-2', 3]]);
  assert.throws(() => Aula.documentFrom('d', 'Título', '   '), /material/);
  assert.throws(() => Aula.documentFrom('d', 'Título', 'a\n\n'.repeat(501)), /500 fragmentos/);
});

test('archivos de proyecto conservan datos y rechazan claves, estados o fuentes inválidas', () => {
  assert.deepEqual(Aula.project(JSON.parse(JSON.stringify(raw))), raw);
  assert.throws(() => Aula.question({...candidate, keys: [0, 1, 2]}, sourceIds, 'q'), /una o dos/);
  assert.deepEqual(Aula.question({...candidate, keys: [2, 0]}, sourceIds, 'q').keys, [0, 2]);
  assert.throws(() => Aula.project({...raw, questions: [{...approved, status: 'other'}]}), /Estado/);
  assert.throws(() => Aula.project({...raw, questions: [{...approved, sourceId: 'otra'}]}), /fragmento/);
});

test('intercambio vinculado al pedido y a sus referencias, con validación de todo el lote', () => {
  const request = {kind: 'aula-candidates', version: 1, requestId: 'pedido', questions: [candidate]};
  const passages = Aula.fragments([doc]);
  const selected = new Set(['material-1']);
  const importBatch = response => Aula.candidates(response, passages, 'pedido', selected, () => 'importada');
  assert.equal(importBatch(request)[0].status, 'pending');
  assert.throws(() => importBatch({...request, requestId: 'otro'}), /pedido vigente/);
  assert.throws(() => importBatch({...request, questions: [candidate, {...candidate, sourceId: 'material-2'}]}), /fragmento/);
  assert.throws(() => importBatch(JSON.parse(']')), SyntaxError);
  assert.equal(raw.questions.length, 2);
});

test('exportación estudiantil excluye marcas, fundamento, fuente y pendientes', () => {
  const student = Aula.examHtml(raw, false);
  const teacher = Aula.examHtml(raw, true);
  assert.match(student, /&lt;img src=x&gt;/);
  assert.doesNotMatch(student, /✓|EXCLUIR BORRADOR|solo-docente|privadas|<img/);
  assert.match(teacher, /✓ Correcta/);
  assert.match(teacher, /solo-docente &amp; respaldo/);
  assert.doesNotMatch(teacher, /EXCLUIR BORRADOR/);
});

test('búsqueda real sobre el corpus y caso de abstención', () => {
  const index = Aula.indexFor(Aula.fragments(recovery.documents));
  for (const method of ['lexical', 'tfidf']) {
    assert.equal(Aula.search(index, 'producto escalar coseno', method)[0].fragment.id, 'vectores-2');
    assert.deepEqual(Aula.search(index, 'zzzxq', method), []);
  }
});

test('Python y JS coinciden en etiquetas y puntuaciones de los casos reservados', () => {
  const classify = Aula.classifier(model);
  for (const row of report.cases) {
    const result = classify(row.text);
    assert.equal(result.topic, row.model, row.text);
    assert.equal(result.scores.length, row.scores.length);
    result.scores.forEach((score, index) => assert.ok(Math.abs(score - row.scores[index]) < 1e-9));
  }
  assert.deepEqual(classify('zzzxq astronaves'), {topic: '', scores: []});
});
