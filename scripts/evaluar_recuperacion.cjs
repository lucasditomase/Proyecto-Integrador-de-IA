'use strict';

const fs = require('node:fs');
const path = require('node:path');
const Aula = require('../app/core.cjs');
const root = path.join(__dirname, '..');
const data = require('../datos/evaluacion_recuperacion.json');
const index = Aula.indexFor(Aula.fragments(data.documents));
const k = 3;
const cases = data.queries.map(([type, query, ...relevant]) => {
  const results = {};
  for (const method of ['lexical', 'tfidf']) {
    const ranked = Aula.search(index, query, method).slice(0, k).map(item => item.fragment.id);
    results[method] = {ranked, precision: relevant.length ? ranked.filter(id => relevant.includes(id)).length / k : null};
  }
  return {type, query, relevant, results};
});
const labelled = cases.filter(item => item.relevant.length);
const mean = {};
for (const method of ['lexical', 'tfidf']) {
  mean[method] = labelled.reduce((sum, item) => sum + item.results[method].precision, 0) / labelled.length;
  console.log(method + ': Precision@' + k + ' ' + mean[method].toFixed(3));
}
fs.writeFileSync(path.join(root, 'datos/resultados_recuperacion.json'), JSON.stringify({k, mean, cases}, null, 2) + '\n');
