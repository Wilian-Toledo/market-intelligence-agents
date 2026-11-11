# Roadmap — implementação incremental

| Etapa | Entrega | Estado |
|---|---|---|
| 0 | Repositório, organização de plugins e instalação alternativa | Disponível |
| 1 | Model Cartographer + mapeamento Power BI via MCP | Disponível; testado localmente pelo usuário, sem verificação remota |
| 1.5 | **Semantic Validator** + contrato genérico de KPIs + checagens | **v0.2 disponível; aguarda validação no projeto do usuário** |
| 2 | Market Diagnostician: evolução, participação, comparações, decomposição de desvios | Planejado |
| 3 | Investigação de hipóteses e evidências independentes | Planejado |
| 4 | Priorização: potencial, esforço, capacidade e riscos econômicos | Planejado |
| 5 | Revisão crítica, narrativa e OnePage por público gerencial | Planejado |

## Critério para iniciar diagnóstico
Não é necessário corrigir todas as medidas: basta **um subconjunto útil de indicadores tecnicamente coerentes**, com limites semânticos explícitos, e aprovação para uso exploratório. Indicadores provisórios não sustentam decisões definitivas.

## Princípio de portabilidade
Agentes e skills contêm método, jamais nomes de empresa, nomes de tabelas, medidas fixas, portas, paths corporativos ou thresholds proprietários. Contextos, objetivos, decisões de negócio e contratos preenchidos ficam no projeto autorizado, fora do Git.
