# Instalação sem `/plugin` e sem PowerShell

Use esta via no **Claude Code local** quando o ambiente corporativo permite acesso a arquivos mas bloqueia PowerShell ou o gerenciador de plugins.

## Se a v0.3 já existe
Prefira o upgrade incremental em [upgrade-v1.0.md](upgrade-v1.0.md), que instala **somente quatro agentes e cinco skills novos**. Nenhum MCP ou relatório precisa ser alterado.

## Instalação completa do zero (por prompt)
1. Abra o projeto local autorizado no Claude Code.
2. Envie:

> Instale os agentes e skills de https://github.com/Wilian-Toledo/market-intelligence-agents neste projeto. Confira a raiz. Use `git clone` para uma pasta temporária **fora do projeto** se permitido; caso contrário use um ZIP previamente baixado e extraído. Copie cada arquivo de `plugins/market-intelligence/agents/` para `.claude/agents/` e cada pasta inteira de `plugins/market-intelligence/skills/` para `.claude/skills/`, preservando `assets/`, `scripts/`, `references/` e `examples/`. Compare e preserve arquivos existentes; em conflitos, solicite confirmação antes de substituir. Não execute PowerShell nem instale dependências. Não altere PBIX, MCP, `.mcp.json`, settings, credenciais ou arquivos `reports/`. Confirme que `reports/` está ignorado no Git. Não faça commits, pushes nem execute o fluxo sem autorização. Resuma o que foi instalado.

3. Inicie uma nova sessão local do Claude Code se necessário.
4. Execute `/gerar-onepage` para a primeira OnePage. As skills individuais `/mapear-modelo`, `/validar-indicadores` e `/diagnosticar-desempenho` também permanecem.

## Alternativa ZIP
No GitHub use **Code → Download ZIP**. Extraia no Windows e dê ao Claude Code o caminho da pasta extraída. Não há necessidade de executar arquivos de script.

## Segurança
Todo dado de projeto e análise ficam em `reports/` fora do Git. O repositório é público e não recebe PBIX, DAX, medidas proprietárias, credenciais nem valores internos.

## Scripts opcionais
Há verificadores Python e um instalador PowerShell legados para ambientes em que sejam permitidos; **não são requisitos** para gerar a OnePage e não devem ser usados para contornar bloqueios corporativos.
