#!/usr/bin/env python3
"""Hipótese 'alucinações silenciosas': o que escapa aos testes e à análise estática.

B) Matriz de cobertura por implementação: {teste E estático / só teste / só estático / escapa dos dois}
   + IC 95% bootstrap agrupado por tarefa, quebras por modelo/dataset/tipo.
A) Piloto preditivo: features de análise estática (regras Sonar) predizem o TIPO de alucinação?
   CV agrupado por tarefa + transferência cross-model (gate: AUC >= 0.6).

Uso: python scripts/analise_silenciosas.py
Salva CSVs em sonarqube_labeled/artifacts/ e figura em docs/.
"""
import json
from collections import defaultdict
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / 'sonarqube_labeled' / 'artifacts'
ART = LAB
RNG = np.random.default_rng(42)

# ---------- dados ----------
meta = {}
for line in open(LAB / 'metadata.jsonl', encoding='utf-8'):
    if not line.strip():
        continue
    d = json.loads(line)
    types = {cl.get('hallucination-type') for cl in (d.get('code_labels') or []) if cl.get('hallucination-type')}
    meta[d['row_number']] = dict(tid=d['_id'], dataset=d['dataset'], model=d['model'],
                                 is_pass=bool((d.get('evaluation_result') or {}).get('is_pass')), types=types)

issues = json.load(open(LAB / 'mapped_issues.json', encoding='utf-8'))
rules = sorted({i['sonar_rule'] for i in issues})
rule_ix = {r: k for k, r in enumerate(rules)}
row_issues = defaultdict(list)
for i in issues:
    row_issues[i['row_number']].append(i)

rows = {}
for rn, m in meta.items():
    fail = not m['is_pass']
    issue = bool(row_issues.get(rn))
    cell = 'both' if (fail and issue) else 'test_only' if fail else 'static_only' if issue else 'none'
    rows[rn] = dict(tid=m['tid'], dataset=m['dataset'], model=m['model'], types=m['types'], cell=cell)

CELLS = ['both', 'test_only', 'static_only', 'none']
LBL = {'both': 'teste E estático', 'test_only': 'só teste', 'static_only': 'só estático', 'none': 'escapa dos dois'}
N = len(rows)

# ---------- B) cobertura ----------
def props(sub):
    n = len(sub)
    return {c: sum(1 for r in sub.values() if r['cell'] == c) / n for c in CELLS}

p = props(rows)
tasks = defaultdict(list)
for rn, r in rows.items():
    tasks[r['tid']].append(rn)
tids = list(tasks)
boot = {c: [] for c in CELLS}
for _ in range(2000):
    sample = [rn for t in RNG.choice(tids, size=len(tids), replace=True) for rn in tasks[t]]
    cnt = defaultdict(int)
    for rn in sample:
        cnt[rows[rn]['cell']] += 1
    for c in CELLS:
        boot[c].append(cnt[c] / len(sample))

print(f'B) Cobertura ({N} implementações anotadas, todas com alucinação):')
ci = {}
for c in CELLS:
    lo, hi = np.percentile(boot[c], [2.5, 97.5])
    ci[c] = (lo, hi)
    print(f'   {LBL[c]:16} {p[c]*100:5.1f}%  IC95% [{lo*100:.1f}, {hi*100:.1f}]')

with open(ART / 'coverage_gates.csv', 'w') as f:
    f.write('cell,prop,ci_low,ci_high\n')
    for c in CELLS:
        f.write(f'{c},{p[c]:.4f},{ci[c][0]:.4f},{ci[c][1]:.4f}\n')

def group_rates(key):
    out = []
    for v in sorted({r[key] for r in rows.values()}):
        sub = {rn: r for rn, r in rows.items() if r[key] == v}
        pp = props(sub)
        out.append((v, len(sub), pp))
    return out

print('\n   por modelo (escapa_ambos / passa_teste / sem_issue):')
for v, nk, pp in group_rates('model'):
    print(f'     {v:22} n={nk:4}  {pp["none"]*100:5.1f}%  {(pp["static_only"]+pp["none"])*100:5.1f}%  {(pp["test_only"]+pp["none"])*100:5.1f}%')
print('   por dataset:')
for v, nk, pp in group_rates('dataset'):
    print(f'     {v:10} n={nk:4}  {pp["none"]*100:5.1f}%  {(pp["static_only"]+pp["none"])*100:5.1f}%  {(pp["test_only"]+pp["none"])*100:5.1f}%')

# ---------- A) piloto preditivo ----------
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score

rowsn = sorted(meta)
n = len(rowsn)
X = np.zeros((n, len(rules) + 3))
for k, rn in enumerate(rowsn):
    for i in row_issues[rn]:
        X[k, rule_ix[i['sonar_rule']]] = 1
    X[k, len(rules)] = len(row_issues[rn])
    X[k, len(rules) + 1] = sum(1 for i in row_issues[rn] if i['sonar_type'] == 'BUG')
    X[k, len(rules) + 2] = sum(1 for i in row_issues[rn] if i['sonar_type'] == 'CODE_SMELL')
