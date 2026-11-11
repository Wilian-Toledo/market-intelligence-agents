# Market Intelligence Agents

Toolkit modular de **agentes e skills para Claude Code**, orientado a diagnósticos quantitativos, confiabilidade de KPIs e decisões baseadas em evidências. O núcleo é **reutilizável entre projetos, setores e modelos**; regras de negócio e evidências pertencem ao ambiente local do usuário.

## v0.2.0 — o que está disponível
- Subagente `model-cartographer` e skills `/mapear-modelo`, `powerbi-semantic-audit` (inventário Power BI via MCP já instalado).
- **Novo:** `/validar-indicadores` e `semantic-validator` — selecionam KPIs úteis, verificam consistência, classificam confiabilidade e geram contratos locais.
- **Novo:** schema e verificador opcional (Python stdlib) empacotados dentro da própria skill, além de exemplos/testes sintéticos.
- Não inclui agente de diagnóstico ou OnePage nesta versão; consulte `docs/roadmap.md`.

## Instalação ou atualização sem PowerShell
Como `/plugin` pode estar indisponível, peça ao **Claude Code no projeto autorizado**:

> Atualize somente as skills a partir de https://github.com/Wilian-Toledo/market-intelligence-agents . Use git clone em uma pasta temporária (ou ZIP baixado), leia `docs/upgrade-v0.2.md`, compare as pastas antes de copiar e instale `semantic-validator` e `validar-indicadores` em `.claude/skills/` do projeto. Preserve MCP, settings, arquivos locais, agentes existentes e relatórios. Não execute PowerShell, não faça commit ou push. Se houver conflito, solicite confirmação.

Depois reinicie a sessão do Claude Code se necessário e use **`/validar-indicadores`**. A auditoria anterior permanece em `reports/powerbi-model-audit/`; o validador escreve em `reports/semantic-validation/` (ambos fora do Git).

Detalhes: `docs/upgrade-v0.2.md` e `docs/installation-without-plugin.md`.

## Estrutura
```text
plugins/market-intelligence/
  agents/model-cartographer.md
  skills/mapear-modelo/SKILL.md
  skills/powerbi-semantic-audit/SKILL.md
  skills/validar-indicadores/SKILL.md
  skills/semantic-validator/
    SKILL.md
    references/kpi-contract.schema.json
    scripts/check_contract.py
    examples/synthetic-catalog.json
contracts/audit-summary.schema.json
tests/test_contract.py
docs/
```

## Regras de qualidade
- Nenhuma conclusão executiva categórica com KPI sem definição de negócio e validação técnica.
- Indicadores provisórios/restritos servem para **exploração sinalizada**; reprovados/bloqueados não podem sustentar recomendações.
- Crescimento YoY e sequencial possuem janelas explicitamente diferentes; medidas não devem ser misturadas.
- Projeto genérico no GitHub, **contexto de negócio e evidências específicas somente no ambiente autorizado**.

## Segurança
Repositório **público**. Não publicar PBIX, dados, DAX internos, nomes de colaboradores/clientes, credenciais, contextos proprietários ou relatórios locais. Qualquer consulta MCP deve ser estritamente somente leitura, quando autorizada. O toolkit não modifica PBIX, medidas, RLS, refresh nem configuração do MCP.
