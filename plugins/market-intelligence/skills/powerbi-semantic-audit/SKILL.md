---
name: powerbi-semantic-audit
description: "Procedimento de inventário e auditoria de modelos semânticos Power BI: DAX, dependências, granularidades, datas, comparabilidade e KPIs de inteligência de mercado."
---

# Power BI Semantic Audit — V0.1

O alvo é o **modelo autorizado já aberto no Power BI Desktop** acessível pelo MCP atual. Trabalhe estritamente em modo de descoberta e leitura.

## 0. Preparação
- Identifique as ferramentas de leitura do MCP de forma dinâmica; **não presuma nomes** ou altere configuração.
- Registre nome do modelo, data/hora, fonte da descoberta, escopo e eventual limitação de permissões.
- É proibido acessar ou exportar linhas individuais, dados pessoais, identificadores de clientes, apólices, sinistros individuais ou dados sigilosos.
- Grave os arquivos **somente localmente** em `reports/powerbi-model-audit/`, com proteção Git. Nunca faça push, commit ou upload.

## 1. Inventário
Conte e descreva em lotes:
- Tabelas visíveis e ocultas, colunas e tipos, calendários, hierarquias, tabelas calculadas e grupos de cálculo (se expostos).
- Relacionamentos: cardinalidade, direção, ativo/inativo e riscos de ambiguidade.
- Medidas: nomes, pastas, format strings, DAX, dependências, filtros implícitos e descrições, quando possível e permitido.
- RLS: presença e possíveis implicações, sem expor regras sensíveis.
- Fontes e datas de atualização quando expostas (não invente refresh).

Classifique tabelas como fato, dimensão, ponte, parâmetro, medidas, técnica ou indeterminada, sempre indicando confiança.

## 2. Contrato de KPIs
Para cada candidato a KPI, registre:
- Nome exato, tabela, definição funcional, expressão DAX/dependências (somente em relatório local autorizado), origem e status de interpretação.
- Unidade e tipo de cálculo: valor, %, variação em pontos percentuais, taxa, contagem, índice; agregabilidade.
- Temporalidade: competência, emissão, contabilização, referência, mês fechado, YTD, 12M; defasagens.
- Dimensões e população: seguradora, mercado, congêneres, produto, ramo, regional, UF, praça, canal; filtros e exclusões.
- Limitações de comparabilidade, risco de dupla contagem e validação pendente.

Procure **sem presumir que existem**: prêmio emitido, ganho, recebido, retido, produção, apólices, tamanho do mercado, market share, crescimento YoY, Δ pontos percentuais, sinistralidade, despesa, margem e índice combinado. Não trate esses conceitos como equivalentes.

## 3. Verificações seguras
Quando o MCP permitir consultas DAX **agregadas, pequenas e apenas leitura**, verifique:
1. Intervalos e última referência disponível por fonte.
2. Mesmo período, ramo, território, unidade e população no numerador e denominador do market share.
3. Zeros/nulos e sensibilidade a filtros e subtotais.
4. Possíveis duplicidades ou dupla contagem por granularidade, sem extrair linhas.
5. Crescimento interanual coerente com as bases, inclusive meses abertos/incompletos.
6. Alterações de mapeamento por região, produto ou concorrente.
7. Até três reconciliações agregadas (seguradora, mercado e razão) **somente quando as definições forem comparáveis**.

Registre cada teste como `verificado`, `reprovado` ou `não testado` (com motivo). Nunca classifique DAX como validado com negócio apenas porque sua sintaxe parece correta.

## 4. Dúvidas fundamentais
Liste até 12 perguntas por risco: qual ramo/produto, composição de mercado, definição regional, origem SUSEP ou fornecedor, data de fechamento/reprocessamentos, base de prêmio, métricas de sinistralidade, métricas econômicas e definição de esforço/retorno.

## 5. Entregáveis locais
Crie os seguintes Markdown com primeira linha **CONFIDENCIAL — material interno — não publicar no Git**:

- `00-resumo-executivo.md`: modelo/escopo, contagens reais, cobertura, 5 achados e capacidades analíticas.
- `01-inventario-modelo.md`: tabelas, dimensões, relações, estrutura, famílias e dependências.
- `02-dicionario-kpis.md`: ficha por KPI, fonte, definição, DAX/dependências, filtros, granularidade, status de validação.
- `03-riscos-validacoes.md`: testes, evidência agregada, falhas, comparabilidade, questões de segurança.
- `04-perguntas-e-proximos-passos.md`: perguntas de negócio priorizadas e backlog mínimo.

## Critérios de conclusão
- Inventário `completo` somente com contagens verificadas e escopo declarado; caso contrário `parcial` ou `bloqueado`.
- Status semântico `validado com negócio` exige confirmação humana ou fonte aprovada; senão `validado tecnicamente`, `inferido` ou `pendente`.
- Se souber os denominadores, reporte cobertura de tabelas, medidas, KPIs e testes. Se não souber, informe `cobertura indeterminada`.
- Não gere projeções ou recomendações nesta fase.
