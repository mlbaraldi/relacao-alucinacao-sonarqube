# Mapeamento SonarQube x taxonomia de alucinações

## Escopo

- Respostas materializadas: **3120**.
- Respostas com anotação manual do paper: **1134** (36.3%).
- Issues retornadas pelo SonarQube: **1426**, em **838** respostas.
- Arquivos não parseados pelo analisador: **111**.
- O scan foi executado no SonarQube 10.0.0 com os perfis padrão para Java e Python.

## Como ler o mapeamento

Cada issue foi ligada à resposta por `component`/arquivo. Em seguida, recebeu todos os tipos manuais anotados naquela resposta; uma resposta pode ter mais de um tipo. Isso é uma associação observacional, não uma classificação nova feita pelo SonarQube.

`candidate_paper_type` em `mapped_issues.json` é apenas uma aproximação baseada na mensagem/regra: `direct/proxy` para variáveis indefinidas ou código não utilizado, `quality-only` para complexidade/manutenibilidade e `not-directly-mappable` nos demais casos.

## Cobertura por tipo do paper

| Tipo | Respostas rotuladas | Com issue Sonar | Cobertura | Issues Sonar |
| --- | --- | --- | --- | --- |
| Behavior Conflicting | 420 | 116 | 27.6% | 160 |
| Data Conflicting | 50 | 6 | 12.0% | 13 |
| Undefined Variables | 200 | 82 | 41.0% | 155 |
| Useless Statements (executed without effect) | 71 | 35 | 49.3% | 65 |
| Useless Statements (unexecuted) | 7 | 3 | 42.9% | 3 |
| Inconsistent Libraries | 2 | 0 | 0.0% | 0 |
| Fragmented Logics | 21 | 2 | 9.5% | 3 |
| Library/Project | 309 | 120 | 38.8% | 266 |
| Algorithm | 60 | 32 | 53.3% | 50 |
| Computer Theory | 27 | 8 | 29.6% | 13 |
| Common Sense | 3 | 1 | 33.3% | 3 |
| Mathematics & Natural Science | 17 | 2 | 11.8% | 2 |

## Regras mais associadas a tipos manuais

| Regra Sonar | Tipo do paper | Issues |
| --- | --- | --- |
| java:S1854 | Library/Project | 160 |
| java:S1854 | Undefined Variables | 114 |
| java:S1854 | Behavior Conflicting | 70 |
| java:S1854 | Useless Statements (executed without effect) | 40 |
| java:S1854 | Algorithm | 20 |
| python:S1172 | Library/Project | 18 |
| java:S1144 | Library/Project | 15 |
| python:S1172 | Behavior Conflicting | 15 |
| java:S1144 | Undefined Variables | 14 |
| python:S1854 | Library/Project | 10 |
| python:S3776 | Library/Project | 9 |
| java:S1168 | Behavior Conflicting | 8 |
| java:S1144 | Behavior Conflicting | 7 |
| java:S106 | Useless Statements (executed without effect) | 7 |
| python:S1542 | Behavior Conflicting | 7 |
| python:S117 | Behavior Conflicting | 7 |
| java:S1172 | Undefined Variables | 6 |
| java:S3776 | Library/Project | 6 |
| python:S1172 | Algorithm | 6 |
| java:S112 | Library/Project | 5 |

## Volume por dataset e modelo

| Dataset | Modelo | Issues |
| --- | --- | --- |
| CEJava | codellama-7b | 180 |
| CEJava | deepseek-coder-1.3b | 167 |
| CEJava | deepseek-coder-7b | 157 |
| CEJava | deepseek-r1 | 298 |
| CEJava | gpt-4 | 200 |
| CEPython | codellama-7b | 75 |
| CEPython | deepseek-coder-1.3b | 63 |
| CEPython | deepseek-coder-7b | 54 |
| CEPython | deepseek-r1 | 79 |
| CEPython | gpt-4 | 46 |
| HumanEval | codellama-7b | 25 |
| HumanEval | deepseek-coder-1.3b | 13 |
| HumanEval | deepseek-coder-7b | 12 |
| HumanEval | deepseek-r1 | 38 |
| HumanEval | gpt-4 | 19 |

## Limitações

- SonarQube detecta bugs, code smells e padrões de qualidade; não determina sozinho conflito com requisito, conhecimento de projeto, algoritmo, matemática ou senso comum.
- Java foi envolvido em classes sintéticas e Python HumanEval recebeu a assinatura do `prompt`; as regras originadas somente desse andaime foram excluídas (`S101`, `S1118`, `S1220`, `S1598`).
- Não foram fornecidas dependências/classes dos projetos CoderEval nem cobertura de testes ao SonarQube; os resultados Java podem ser menos precisos e não substituem a avaliação funcional já presente no JSONL.
- Arquivos não parseados permanecem no denominador do experimento, mas não podem gerar issues semânticas. Para uma análise mais forte, seria necessário separar respostas sintaticamente inválidas e fornecer os contextos/dependências originais.

## Artefatos

- `sonar_issues.json`: retorno bruto paginado da API do SonarQube.
- `mapped_issues.json`: issues com modelo, dataset e tipos do paper.
- `sonar_rule_by_paper_type.csv`: cruzamento regra x tipo.
- `sonar_rule_summary.csv`: distribuição geral por regra.
- `sonar_type_x_paper_hallucination_coverage.csv`: cruzamento agregado `BUG`/`CODE_SMELL` x tipo do paper, com coberturas.
- `sonar_issue_type_x_paper_hallucination_coverage.csv`: cruzamento detalhado por regra Sonar x tipo do paper.

