'use strict';

const Aula = (() => {
  const topics = {
    representacion_vecinos: 'Representación y vecinos',
    datos_evaluacion: 'Datos y evaluación',
    redes_aprendizaje: 'Redes y aprendizaje',
  };
  const stop = new Set('como cuando cual cuales que quien para por con las los una uno unos del desde esta este esto esa ese eso sus son hay tiene usar entre ante sobre sin mas muy donde cada que al de un y o el la en se su lo es a'.split(' '));
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const tokens = text => (normalize(text).match(/[a-z0-9]+/g) || []).filter(t => !stop.has(t));
  const counts = words => {
    const result = new Map();
    for (const word of words) result.set(word, (result.get(word) || 0) + 1);
    return result;
  };
  const clean = (value, max, label) => {
    if (typeof value !== 'string' || !value.trim() || value.length > max) {
      throw new Error(label + ' debe tener entre 1 y ' + max + ' caracteres.');
    }
    return value.trim();
  };
  const expect = (condition, message) => {
    if (!condition) throw new Error(message);
  };
  const object = value => value && typeof value === 'object' && !Array.isArray(value);
  const id = (value, label) => {
    expect(typeof value === 'string' && /^[a-zA-Z0-9_-]{1,80}$/.test(value), label + ' inválido.');
    return value;
  };
  function documentFrom(identifier, name, text) {
    text = clean(text, 200000, 'El material').replace(/\r\n?/g, '\n');
    const document = {id: id(identifier, 'Identificador'), name: clean(name, 200, 'El título'), text};
    fragments([document]);
    return document;
  }
  function fragments(documents) {
    return documents.flatMap(doc => {
      const result = [];
      let prevOffset = 0;
      let line = 1;
      for (const block of doc.text.matchAll(/\S[\s\S]*?(?=\n[ \t]*\n|$)/g)) {
        let offset = block.index;
        let remaining = block[0];
        while (remaining.length) {
          const lastSpace = remaining.length > 1000 ? remaining.lastIndexOf(' ', 1000) : remaining.length;
          const length = lastSpace > 500 ? lastSpace : Math.min(remaining.length, 1000);
          const text = remaining.slice(0, length).trim();
          if (text) {
            expect(result.length < 500, 'El material supera los 500 fragmentos por documento.');
            line += doc.text.slice(prevOffset, offset).split('\n').length - 1;
            prevOffset = offset;
            result.push({id: doc.id + '-' + (result.length + 1), name: doc.name, text, line});
          }
          const next = remaining.slice(length);
          offset += length + next.length - next.trimStart().length;
          remaining = next.trimStart();
        }
      }
      return result;
    });
  }
  function vector(words, idf) {
    const weighted = new Map();
    let squared = 0;
    for (const [term, times] of counts(words)) {
      if (!idf.has(term)) continue;
      const weight = (1 + Math.log(times)) * idf.get(term);
      weighted.set(term, weight);
      squared += weight * weight;
    }
    if (squared) {
      const norm = Math.sqrt(squared);
      for (const [term, weight] of weighted) weighted.set(term, weight / norm);
    }
    return weighted;
  }
  function indexFor(items) {
    const frequency = new Map();
    const rows = items.map(item => {
      const words = tokens(item.text);
      const terms = new Set(words);
      for (const term of terms) frequency.set(term, (frequency.get(term) || 0) + 1);
      return {item, words, terms};
    });
    const idf = new Map([...frequency].map(([term, df]) =>
      [term, 1 + Math.log((1 + rows.length) / (1 + df))]));
    for (const row of rows) row.vector = vector(row.words, idf);
    return {rows, idf};
  }
  function search(index, query, method) {
    const words = tokens(query);
    const terms = new Set(words);
    const queryVector = vector(words, index.idf);
    return index.rows.map(row => {
      let score = 0;
      if (method === 'lexical') {
        for (const term of terms) if (row.terms.has(term)) score++;
      } else {
        for (const [term, weight] of queryVector) score += weight * (row.vector.get(term) || 0);
      }
      return {fragment: row.item, score};
    }).filter(entry => entry.score > 0).sort((a, b) => b.score - a.score);
  }
  function classifier(model) {
    const idf = new Map(Object.entries(model.idf));
    return text => {
      const features = vector(tokens(text), idf);
      if (!features.size) return {topic: '', scores: []};
      const scores = model.biases.slice();
      for (const [term, weight] of features) {
        for (const [i, coefficient] of model.weights[term].entries()) scores[i] += weight * coefficient;
      }
      return {topic: model.labels[scores.indexOf(Math.max(...scores))], scores};
    };
  }
  function question(input, sources, identifier, status = 'pending') {
    expect(object(input), 'Cada pregunta debe ser un objeto.');
    expect(Array.isArray(input.options) && input.options.length === 4, 'Se requieren cuatro opciones.');
    const options = input.options.map(option => clean(option, 500, 'La opción'));
    expect(new Set(options.map(normalize)).size === 4, 'Las cuatro opciones deben ser diferentes.');
    const keys = input.keys;
    expect(Array.isArray(keys) && (keys.length === 1 || keys.length === 2) &&
      keys.every(key => Number.isInteger(key) && key >= 0 && key < 4) &&
      new Set(keys).size === keys.length, 'Marcá una o dos respuestas correctas diferentes.');
    expect(sources.has(input.sourceId), 'La pregunta debe referenciar un fragmento válido.');
    expect(['pending', 'approved', 'discarded'].includes(status), 'Estado de pregunta inválido.');
    const topic = input.topic ?? '';
    expect(typeof topic === 'string' && topic.length <= 80, 'Tema inválido.');
    return {id: id(identifier, 'Identificador de pregunta'), text: clean(input.text, 1500, 'El enunciado'),
      options, keys: keys.slice().sort(), sourceId: input.sourceId,
      rationale: clean(input.rationale, 2500, 'El fundamento'), topic: topic.trim(), status};
  }
  function project(input) {
    expect(object(input) && input.kind === 'aula-project' && input.version === 1, 'Formato de proyecto incompatible.');
    expect(Array.isArray(input.documents) && input.documents.length <= 10, 'El proyecto admite hasta 10 documentos.');
    expect(Array.isArray(input.questions) && input.questions.length <= 200, 'El proyecto admite hasta 200 preguntas.');
    const documents = input.documents.map(doc => {
      expect(object(doc), 'Documento inválido.');
      return documentFrom(doc.id, doc.name, doc.text);
    });
    expect(new Set(documents.map(doc => doc.id)).size === documents.length, 'Hay documentos con ID repetido.');
    const sources = new Set(fragments(documents).map(fragment => fragment.id));
    const questions = input.questions.map(item => {
      expect(object(item), 'Pregunta inválida.');
      return question(item, sources, item.id, item.status);
    });
    expect(new Set(questions.map(item => item.id)).size === questions.length, 'Hay preguntas con ID repetido.');
    let request = null;
    if (input.request != null) {
      expect(object(input.request) && Array.isArray(input.request.sourceIds) &&
        input.request.sourceIds.length >= 1 && input.request.sourceIds.length <= 12 &&
        input.request.sourceIds.every(ref => sources.has(ref)) &&
        new Set(input.request.sourceIds).size === input.request.sourceIds.length, 'Pedido guardado inválido.');
      request = {id: id(input.request.id, 'Identificador de pedido'), sourceIds: input.request.sourceIds.slice()};
    }
    return {kind: 'aula-project', version: 1, title: clean(input.title, 160, 'El título'), documents, questions, request};
  }
  function candidates(input, currentFragments, requestId, selectedIds, makeId) {
    expect(requestId && object(input) && input.kind === 'aula-candidates' && input.version === 1 &&
      input.requestId === requestId, 'La respuesta debe corresponder al pedido vigente.');
    expect(Array.isArray(input.questions) && input.questions.length > 0 && input.questions.length <= 20,
      'La respuesta debe traer entre 1 y 20 preguntas.');
    const sources = new Set(currentFragments.filter(fragment => selectedIds.has(fragment.id)).map(fragment => fragment.id));
    return input.questions.map(item => question(item, sources, makeId()));
  }
  const escape = value => String(value).replace(/[&<>"']/g, char =>
    ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'})[char]);
  function examHtml(current, teacher) {
    const approved = current.questions.filter(item => item.status === 'approved');
    expect(approved.length, 'Aprobá al menos una pregunta.');
    const sourceMap = new Map(fragments(current.documents).map(fragment => [fragment.id, fragment]));
    const title = escape(current.title) + (teacher ? ' · Clave docente' : '');
    const questions = approved.map(item => {
      const source = sourceMap.get(item.sourceId);
      const options = item.options.map((option, i) =>
        '<li>' + escape(option) + (teacher && item.keys.includes(i) ? ' <strong>✓ Correcta</strong>' : '') + '</li>').join('');
      const notes = teacher ? '<p><strong>Fundamento:</strong> ' + escape(item.rationale) +
        '</p><p><strong>Fuente:</strong> ' + escape(source.name) + ' · línea ' + source.line +
        '</p><blockquote>' + escape(source.text) + '</blockquote>' : '';
      return '<li class="question"><strong>' + escape(item.text) + '</strong><p>Marcá ' +
        (item.keys.length === 1 ? 'una opción.' : 'exactamente dos opciones.') +
        '</p><ol type="A">' + options + '</ol>' + notes + '</li>';
    }).join('');
    return '<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>' +
      title + '</title><style>body{font:16px/1.6 Georgia,serif;max-width:760px;margin:2rem auto;padding:0 1rem}li{margin:.4rem 0}.question{margin:1.4rem 0;break-inside:avoid}</style></head><body><h1>' +
      title + '</h1>' + (teacher ? '' : '<p>Nombre: ________________________ Fecha: __________</p>') +
      '<ol>' + questions + '</ol></body></html>';
  }
  return {topics, tokens, documentFrom, fragments, indexFor, search, classifier, question, project, candidates, examHtml};
})();
if (typeof module !== 'undefined') module.exports = Aula;
