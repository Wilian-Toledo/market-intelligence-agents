# Arquitetura de Market Intelligence Agents

## Fluxo desejado
Power BI (MCP preexistente) → Inventário confiável → Diagnóstico quantitativo → Investigação de hipóteses → Priorização econômico-comercial → Revisão crítica → Storytelling executivo/OnePage.

## Papéis
- **MCP:** acesso de leitura ao modelo Power BI já aberto. Fora do plugin; não reconfigurar.
- **Agentes:** tarefas cognitivas especializadas e delimitadas.
- **Skills:** metodologia analítica, regras de cálculo, verificações e critérios de aceitação.
- **Contratos:** outputs estruturados e rastreabilidade de fonte, indicador, período e filtro.
- **Orquestração:** Claude Code, evitando agentes redundantes.

## Guardrails
1. Dados específicos e relatórios ficam exclusivamente em diretórios locais autorizados.
2. Nenhum número sem indicador, período, população, unidade, fonte, filtros e evidência.
3. Diferenciar fatos, hipóteses, causas validadas e recomendações.
4. Não atribuir causa sem evidência nem propor crescimento desconsiderando sinistralidade, custo e margem.
5. Só realizar projeções após avaliar histórico, sazonalidade, backtesting e incerteza.
6. Perspectivas de diretoria, gerência e coordenação serão skill, não agentes redundantes.

## Módulos
- **Implementado:** `model-cartographer` (mapa semântico).
- **Planejados:** `market-diagnostician`, `hypothesis-investigator`, `opportunity-strategist`, `challenge-reviewer`, `executive-storyteller`.

Adicionaremos cada módulo somente após validar a qualidade da etapa anterior.
