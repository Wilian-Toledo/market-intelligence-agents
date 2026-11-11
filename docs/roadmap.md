# Roadmap — Market Intelligence Agents

| Etapa | Estado no GitHub |
|---|---|
| 1. Mapeamento semântico (`model-cartographer`) | Implementado |
| 2. Contratos e validação (`semantic-validator`) | Implementado |
| 3. Diagnóstico (`market-diagnostician`) | Implementado |
| 4. Investigação (`hypothesis-investigator`) | Implementado v1.0 |
| 5. Priorização condicional (`opportunity-strategist`) | Implementado v1.0 |
| 6. Revisão crítica (`challenge-reviewer`) | Implementado v1.0 |
| 7. Storytelling visual (`executive-storyteller`) | Implementado v1.0 |
| 8. Orquestração integrada (`/gerar-onepage`) | Implementado v1.0 |

**Status real:** MVP implementado no repositório e ainda sujeito a validação end-to-end em Claude Code + Power BI. Nem os KPIs locais nem o uso executivo estão aprovados por esse estado.

## Depois do MVP
Ajustar narrativa, formatos, avaliações e projeções somente quando os dados e objetivos permitirem. Evitar reabrir etapas anteriores sem necessidade.

## Regra de portabilidade
O framework público nunca conhece nomes de organizações, tabelas, medidas, fórmulas proprietárias ou thresholds. Contratos, dicionários, perguntas de negócio, KPIs e relatórios ficam no projeto local e podem ser substituídos sem reescrever as skills.
