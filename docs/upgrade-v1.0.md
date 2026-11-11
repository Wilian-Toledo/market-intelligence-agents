# Atualização única v0.3 → v1.0 — sem PowerShell

## Instalar somente o que mudou
**Agentes novos** em `plugins/market-intelligence/agents/`:
- `hypothesis-investigator.md`
- `opportunity-strategist.md`
- `challenge-reviewer.md`
- `executive-storyteller.md`

**Skills novas (copiar pastas completas)** em `plugins/market-intelligence/skills/`:
- `hypothesis-analysis/`
- `action-prioritization/`
- `evidence-review/`
- `executive-storytelling/` (inclui `assets/onepage-template.html`)
- `gerar-onepage/`

Nada do que está instalado na v0.3 precisa ser substituído.

## Prompt único para Claude Code local
> Atualize este projeto para o Market Intelligence Agents v1.0 usando https://github.com/Wilian-Toledo/market-intelligence-agents . Confira a raiz do projeto. Clone o repositório para uma pasta temporária **fora do projeto** se `git` estiver permitido; alternativamente use o ZIP já baixado e extraído. Leia `docs/upgrade-v1.0.md`. Instale SOMENTE os quatro novos arquivos de agentes (`hypothesis-investigator.md`, `opportunity-strategist.md`, `challenge-reviewer.md`, `executive-storyteller.md`) em `.claude/agents/` e as cinco novas pastas completas de skills (`hypothesis-analysis`, `action-prioritization`, `evidence-review`, `executive-storytelling`, `gerar-onepage`) em `.claude/skills/`. Compare conflitos antes de copiar; não sobrescreva arquivos diferentes sem aprovação. Preserve todo o MCP existente, configurações, demais agentes/skills, PBIX e `reports/`. Não execute PowerShell, scripts, instalação de dependências, auditorias ou consultas DAX; não faça git commit/push. Confirme os nove componentes instalados e que `reports/` está no gitignore do projeto. Não execute `/gerar-onepage` automaticamente.

Depois, reinicie a sessão local caso necessário.

## Gerar o MVP (um comando)
```text
/gerar-onepage
```

O comando reaproveita `reports/powerbi-model-audit/`, `reports/semantic-validation/` e `reports/performance-diagnostics/` se estiverem adequados. Cria `reports/market-intelligence/onepage.html` e `onepage.md`, hipóteses, prioridades e revisão crítica. Não altera o PBIX.

## Resultado e feedback
Abra o HTML localmente no navegador. Só compartilhe com ferramentas externas um resumo **sanitizado e aprovado**, nunca medidas, extratos, dados pessoais, nomes corporativos, valores internos ou conteúdo completo.

## Caso não tenha v0.3 instalada
Siga `docs/installation-without-plugin.md` para copiar **todos** os agentes em `.claude/agents/` e **todas** as skills em `.claude/skills/`, sem PowerShell.
