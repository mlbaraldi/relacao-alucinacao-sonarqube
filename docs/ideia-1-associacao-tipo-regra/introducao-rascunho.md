# Rascunho de Introdução — DRAFT (revisado pelo librarian em out/2026)

> Material de apoio para a Introdução (Overleaf). Referência-base: **Liu et al.** (`Lorien1128/code_hallucination` → IEEE TSE 2026). As citações usam as chaves de `referencias.bib` (já com autores/venue verificados). Esqueleto para adaptar, não texto final.

## Esqueleto (6 parágrafos)

**P1 — Contexto: geração de código por LLMs.**
Modelos de linguagem de grande porte tornaram-se infraestrutura da engenharia de software moderna, com destaque para a geração de código, integrados a assistentes adotados em escala industrial \cite{hou2024llm4se,ziegler2022copilot}. O desempenho em benchmarks consagrados — de funções isoladas no HumanEval \cite{chen2021humaneval} a tarefas pragmáticas dependentes de contexto no CoderEval \cite{yu2024codereval} — cresceu de forma sustentada. Essa adoção, porém, transfere para o código gerado um problema clássico: confiar em código não inspecionado é arriscado, e a confiança do desenvolvedor nem sempre corresponde à qualidade do que é gerado \cite{perry2023users,pearce2022asleep}.

**P2 — Alucinações em código.**
Herdado da geração de linguagem natural, o conceito de *alucinação* — saída plausível, porém inconsistente com a intenção do usuário, com o contexto ou com conhecimento factual \cite{ji2023survey} — foi transplantado para código por Liu et al., que analisaram 3.120 implementações geradas por cinco LLMs e propuseram uma taxonomia com 3 categorias primárias e 12 tipos específicos, com pacote de replicação público \cite{liu2024beyond}. Trabalhos subsequentes propuseram benchmarks de detecção \cite{codemirage2024}, ampliaram a análise para geração em nível de repositório \cite{zhang2025practical} e consolidaram o campo em surveys \cite{lee2025survey}. Um ponto central e pouco explorado é que a alucinação não se manifesta apenas como erro funcional: ela degrada também legibilidade e eficiência \cite{liu2024beyond} — dimensões que a avaliação funcional ignora e a revisão manual raramente captura.

**P3 — Além da correção funcional: qualidade de código e análise estática.**
A análise estática consolidou-se como resposta industrial a esse risco: ferramentas baseadas em regras verificam bilhões de linhas em produção há duas décadas \cite{bessey2010few}. O SonarQube é uma das ferramentas de maior adoção, classificando violações (*issues*) por tipo e severidade e associando-as a dívida técnica \cite{sonarsource-docs,lenarduzzi2019techdebt}. A literatura empírica, contudo, mostra que a relação com defeitos reais é sutil e fortemente dependente da regra: regras rotuladas como "bug" raramente antecipam falhas \cite{lenarduzzi2020sonarrules}; o efeito agregado das issues sobre falhas e mudanças é significativo, porém pequeno \cite{lenarduzzi2020sonarissues}; e poucas regras carregam peso preditivo \cite{lomio2021faultprediction}. Para código gerado por IA, a evidência inicial é preocupante: quase metade dos programas de ChatGPT que passam nos testes apresenta issues de estilo e manutenibilidade detectáveis por análise estática \cite{liu2024refining}.

**P4 — Lacuna de pesquisa.**
As duas literaturas evoluíram isoladamente: as taxonomias de alucinação caracterizam *o que* está semanticamente errado no código gerado, enquanto a análise estática caracteriza *quais padrões sintáticos e estruturais* as regras capturam. Não está estabelecido se **tipos específicos de alucinação tendem a se manifestar junto com violações de regras específicas**. Além disso, avaliações funcionais (*pass/fail*) capturam apenas parte do problema: defeitos que não impedem a execução acumulam-se como issues de qualidade, e quase metade do código de LLM aprovado carrega issues de manutenibilidade \cite{liu2024refining}, sem que a literatura estabeleça se esses sinais se sobrepõem às alucinações anotadas.

