# Atualização incremental v0.2 → v0.3 (sem PowerShell)

## O que entra na versão
**Novo agente**
- `plugins/market-intelligence/agents/market-diagnostician.md`

**Novas skills (copiar pastas inteiras)**
- `plugins/market-intelligence/skills/performance-diagnostics/` (método, schema, verificador opcional e exemplo sintético)
- `plugins/market-intelligence/skills/diagnosticar-desempenho/` (comando)

As skills e o agente anteriores permanecem intactos. Nenhum MCP ou configuração será modificado.

## Prompt pronto para o Claude Code local
> Atualize este projeto para **Market Intelligence Agents v0.3** a partir de https://github.com/Wilian-Toledo/market-intelligence-agents . Primeiro confirme a raiz do projeto e que existe `reports/semantic-validation/01-catalogo-kpis.json`; **não abra nem envie dados para o GitHub**. Se `git clone` estiver permitido, clone o repositório para uma pasta temporária fora deste projeto; caso contrário, use o ZIP do GitHub previamente extraído. Leia `docs/upgrade-v0.3.md`. Copie **somente** `plugins/market-intelligence/agents/market-diagnostician.md` para `.claude/agents/` e as duas pastas completas `plugins/market-intelligence/skills/performance-diagnostics/` e `plugins/market-intelligence/skills/diagnosticar-desempenho/` para `.claude/skills/`. Preserve `references/`, `scripts/` e `examples/`. Compare conflitos antes de copiar e peça confirmação se houver diferença. Não execute PowerShell. Não altere o PBIX, MCP, settings, relatórios locais, agentes/skills anteriores nem credenciais. Não faça commit ou push. Verifique que `reports/` está ignorado pelo Git. Ao terminar, confirme a instalação, **sem rodar o diagnóstico automaticamente**.

## Execução
Reinicie a sessão local do Claude Code se necessário e execute:
```text
/diagnosticar-desempenho
```

Opcionalmente informe uma pergunta, por exemplo:
```text
/diagnosticar-desempenho Quais recortes apresentam maior diferença de crescimento em janelas comparáveis?
```

O comando usará `reports/semantic-validation/01-catalogo-kpis.json`, respeitará status e restrições, consultará agregados somente quando necessário/permitido e gravará **somente no projeto local**:
- `reports/performance-diagnostics/00-sintese-exploratoria.md`
- `reports/performance-diagnostics/01-achados.json`
- `reports/performance-diagnostics/02-evidencias-e-lacunas.md`
- `reports/performance-diagnostics/03-rascunho-onepage.md`

Com zero KPIs aprovados, os resultados serão apenas **exploratórios** e não devem ser utilizados como decisões executivas. Ao final, solicite um resumo sanitizado sem valores ou nomes internos para revisão externa.

## Sem Python
A análise e a checagem manual ainda funcionam; o script de verificação de achados é **opcional**. Não instale Python nem contorne bloqueios corporativos.
