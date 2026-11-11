# Market Intelligence Agents

Kit de agentes e skills para Claude Code, focado em auditoria de modelos semânticos Power BI e inteligência de mercado baseada em evidências.

**Versão 0.1.0** — primeiro subagente: `model-cartographer`. O MCP do Power BI deve estar previamente configurado no projeto local; este repositório não instala, edita nem reconfigura MCP.

> **Segurança:** repositório público. Não publique dados, PBIX, credenciais, regras de negócios internas, relatórios ou metadados corporativos.

## Instalação recomendada (sem /plugin)

Execute no PowerShell, na pasta do seu projeto Claude Code:

```powershell
$dest = Join-Path $env:TEMP ('market-intelligence-' + [guid]::NewGuid().ToString('N')); git clone --depth 1 https://github.com/Wilian-Toledo/market-intelligence-agents.git $dest; if ($LASTEXITCODE -ne 0) { throw 'Falha ao clonar'; }; & (Join-Path $dest 'scripts/install-native.ps1') -ProjectPath (Get-Location).Path
```

Reinicie o Claude Code local, caso necessário, e use `/mapear-modelo`.

O instalador copia agentes/skills para `.claude/` do projeto atual, verifica conflitos e preserva as configurações existentes. Veja `docs/installation-without-plugin.md`.

## Estrutura

- `plugins/market-intelligence/agents/model-cartographer.md`: subagente de mapeamento.
- `plugins/market-intelligence/skills/mapear-modelo/SKILL.md`: comando de auditoria.
- `plugins/market-intelligence/skills/powerbi-semantic-audit/SKILL.md`: método.
- `scripts/install-native.ps1`: instalação em projeto existente.
- `docs/`: arquitetura, roteiro, segurança e instalação.
- `contracts/`: contrato de saída.
- `.claude-plugin/`: opção futura de distribuição via plugin.

Os demais agentes (diagnóstico, hipótese, oportunidade, priorização, revisão crítica e narrativa executiva) serão implementados e testados incrementalmente. Este projeto ainda não foi validado com PBIX real.

## Aviso

A conexão e o uso de IA sobre metadados empresariais exigem autorização de segurança e conformidade da organização. Artefatos locais de auditoria devem ficar em `reports/powerbi-model-audit/`, fora do versionamento.