**P5 — Este estudo.**
Materializamos as 3.120 implementações do pacote de replicação de Liu et al. — 1.150 de CEJava, 1.150 de CEPython e 820 de HumanEval, correspondentes a 624 tarefas geradas por cinco LLMs \cite{liu2024beyond,yu2024codereval,chen2021humaneval} — e as submetemos ao SonarQube 10.0 \cite{sonarsource-docs}, obtendo 1.426 issues em 838 arquivos sob 71 regras. A análise de associação é restrita ao subconjunto com anotação manual de alucinação (1.134 implementações), no qual 60 regras ocorrem: combinadas aos 12 tipos, geram 720 pares candidatos, dos quais **596 são avaliáveis** (288 com regras Java e 308 com regras Python). Como o desenho é um **estudo de caso exploratório**, a análise em dois níveis — implementação e tarefa — considera conjuntamente direção, magnitude (diferença de proporções e *odds ratio*) e suporte observacional de cada par, em vez de testes de significância, dado que as tabelas de contingência são esparsas.

**P6 — Contribuições e implicações.**
As contribuições são três: (i) o primeiro mapeamento em escala entre tipos de alucinação (taxonomia de 12 tipos) e regras do SonarQube, sobre 596 pares avaliáveis em dois níveis; (ii) um arcabouço exploratório para cruzar taxonomias qualitativas com saídas de análise estática sob esparsidade, reprodutível sobre pacotes de replicação públicos; e (iii) implicações práticas para desenvolvedores que usam LLMs — se sinais de análise estática funcionam (ou não) como *proxy* de alucinações específicas — e para fornecedores de ferramentas de qualidade. O restante do artigo: Seção 2 descreve o desenho; Seção 3 reporta a caracterização; Seção 4 discute achados, ameaças à validade e implicações.

## Gap — frases prontas

1. "Embora alucinações em código gerado por LLMs e regras de análise estática tenham sido estudadas isoladamente, a relação entre **tipos específicos** de alucinação e **regras específicas** — isto é, se um tipo de alucinação tende a se manifestar junto com certas violações — permanece inexplorada."
2. "Avaliações funcionais (*pass@1*/pass/fail) capturam apenas parte do problema: defeitos que não impedem a execução acumulam-se como issues de qualidade, e quase metade do código de LLM que passa nos testes carrega issues de manutenibilidade \cite{liu2024refining} — sem que a literatura estabeleça se esses sinais se sobrepõem às alucinações anotadas."
3. "A esparsidade das combinações tipo × regra (596 pares avaliáveis de 720 candidatos, com contagens baixas por célula) exige um desenho descritivo-exploratório que não dependa de testes de significância — um método que este trabalho formaliza em dois níveis de análise."

## Contribuição (1 frase)

> Este estudo fornece o primeiro mapeamento empírico entre a taxonomia de alucinações em código gerado por LLMs e as regras do SonarQube, com um método exploratório em dois níveis (implementação e tarefa) adaptado à esparsidade dos dados, sobre 1.134 implementações anotadas de um corpus público de 3.120.

## Incertezas remanescentes (do librarian)

- `zhang2025practical`: fascículo rotulado "ISSTA" (PACMSE 2(ISSTA), pp. 481–503); conferir nº de artigo na ACM DL se a disciplina exigir.
- `lee2025survey`: ainda preprint na verificação; conferir aceite posterior.
- `ji2023survey`: volume/páginas confirmados indiretamente; DOI não conferido.
- `lomio2021faultprediction`: possível versão publicada não localizada — verificar ou remover.
- `liu2024refining`: DOI/ano confirmados; nº de artigo/páginas não conferidos.
- Liu et al.: cite a versão TSE (DOI `10.1109/TSE.2026.3657432`); a IEEE Xplore bloqueou o fetch direto — conferir a página final na submissão.

## Notas / pendências
- Chaves renomeadas em relação ao rascunho anterior: `saarimaki2020sonarissues` → `lenarduzzi2020sonarissues`; `lenarduzzi2021faultprediction` → `lomio2021faultprediction` (autores corrigidos). Atualizar quaisquer `\cite{}` que ainda usem as chaves antigas.
- Novo: `ji2023survey`, `bessey2010few`, `liu2024refining`.
- Números alinhados ao `3-metodologia_v2.tex`: 1.134 anotadas, 60 regras (32 Java/28 Python), 720 candidatos, **596 avaliáveis** (288/308).
