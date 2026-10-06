# Alucinações silenciosas — o que escapa aos testes e à análise estática (DRAFT)

> Nova hipótese (branch `alucinacoes-silenciosas`). Reaproveita o corpus e os artefatos existentes. Universo: **1.134 implementações com alucinação anotada** (todas têm ≥1 tipo; não há classe "sem alucinação"). Análise: `scripts/analise_silenciosas.py`. Dados: `sonarqube_labeled/artifacts/coverage_gates.csv` e `prediction_auc.csv`. Figura: `docs/fig-cobertura-gates.png`.

## RQ
Que fração e tipos de alucinações **sobrevivem** ao teste funcional e/ou ao scan estático (SonarQube), e como esse risco varia por modelo, benchmark e tipo?

Definições: **teste captura** = a implementação **falha** nos testes (`evaluation_result`); **estático captura** = a implementação tem ≥1 issue SonarQube. Quatro células mutuamente exclusivas.

## B) Matriz de cobertura (resultado central)

| Célula | % | IC 95% (bootstrap por tarefa) |
|---|---|---|
| teste **E** estático | 28,4% | [24,6; 32,3] |
| **só teste** | 65,9% | [61,9; 70,0] |
| **só estático** | 4,1% | [2,2; 6,3] |
| **escapa dos dois** | **1,6%** | [0,8; 2,4] |

**Leituras positivas:**
- **67,5%** das implementações alucinadas **não têm nenhum sinal Sonar** → análise estática é um gate **fraco** para alucinação (número acionável).
- **1,6%** passam no teste **e** não têm issue → "escapam de ambos os gates"; é o argumento para **detectores dedicados**.
- **5,7%** passam no teste funcional (escapam do gate funcional).

**Variação (importante):**
- Por **dataset**: HumanEval **0%** passa nos testes (os testes capturam 100%) e 84,5% sem issue; CEJava **10,6%** passa nos testes; CEPython 1,6%. → a força do gate funcional depende do **benchmark**.
- Por **tipo**: **Algorithm** é o mais "silencioso" (**33,3%** passam nos testes; 8,3% escapam de ambos). Data Conflicting (88%), Fragmented Logics (90,5%), Library/Project (64,4%) e Behavior Conflicting (73,3%) têm as maiores taxas de **escape do estático**.
- Por **modelo**: escapar de ambos varia de 0,7% (codellama-7b) a 2,8% (deepseek-r1); GPT-4 passa nos testes com mais frequência (7,4%).

## A) Piloto preditivo (gate não passou)

Features: 60 regras Sonar (binárias) + nº de issues + contagem de BUG/CODE_SMELL. Alvo: cada um dos 12 tipos (one-vs-rest).

| Cenário | AUC médio |
|---|---|
| CV agrupado por tarefa | **0,537** |
| Transferência cross-model | **0,593** |
| (sanidade) prever pass/fail | **0,725** |

- Prever **tipo** de alucinação com sinais Sonar fica **abaixo do gate 0,6** — coerente com o achado descritivo (associação tipo×regra fraca). **A vira análise secundária.**
- Como **sanidade**, as mesmas features preveem **pass/fail** com AUC **0,725** → há sinal estático útil para *falha funcional*, mas não para *tipo* de alucinação. Achado honesto e reaproveitável.

## Contribuição proposta
1. Primeiro mapa de **alucinações silenciosas** multi-modelo/benchmark (cobertura em camadas: teste × estático).
2. Evidência de que o SonarQube **não proxya tipo** de alucinação (o resultado negativo vira **motivação estrutural**).
3. Quantificação do "escapa dos dois gates" → justifica **detecção dedicada** de alucinações.

## Ressalvas
- "Teste captura" é **proxy**: falha funcional pode não corresponder à alucinação anotada.
- Viés do subconjunto anotado (1.134/3.120, 36,3%; 94% são falhas) — declarar.
- Dependência das 5 implementações/tarefa — ICs agrupados por tarefa (feito no bootstrap).
- Casos de n baixo (Common Sense n=3, Inconsistent Libraries n=2) — sinalizados como frágeis.
- Tipos em inglês (taxonomia original) × eixos em português — padronizar depois.
