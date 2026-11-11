---
name: performance-diagnostics
description: "Método genérico para diagnóstico de desempenho e mercado, com janelas comparáveis, contribuição por segmento, evidências, incertezas e achados rastreáveis. Não substitui contratos de KPI."
---

# Performance Diagnostics — método v0.3

## Objetivo
Responder: **o que mudou, em relação a qual referência, em quais recortes e com que evidências?** O método é portável: não fixe nomes de empresas, medidas, limiares, segmentos, datas ou regras setoriais.

## Pré-requisitos e seleção
1. Leia o contrato local produzido por `semantic-validator` (por padrão `reports/semantic-validation/01-catalogo-kpis.json`). Consulte a auditoria original apenas quando necessário.
2. Filtre `rejected` e `blocked`. Valide `allowed_uses` antes de incluir `approved`, `provisional` ou `restricted`.
3. Para `restricted`, confira **na prática** as restrições do recorte. Caso não seja possível, exclua esse KPI. Para `provisional`, adicione ressalva explícita de definição/origem não confirmada.
4. Não recalcule ou promova status unilateralmente. Se um teste contradisser o contrato, suspenda o uso do indicador e sinalize revisão sem alterar a fonte.
5. Sem `approved` relevantes para a pergunta, mantenha **modo exploratory** em toda a narrativa. Isto não impede um rascunho, mas impede afirmações executivas definitivas.

## Plano mínimo da análise
Escolha uma pergunta principal (ou use "Como evoluiu o desempenho observado e onde existem desvios relevantes?"). Registre:
- KPI e unidade; entidade-alvo, benchmark/mercado e denominador; população/segmento.
- Janela atual e de comparação, cobertura, data de fechamento e filtros. Identifique `yoy` e `sequential` separadamente.
- Qualidade dos dados, universo consistente, medidas válidas por recorte e histórico disponível.
- Dimensões pertinentes: produto, região, canal, competidor, segmento ou outras disponíveis.

**Não faça consultas ao modelo se as evidências locais bastarem.** Se faltar um agregado essencial e a ferramenta for permitida, faça uma consulta pequena e somente leitura. Evite varreduras gigantescas; não extraia registros individuais ou atributos pessoais.

## Checagens quantitativas
- Taxa de crescimento: `(atual / referência) - 1` quando referência não for zero; identifique divisão por zero e bases negativas.
- Mudança de share: `share_atual - share_anterior`, em **pontos percentuais** (pp), com denominador comparável e filtros isolados.
- Desvio relativo ao mercado: compare taxas **somente com janelas idênticas e mesmo universo**. Diferencie diferença em pp da distância percentual.
- Contribuição por segmento: `(valor_atual_segmento - valor_ref_segmento) / (valor_total_atual - valor_total_ref)` apenas se a soma de segmentos reconciliar o total e se o delta total não for zero. Se houver compensações entre ganhos e perdas, reporte também contribuições absolutas e ressalva interpretativa.
- Não apresente `gap`, `oportunidade potencial` ou `sinistralidade` como indicadores validados se o contrato local não permitir.
- Nunca rankeie "melhores para investir" sem custos, risco e viabilidade. Identificar maiores desvios **não é** priorizar investimentos.

## Critérios de achados
Produza **no máximo 5**, cada qual contendo:
1. `headline` factual e específico ao que é demonstrável.
2. `finding_type`: `observation` ou `hypothesis`. Hipótese nunca apresentada como fato.
3. `confidence`: `preliminary` (definição pendente) ou `validated` (somente dados aprovados e testes suficientes).
4. `kpi_ids` do contrato e `evidence_refs` locais; população, recorte, períodos e filtros na descrição.
5. `limitations`: o que não podemos concluir com os dados.
6. `next_check`: próximo teste específico que melhor distingue explicações concorrentes.

Um achado com KPI provisório ou restrito permanece `preliminary`. Nenhum achado pode depender de KPI reprovado ou bloqueado. Não afirmamos causa por simples correlação.

## Entregáveis
Em `reports/performance-diagnostics/`, fora do Git:
- `00-sintese-exploratoria.md`: questão, cobertura, regras metodológicas, 3–5 achados e decisões que ainda **não** podem ser tomadas.
- `01-achados.json`: contrato do arquivo em `references/findings.schema.json`.
- `02-evidencias-e-lacunas.md`: cálculo, filtros, recorte, fonte e testes faltantes por achado.
- `03-rascunho-onepage.md`: rascunho textual curto: título orientado a descoberta, situação observada, comparativos com ressalvas, sinais por recorte e **próximas verificações**. Coloque "EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA" se houver qualquer KPI não aprovado; não produza recomendações de investimento.

Quando disponível e permitido, execute o verificador local opcional da skill. Sem Python, confira manualmente seguindo o schema e diga que a checagem automatizada não foi executada.

## Condições de parada
Se não houver KPI utilizável, comparação temporal válida ou evidências suficientes para a pergunta, **não invente dados**: registre bloqueios e proponha uma única próxima verificação. Não volte a auditar o modelo inteiro nem faça análises fora do escopo.
