# Resultados exploratórios — pré-análise (DRAFT)

> Recomputação independente sobre o subconjunto anotado (`sonarqube_labeled/artifacts/`). O objetivo é caracterizar, de forma **descritiva**, a relação entre tipos de alucinação (taxonomia de Liu, 12 tipos) e regras do SonarQube (60 regras: 32 Java, 28 Python). Pares avaliáveis: **596** em ambos os níveis. Cada par vem com a tabela 2×2 completa em `sonarqube_labeled/artifacts/analysis_pairs_implementation.csv` e `analysis_pairs_task.csv`.

## Nível da implementação (1.134 anotadas; elegíveis 547 Java / 587 Python)

**Classificação estrutural dos 596 pares**

| Classe | Pares | % |
|---|---|---|
| Sem coocorrência ($a=0$) | 472 | 79,2% |
| Coocorrência completa | 83 | 13,9% |
| Coocorrência com célula zero | 41 | 6,9% |

Apenas **124 pares** têm alguma coocorrência ($a \ge 1$); **16** têm suporte observacional suficiente ($S \ge 10$ e $a \ge 5$).

**Pares destacáveis de maior $|\Delta|$** (todos com $\Delta \le 0{,}08$):

| Alucinação | Regra | a | nX | nY | Δ | OR |
|---|---|---|---|---|---|---|
| Useless Statements (executed) | java:S106 | 6 | 67 | 10 | +0,08 | 11,7 |
| Algorithm | java:S1854 | 17 | 41 | 197 | +0,06 | 1,28 |
| Library/Project | python:S3776 | 9 | 146 | 13 | +0,05 | 7,18 |
| Library/Project | java:S1144 | 15 | 163 | 32 | +0,05 | 2,19 |
| Library/Project | java:S1854 | 64 | 163 | 197 | +0,05 | 1,22 |
| Behavior Conflicting | java:S1168 | 6 | 129 | 10 | +0,04 | 5,05 |

**Dominância de `java:S1854`**: é a regra de 9 dos pares e concentra **215** das coocorrências (a próxima, `python:S1172`, tem 36). É uma regra genérica (variáveis/código sem uso) — a associação mecânica com qualquer tipo infla qualquer padrão.

## Estratificação por correção funcional (`evaluation_result`)

- **Estrato que falha** (1.069): 14 destacáveis; reproduz o padrão geral (inclusive Useless×S106, $a=6$).
- **Estrato que passa** (65): apenas **216 pares avaliáveis**, **199 sem coocorrência** e só **2 destacáveis**, ambos com `java:S1854` e em **direções opostas** (Algorithm×S1854 $\Delta=-0{,}16$; Behavior×S1854 $\Delta=+0{,}13$).

O único destaque do nível da implementação (Useless Statements×`java:S106`) **não aparece no estrato que passa**. Ou seja, os poucos sinais **não se sustentam** quando se controla a correção funcional (e o estrato "passa" é pequeno demais para conclusões).

## Contribuição por modelo (nos 8 pares destacáveis de maior $|\Delta|$)

Vários pares são **dominados por um único modelo**:

| Par | $a$ | Modelo dominante |
|---|---|---|
| Library/Project × python:S3776 | 9 | deepseek-r1: 8 |
| Library/Project × java:S1144 | 15 | deepseek-r1: 11 |
| Library/Project × java:S1854 | 64 | deepseek-r1: 27 |
| Useless (executed) × java:S1854 | 22 | gpt-4: 12 |
| Algorithm × java:S1854 | 17 | disperso (codellama 6, gpt-4 5) |

→ O **modelo é confundidor**: parte dos "padrões" reflete o estilo de um LLM, não o vínculo alucinação→regra.

## Nível da tarefa (433 tarefas; java 178 / python 255)

**Classificação**: 407 sem coocorrência (68,3%), 99 coocorrência completa, 90 com célula zero. Apenas **189 pares** com $a \ge 1$.

**Pares destacáveis de maior $|\Delta|$**

| Alucinação | Regra | a | nX | nY | Δ | OR |
|---|---|---|---|---|---|---|
| Undefined Variables | java:S1854 | 59 | 91 | 87 | +0,33 | 3,89 |
| Behavior Conflicting | java:S1854 | 41 | 64 | 87 | +0,24 | 2,64 |
| Undefined Variables | python:S1172 | 7 | 22 | 30 | +0,22 | 4,26 |
| Useless Statements (executed) | java:S1854 | 24 | 37 | 87 | +0,20 | 2,29 |
| Algorithm | java:S1854 | 12 | 19 | 87 | +0,16 | 1,92 |

As magnitudes de $\Delta$ são **maiores** que no nível da implementação — mas isso é **esperado pela agregação `any`** (que infla a coocorrência), não evidência mais forte. E, de novo, **`java:S1854` domina** (4 dos 5 primeiros pares).

## Leitura honesta

1. **Alucinação e regra do SonarQube quase não se sobrepõem.** ~79% (implementação) dos pares avaliáveis têm **zero** coocorrência. O SonarQube **não funciona como proxy geral** de tipos específicos de alucinação.
2. **Os poucos sinais são fracos e confundidos.** No nível da implementação, $|\Delta| \le 0{,}08$; quase tudo passa por `java:S1854` (regra genérica) e por um único modelo (`deepseek-r1`).
3. **Não há robustez à correção funcional.** O destaque principal desaparece no estrato "passa"; as associações com `java:S1854` chegam a inverter de sinal. O estrato "passa" (65) é pequeno demais.
4. **O nível da tarefa não fortalece a evidência** — apenas amplia $\Delta$ por construção.
5. **Conclusão compatível com a literatura**: regras de análise estática têm relação fraca e heterogênea com defeitos reais; aqui, também com tipos de alucinação. Achado modesto, porém **honesto e defensável** — e uma contribuição negativa útil ("não use regras Sonar como proxy de alucinação específica").

## Ressalvas
- Recomputação independente; deve ser confrontada com o pipeline da Priscila antes de virar resultado oficial.
- `nY` contado **dentro do conjunto elegível** (mesmo universo de `nX`), ao contrário da Tabela 1 original.
- Regras de andaime (`S101`, `S1118`, `S1220`, `S1598`) já excluídas; 111 arquivos não parseados permanecem no denominador.
