# Instalação sem `/plugin` e sem PowerShell

Esta é a via recomendada quando o Claude Code roda em Windows com políticas corporativas que bloqueiam PowerShell, mas permitem acesso aos arquivos do projeto.

## Requisitos
- Claude Code local com acesso à pasta do projeto.
- Acesso ao GitHub pelo terminal **se permitido**; caso contrário, baixe o ZIP pelo navegador.
- Permissão da organização para consumir este repositório público. Não exporte dados internos para o GitHub.

## Instalação via Claude Code
Abra o projeto no Claude Code e peça:

> Instale os agentes e skills de https://github.com/Wilian-Toledo/market-intelligence-agents neste projeto. Primeiro localize a raiz e verifique conflitos. Faça `git clone` para uma pasta **fora da raiz do projeto** (ou utilize um ZIP previamente baixado e extraído). Copie o conteúdo de `plugins/market-intelligence/agents/` para `.claude/agents/`, e o conteúdo de `plugins/market-intelligence/skills/` para `.claude/skills/`, preservando todos os arquivos de cada pasta, inclusive `references/` e `scripts/`. Não use PowerShell. Nunca sobrescreva arquivos diferentes sem backup e aprovação. Preserve MCP, `.mcp.json`, `settings.json`, credenciais, relatórios e PBIX. Garanta `reports/` ignorado pelo Git. Não execute auditoria, commit nem push automaticamente.

Reinicie a sessão do Claude Code se necessário. Execute `/mapear-modelo` ou `/validar-indicadores` após instalar. Consulte `docs/upgrade-v0.2.md` para atualização incremental.

## Alternativa ZIP
No GitHub selecione **Code → Download ZIP**, extraia em uma pasta temporária acessível, e peça ao Claude Code para instalar conforme os caminhos acima. Não é necessário executar scripts.

## Instalação opcional por script
O repositório conserva `scripts/install-native.ps1` para ambientes com PowerShell **autorizado**, mas ele não é necessário nem recomendado onde o terminal é bloqueado.

## Segurança
O MCP existente permanece intocado. Os relatórios de auditoria são gravados localmente em `reports/powerbi-model-audit/` e os contratos específicos em `reports/semantic-validation/`. Nunca publique esses arquivos.
