# Atualização 0.1 → 0.2 — sem PowerShell

## O que muda
Adicionamos somente:
- `skills/validar-indicadores/SKILL.md` — comando.
- `skills/semantic-validator/SKILL.md` — método.
- `skills/semantic-validator/references/kpi-contract.schema.json` — contrato portátil.
- `skills/semantic-validator/scripts/check_contract.py` — verificador **opcional** sem dependências.
- `skills/semantic-validator/examples/synthetic-catalog.json` — exemplo fictício.

O agente `model-cartographer` e as skills anteriores **não precisam ser reinstalados** para este upgrade.

## Prompt recomendado no Claude Code (cole na conversa local)
> Quero atualizar este projeto para Market Intelligence Agents v0.2 a partir de https://github.com/Wilian-Toledo/market-intelligence-agents . Primeiro confirme a raiz deste projeto e localize `.claude/skills/`. Se `git` estiver disponível e autorizado, clone o repositório para uma pasta temporária **fora da raiz deste projeto**; caso contrário, peça a pasta de um ZIP extraído. Leia os arquivos a copiar. Copie **apenas** as duas novas pastas completas `plugins/market-intelligence/skills/semantic-validator/` e `plugins/market-intelligence/skills/validar-indicadores/` para `.claude/skills/`, incluindo referências, script e exemplo. Antes de sobrescrever, faça diff e solicite aprovação se houver conteúdo diferente. Não execute scripts PowerShell; não altere `.mcp.json`, `.claude/settings.json`, agentes existentes, PBIX ou relatórios de auditoria. Garanta que `reports/` não seja versionado. Não execute o validador ainda, não faça commit nem push. Ao terminar, confirme arquivos instalados e instrução de uso.

## Primeiro uso
Abra/reinicie a sessão do Claude Code e execute:
```text
/validar-indicadores
```

Ele deve reutilizar a auditoria de `reports/powerbi-model-audit/` e gerar, **somente localmente**, um catálogo de até 12 KPIs prioritários, status/evidências/limites de uso e as próximas 3 decisões. Se Python estiver disponível e permitido, pode executar o verificador do contrato; caso contrário, prossiga pela revisão manual.

## Segurança
Não inclua os relatórios específicos da empresa, amostras reais, tokens ou DAX proprietários no GitHub. O repositório é público.
