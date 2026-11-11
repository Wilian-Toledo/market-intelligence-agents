# Instalação nativa sem `/plugin`

O comando `/plugin` pode estar indisponível em determinadas superfícies do Claude. Isso não impede a instalação em **Claude Code local (CLI/IDE)** via `.claude/agents/` e `.claude/skills/`.

## Pré-requisitos
- PowerShell/Windows e Git instalado para a opção de clonagem.
- Diretório local do projeto onde o MCP do Power BI já está configurado.
- Permissão de TI/segurança para o uso deste repositório público e para processar metadados no serviço de IA.

## Um comando no terminal PowerShell
Abra o terminal **dentro do projeto existente** e execute:

```powershell
$dest = Join-Path $env:TEMP ('market-intelligence-' + [guid]::NewGuid().ToString('N')); git clone --depth 1 https://github.com/Wilian-Toledo/market-intelligence-agents.git $dest; if ($LASTEXITCODE -ne 0) { throw 'Falha no git clone'; }; & (Join-Path $dest 'scripts/install-native.ps1') -ProjectPath (Get-Location).Path
```

Ou clone/revise antes e execute manualmente:

```powershell
& 'C:\caminho\market-intelligence-agents\scripts\install-native.ps1' -ProjectPath (Get-Location).Path
```

O instalador:
1. Copia `model-cartographer.md` para `.claude/agents/`.
2. Copia todas as skills do plugin para `.claude/skills/`.
3. Preserva `.mcp.json`, `.claude/settings.json`, credenciais e PBIX.
4. Verifica conflitos antes de copiar; não sobrescreve arquivos diferentes sem `-Force`. Com `-Force`, faz backup local.
5. Acrescenta `/reports/powerbi-model-audit/` ao `.gitignore` existente, sem apagar regras anteriores.

## Primeira execução
Com PBIX aberto no Power BI Desktop e MCP operacional, abra ou reinicie Claude Code local e execute:

```text
/mapear-modelo
```

Ou peça: "Use a skill mapear-modelo e o agente model-cartographer para auditar, em leitura apenas, o PBIX aberto".

Se estiver em um chat remoto sem acesso aos arquivos e ao terminal local, a instalação não os tornará visíveis nessa superfície. O primeiro teste deve ocorrer em uma sessão Claude Code com acesso ao projeto.

## Política de dados
Não faça push nem upload de inventários, DAX internos, outputs ou qualquer informação corporativa para o GitHub público. A auditoria permanece em `reports/powerbi-model-audit/` no projeto autorizado.