models = np.array([meta[rn]['model'] for rn in rowsn])
gid = {t: k for k, t in enumerate(sorted({meta[rn]['tid'] for rn in rowsn}))}
groups = np.array([gid[meta[rn]['tid']] for rn in rowsn])
allt = sorted({t for rn in rowsn for t in meta[rn]['types']})


def clf():
    return make_pipeline(StandardScaler(with_mean=False), LogisticRegression(max_iter=1000, class_weight='balanced'))


cv = {}
for t in allt:
    y = np.array([1 if t in meta[rn]['types'] else 0 for rn in rowsn])
    if y.sum() < 5:
        continue
    proba = np.zeros(n)
    for tr, te in GroupKFold(n_splits=5).split(X, y, groups=groups):
        c = clf().fit(X[tr], y[tr])
        proba[te] = c.predict_proba(X[te])[:, 1]
    cv[t] = roc_auc_score(y, proba) if len(set(y)) > 1 else None

lomo = {}
for t in allt:
    y = np.array([1 if t in meta[rn]['types'] else 0 for rn in rowsn])
    if y.sum() < 10:
        continue
    aucs = []
    for m in sorted(set(models)):
        tr = models != m; te = models == m
        if len(set(y[te])) < 2:
            continue
        c = clf().fit(X[tr], y[tr])
        aucs.append(roc_auc_score(y[te], c.predict_proba(X[te])[:, 1]))
    lomo[t] = float(np.mean(aucs)) if aucs else None

with open(ART / 'prediction_auc.csv', 'w') as f:
    f.write('type,auc_grouped_cv,auc_cross_model,n_pos\n')
    for t in allt:
        npos = sum(1 for rn in rowsn if t in meta[rn]['types'])
        f.write(f'"{t}",{cv.get(t) or ""},{lomo.get(t) or ""},{npos}\n')

gv = [v for v in cv.values() if v]
lv = [v for v in lomo.values() if v]
print(f'\nA) Prever TIPO a partir de features Sonar:')
print(f'   AUC médio CV agrupado (tarefa) = {np.mean(gv):.3f}  |  cross-model = {np.mean(lv):.3f}  (baseline 0.500, gate 0.600)')

# sanity: pass/fail
mp = {json.loads(l)['row_number']: bool((json.loads(l).get('evaluation_result') or {}).get('is_pass'))
      for l in open(LAB / 'metadata.jsonl', encoding='utf-8') if l.strip()}
y2 = np.array([1 if mp[rn] else 0 for rn in rowsn])
proba = np.zeros(n)
for tr, te in GroupKFold(n_splits=5).split(X, y2, groups=groups):
    proba[te] = clf().fit(X[tr], y2[tr]).predict_proba(X[te])[:, 1]
print(f'   sanidade: prever pass/fail com features Sonar = AUC {roc_auc_score(y2, proba):.3f}')

# ---------- figura ----------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.8), gridspec_kw={'width_ratios': [1, 1.35]})
cs = ['#12457f', '#4a90d9', '#e07b00', '#8a8a8a']
vals = [p[c] * 100 for c in CELLS]
err_lo = [(p[c] - ci[c][0]) * 100 for c in CELLS]
err_hi = [(ci[c][1] - p[c]) * 100 for c in CELLS]
ax[0].bar([LBL[c] for c in CELLS], vals, color=cs, yerr=[err_lo, err_hi], capsize=4)
for k, c in enumerate(CELLS):
    ax[0].text(k, vals[k] + err_hi[k] + 2.5, f'{vals[k]:.1f}%', ha='center', fontsize=9)
ax[0].set_ylim(0, max(v + e for v, e in zip(vals, err_hi)) * 1.20)
ax[0].set_ylabel('% das implementações anotadas')
ax[0].set_title('Cobertura dos gates (teste × SonarQube)')
ax[0].grid(axis='y', alpha=0.25)
plt.setp(ax[0].get_xticklabels(), rotation=15, ha='right')

types = sorted(allt, key=lambda t: -sum(1 for r in rows.values() if t in r['types']))
labs, sem_issue = [], []
for t in types:
    sub = [r for r in rows.values() if t in r['types']]
    labs.append(f'{t}  (n={len(sub)}{"*" if len(sub) < 10 else ""})')
    sem_issue.append(sum(1 for r in sub if r['cell'] in ('test_only', 'none')) / len(sub) * 100)
ax[1].barh(range(len(types)), sem_issue, color='#e07b00')
ax[1].set_yticks(range(len(types)))
ax[1].set_yticklabels(labs, fontsize=7)
for k, v in enumerate(sem_issue):
    ax[1].text(v + 1.5, k, f'{v:.1f}%', va='center', fontsize=7.5)
ax[1].invert_yaxis()
ax[1].set_xlim(0, 112)
ax[1].set_xlabel('% sem qualquer issue Sonar')
ax[1].set_title('Escapa da análise estática, por tipo de alucinação')
ax[1].grid(axis='x', alpha=0.25)
fig.tight_layout()
fig.text(0.5, -0.02, '* n < 10: estimativa frágil (poucos casos)', ha='center', fontsize=7, color='#555555')
fig.savefig(ROOT / 'docs' / 'fig-cobertura-gates.png', dpi=300, bbox_inches='tight')
print('\nSalvos: coverage_gates.csv, prediction_auc.csv, docs/fig-cobertura-gates.png')
