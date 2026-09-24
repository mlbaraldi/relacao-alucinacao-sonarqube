# Mapeamento SonarQube x taxonomia de alucinações

## Escopo

- Respostas materializadas: **1134**.
- Respostas com anotação manual do paper: **1134** (100.0%).
- Issues retornadas pelo SonarQube: **691**, em **369** respostas.
- Arquivos não parseados pelo analisador: **43**.
- O scan foi executado no SonarQube 10.0.0 com os perfis padrão para Java e Python.

## Como ler o mapeamento

Cada issue foi ligada à resposta por `component`/arquivo. Em seguida, recebeu todos os tipos manuais anotados naquela resposta; uma resposta pode ter mais de um tipo. Isso é uma associação observacional, não uma classificação nova feita pelo SonarQube.

`candidate_paper_type` em `mapped_issues.json` é apenas uma aproximação baseada na mensagem/regra: `direct/proxy` para variáveis indefinidas ou código não utilizado, `quality-only` para complexidade/manutenibilidade e `not-directly-mappable` nos demais casos.

## Cobertura por tipo do paper

| Tipo | Respostas rotuladas | Com issue Sonar | Cobertura | Issues Sonar |
| --- | --- | --- | --- | --- |
| Behavior Conflicting | 420 | 112 | 26.7% | 154 |
| Data Conflicting | 50 | 6 | 12.0% | 13 |
| Undefined Variables | 200 | 86 | 43.0% | 171 |
| Useless Statements (executed without effect) | 71 | 33 | 46.5% | 64 |
| Useless Statements (unexecuted) | 7 | 3 | 42.9% | 3 |
| Inconsistent Libraries | 2 | 0 | 0.0% | 0 |
| Fragmented Logics | 21 | 2 | 9.5% | 3 |
| Library/Project | 309 | 110 | 35.6% | 261 |
| Algorithm | 60 | 31 | 51.7% | 52 |
| Computer Theory | 27 | 9 | 33.3% | 15 |
| Common Sense | 3 | 3 | 100.0% | 6 |
| Mathematics & Natural Science | 17 | 2 | 11.8% | 2 |

## Regras mais associadas a tipos manuais

| Regra Sonar | Tipo do paper | Issues |
| --- | --- | --- |
| java:S1854 | Library/Project | 164 |
| java:S1854 | Undefined Variables | 132 |
| java:S1854 | Behavior Conflicting | 67 |
| java:S1854 | Useless Statements (executed without effect) | 42 |
| java:S1854 | Algorithm | 24 |
| python:S1172 | Library/Project | 18 |
| java:S1144 | Library/Project | 15 |
| python:S1172 | Behavior Conflicting | 15 |
| python:S1854 | Library/Project | 10 |
| python:S3776 | Library/Project | 9 |
| java:S1144 | Undefined Variables | 8 |
| java:S106 | Useless Statements (executed without effect) | 7 |
| python:S1542 | Behavior Conflicting | 7 |
| python:S117 | Behavior Conflicting | 7 |
| java:S1168 | Behavior Conflicting | 6 |
| java:S3776 | Library/Project | 6 |
| python:S1172 | Algorithm | 6 |
| java:S1172 | Undefined Variables | 5 |
| java:S1144 | Behavior Conflicting | 5 |
| java:S3012 | Behavior Conflicting | 5 |

## Volume por dataset e modelo

| Dataset | Modelo | Issues |
| --- | --- | --- |
| CEJava | codellama-7b | 104 |
| CEJava | deepseek-coder-1.3b | 109 |
| CEJava | deepseek-coder-7b | 73 |
| CEJava | deepseek-r1 | 170 |
| CEJava | gpt-4 | 91 |
| CEPython | codellama-7b | 36 |
| CEPython | deepseek-coder-1.3b | 21 |
| CEPython | deepseek-coder-7b | 19 |
| CEPython | deepseek-r1 | 28 |
| CEPython | gpt-4 | 11 |
| HumanEval | codellama-7b | 14 |
| HumanEval | deepseek-coder-1.3b | 8 |
| HumanEval | deepseek-coder-7b | 5 |
| HumanEval | gpt-4 | 2 |

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

