# Atualização v1.0 → v1.1 — OnePage para notebook

## Arquivos que mudaram
**Agentes** (origem `plugins/market-intelligence/agents/` → destino `.claude/agents/`):
- `opportunity-strategist.md`
- `executive-storyteller.md`
- `challenge-reviewer.md`

**Skills** (origem `plugins/market-intelligence/skills/` → destino `.claude/skills/`):
- `action-prioritization/SKILL.md`
- `executive-storytelling/SKILL.md`
- `executive-storytelling/assets/onepage-template.html`
- `evidence-review/SKILL.md`
- `gerar-onepage/SKILL.md`

Todo o resto — MCP, PBIX, `reports/`, demais especialistas, contratos e settings — **permanece igual**.

## Prompt curto para colar no Claude Code
> Atualize minhas skills e agentes do toolkit https://github.com/Wilian-Toledo/market-intelligence-agents para v1.1. Leia `docs/upgrade-v1.1.md` e copie apenas os arquivos alterados para `.claude/`, conferindo conflitos e fazendo backup local antes de substituir. Use git clone temporário ou ZIP, sem PowerShell. Preserve MCP, PBIX, configurações e `reports/`; não execute consultas, commits ou pushes. Depois confirme a atualização.

## Rodar
Em sessão local nova do Claude Code:
```text
/gerar-onepage
```
A OnePage será uma página **web para notebook**, não A4. O comando deverá reusar as análises locais e recriar somente o HTML/Markdown e etapas derivadas necessárias.

## Segurança
Nada de dados reais ou relatórios enviados ao GitHub público. Não tente contornar bloqueios corporativos; se Git estiver indisponível, use ZIP autorizado. Não publicar o HTML ou compartilhá-lo sem permissão.
