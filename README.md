# Análise de alucinações de código com SonarQube

Este repositório reúne respostas de modelos de linguagem materializadas como arquivos Java e Python, metadados por resposta, resultados de uma análise estática do SonarQube e agregações que relacionam as issues encontradas com os rótulos manuais de alucinação do paper.

A análise inicial e a taxonomia de alucinações utilizadas neste trabalho vêm do repositório [`Lorien1128/code_hallucination`](https://github.com/Lorien1128/code_hallucination/tree/master). Este repositório específico contém a análise complementar com SonarQube e o cruzamento das issues com os rótulos dessa taxonomia.

O SonarQube aponta problemas de código (por exemplo, bugs e code smells); ele não decide se a resposta está correta em relação ao enunciado. O cruzamento com os tipos do paper é observacional: uma issue encontrada em um arquivo recebe os tipos manuais associados àquela resposta. Portanto, associação não significa que o SonarQube detectou ou causou a alucinação.

## Conteúdo

- `src/`: respostas de código separadas por dataset e modelo (`src/<dataset>/<modelo>/`). Inclui `CEJava`, `CEPython` e `HumanEval`.
- `metadata.jsonl`: um registro JSON por resposta, com identificador, dataset, modelo, arquivo de origem, resultado da avaliação e anotações. `source_file` liga o registro ao arquivo em `src/`; `code_labels` contém os tipos anotados manualmente.
- `sonar-project.properties`: configuração do projeto enviada ao scanner. A análise usa `src` como fonte e exclui quatro regras Java ligadas ao andaime sintético: `S101`, `S1118`, `S1220` e `S1598`.
- `sonar_issues.json`: issues obtidas do SonarQube, antes do mapeamento aos metadados.
- `mapped_issues.json`: as mesmas issues enriquecidas com dataset, modelo, número da resposta, tipos do paper e informações de avaliação.
- `summary.json`: contagens resumidas usadas na análise.
- `report.md`: relatório tabular e discussão dos resultados desta execução.
- `sonar_scan.log`: log do scanner, útil para conferir a versão usada e problemas de parsing.
- Os quatro CSVs descritos abaixo: agregações para análise em planilha ou scripts de análise.

O conjunto tem 3.120 respostas materializadas nos metadados: 1.150 de `CEJava`, 1.150 de `CEPython` e 820 de `HumanEval`, distribuídas igualmente entre cinco modelos. O relatório desta execução registra 1.426 issues em 838 arquivos e 1.134 respostas com rótulo manual.

## CSVs gerados

Os CSVs usam cabeçalho na primeira linha, codificação UTF-8 e vírgula como separador. Em geral, `paper_hallucination_type`/`paper_type` vazio ou `<unlabeled>` significa que a resposta não tinha tipo manual associado; não significa “sem alucinação”. Uma resposta pode ter mais de um tipo manual, então seus issues podem aparecer em mais de uma linha/tipo. Totais por tipo não devem ser somados como se fossem categorias exclusivas.

### `sonar_rule_summary.csv`

Distribuição de todas as issues por regra Sonar e tipo de issue.

| Coluna | Significado |
| --- | --- |
| `sonar_rule` | Chave da regra, como `java:S1854` ou `python:S1172`. |
| `sonar_type` | Categoria atribuída pelo SonarQube, por exemplo `BUG` ou `CODE_SMELL`. |
| `issues` | Número de issues dessa regra e categoria. |

### `sonar_rule_by_paper_type.csv`

Contagem de issues por regra Sonar e rótulo manual do paper. `<unlabeled>` agrupa issues cujo arquivo não tem rótulo manual correspondente nos metadados.

| Coluna | Significado |
| --- | --- |
| `sonar_rule` | Chave da regra Sonar. |
| `paper_type` | Tipo manual associado à resposta ou `<unlabeled>`. |
| `issues` | Número de issues na combinação. |

### `sonar_type_x_paper_hallucination_coverage.csv`

Cruzamento agregado entre a categoria geral da issue (`BUG`/`CODE_SMELL`) e cada tipo manual do paper. A cobertura de tipo do paper mede a fração das respostas anotadas daquele tipo que tiveram ao menos uma issue Sonar associada.

| Coluna | Significado |
| --- | --- |
| `sonar_issue_type` | Categoria geral Sonar, como `BUG` ou `CODE_SMELL`. |
| `paper_hallucination_type` | Tipo manual do paper. |
| `relation_issue_count` | Número de issues na combinação de categoria Sonar e tipo manual. |
| `sonar_issue_type_total` | Total de issues daquela categoria Sonar. |
| `relation_coverage_of_sonar_type_pct` | Percentual das issues da categoria Sonar que estão nessa combinação. |
| `relation_coverage_of_all_sonar_issues_pct` | Percentual de todas as issues Sonar nessa combinação. |
| `responses_with_relation` | Número de respostas distintas com essa combinação. |
| `paper_labeled_responses` | Número de respostas anotadas com esse tipo manual. |
| `paper_type_coverage_pct` | Percentual de respostas daquele tipo que tiveram uma ou mais issues Sonar associadas. |

### `sonar_issue_type_x_paper_hallucination_coverage.csv`

Mesmo cruzamento de cobertura, agora detalhado por regra Sonar. `sonar_rule_total_issues` é o denominador da cobertura da regra; as demais colunas de cobertura e contagem seguem a interpretação da tabela anterior.

| Coluna | Significado |
| --- | --- |
| `sonar_rule` | Chave da regra Sonar. |
| `sonar_issue_type` | Categoria Sonar da issue (`BUG`, `CODE_SMELL` etc.). |
| `sonar_severity` | Severidade informada pelo SonarQube, como `MAJOR`. |
| `paper_hallucination_type` | Tipo manual do paper associado. |
| `relation_issue_count` | Issues dessa regra associadas ao tipo manual. |
| `sonar_rule_total_issues` | Total de issues da regra, usado como denominador da cobertura da regra. |
| `relation_coverage_of_sonar_rule_pct` | Percentual das issues da regra nessa combinação. |
| `relation_coverage_of_all_sonar_issues_pct` | Percentual de todas as issues nessa combinação. |
| `responses_with_relation` | Respostas distintas com essa combinação. |
| `paper_labeled_responses` | Respostas anotadas com o tipo manual. |
| `paper_type_coverage_pct` | Percentual das respostas desse tipo com uma ou mais issues associadas. |

## Executar uma nova análise SonarQube

O log incluído registra SonarQube **10.0.0**, SonarScanner **5.0.1** e Java **17**. Para reproduzir a configuração deste resultado, use SonarQube 10.0 Community e mantenha os perfis Java/Python equivalentes aos perfis padrão (Sonar way) usados naquela execução. Versões mais novas de servidor ou analisadores podem alterar as regras e os resultados.

### 1. Subir o servidor

É necessário ter Docker instalado. Em Linux, o SonarQube também requer que o host tenha `vm.max_map_count` configurado para pelo menos `262144` (consulte a documentação da sua distribuição para persistir essa configuração).

```sh
docker run -d --name sonarqube \
  -p 9000:9000 \
  sonarqube:10.0-community
```

Espere o servidor ficar disponível em <http://localhost:9000>. Entre com a conta inicial `admin` / `admin` e troque a senha quando solicitado. Crie um token de análise na interface do SonarQube e guarde-o em uma variável de ambiente:

```sh
export SONAR_TOKEN='token-criado-no-sonarqube'
```

### 2. Rodar o scanner

Instale o SonarScanner CLI 5.0.1 e Java 17, e execute os comandos a partir deste diretório, onde estão `sonar-project.properties` e `src/`:

```sh
sonar-scanner \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token="$SONAR_TOKEN"
```

O scanner envia a análise ao servidor. Acompanhe o resultado no projeto `code-hallucination-result-v2` em <http://localhost:9000>. O diretório local `.scannerwork/` é temporário e contém estado/metadados de execução; o log completo pode ser salvo assim:

```sh
sonar-scanner \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token="$SONAR_TOKEN" 2>&1 | tee sonar_scan.log
```

Ao terminar, pare e remova o container quando não precisar mais dele:

```sh
docker stop sonarqube
docker rm sonarqube
```

### 3. Exportar issues e reconstruir os CSVs

O scanner não grava `sonar_issues.json`, `mapped_issues.json` nem os CSVs diretamente. As issues são consultadas na API Web do SonarQube (`api/issues/search`, paginada) e depois ligadas a `metadata.jsonl` pelo caminho do arquivo. O JSON bruto e os CSVs deste diretório são artefatos pós-processados.

Este diretório não contém os scripts que fizeram essa extração e agregação. Assim, os arquivos existentes permitem inspecionar e analisar o resultado, mas o passo de reconstrução dos JSONs/CSVs não é reproduzível apenas com o conteúdo versionado aqui. Depois de rodar o scan, a exportação pode ser feita pela API do servidor com o token de análise e a chave `code-hallucination-result-v2`; para obter os mesmos CSVs com consistência, é necessário recuperar ou adicionar ao projeto o script de exportação/mapeamento que define a paginação, associação de metadados, deduplicação e fórmulas de cobertura.

## Limitações da análise

- SonarQube detecta padrões estáticos de bugs e qualidade. Não avalia se o programa cumpre o enunciado ou se usa corretamente o contexto do projeto.
- O campo `candidate_paper_type` em `mapped_issues.json` é uma heurística baseada na regra/mensagem Sonar (`direct/proxy`, `quality-only` ou `not-directly-mappable`), não um rótulo validado manualmente.
- Nesta execução, o relatório registra 111 arquivos Java/Python que não foram parseados. Eles não podem contribuir com issues semânticas; consulte `sonar_scan.log` para as mensagens do analisador.
- Contextos e dependências originais dos projetos CoderEval não foram fornecidos ao scan; também não foi fornecida cobertura de testes. Os resultados Java podem, portanto, ser menos precisos.
- As contagens deste README descrevem os artefatos já incluídos. Uma nova análise pode produzir resultados diferentes se os arquivos, perfis, regras ou versões mudarem.
