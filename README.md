# Market Intelligence Agents

Toolkit público de **agentes e skills para Claude Code**, com especialistas reutilizáveis em governança de KPIs e diagnósticos de desempenho. Cada projeto fornece seu **contexto local**: métricas, definições, recortes, evidências e perguntas de negócio. As skills não contêm nomes de empresas, medidas proprietárias nem limiares específicos.

## v0.3.0 — módulos disponíveis
1. `model-cartographer` + `/mapear-modelo`: inventário e auditoria técnica de modelo semântico Power BI via MCP **já existente**.
2. `semantic-validator` + `/validar-indicadores`: contratos de KPIs e classificação de confiabilidade.
3. **Novo:** `market-diagnostician` + `performance-diagnostics` + `/diagnosticar-desempenho`: análise de crescimento, desvios, recortes, comparações coerentes e **rascunho exploratório de OnePage**.

> Com **zero indicadores aprovados**, o diagnóstico é obrigatoriamente **exploratório**, com evidências e ressalvas. Não equivale a recomendação executiva nem prova retorno financeiro.

## Atualização no Claude Code sem PowerShell
Se a versão 0.2 já foi instalada, use o **prompt pronto** em [docs/upgrade-v0.3.md](docs/upgrade-v0.3.md). Ele copia somente o agente e as duas skills novas para `.claude/`, preservando MCP, configurações e relatórios anteriores. Após reiniciar a sessão (se necessário), execute `/diagnosticar-desempenho`.

Se ainda não instalou nenhuma versão, veja [docs/installation-without-plugin.md](docs/installation-without-plugin.md). Você pode usar `git clone` em pasta temporária ou baixar o ZIP no navegador. Não precisa executar PowerShell.

## Estrutura
```text
plugins/market-intelligence/
  agents/
    model-cartographer.md
    market-diagnostician.md
  skills/
    mapear-modelo/SKILL.md
    powerbi-semantic-audit/SKILL.md
    validar-indicadores/SKILL.md
    semantic-validator/{SKILL.md,references/,scripts/,examples/}
    diagnosticar-desempenho/SKILL.md
    performance-diagnostics/{SKILL.md,references/,scripts/,examples/}
tests/
docs/
```

## Política de dados e confiabilidade
- **Nenhum dado real, DAX interno, PBIX, credencial, metadado proprietário ou relatório local** deve ser enviado ao GitHub público.
- Cada achado referencia o ID de KPI, janela, recorte, evidência e limitações, permitindo reanálise após mudança de regras.
- KPIs `rejected`/`blocked` não podem fundamentar achados; `restricted` exigem recorte comprovadamente compatível.
- Projeções, explicações causais e priorização de investimentos são módulos posteriores, não incluídos na v0.3.
- O toolkit nunca altera PBIX, medidas, fontes, RLS, refresh ou configuração do MCP.

## Estado de validação
Os **arquivos publicados** são conferidos no GitHub. Há testes sintéticos de contratos; o novo agente deve ser testado no Claude Code local sobre dados autorizados antes de qualquer utilização real.
