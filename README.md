# Market Intelligence Agents

**MVP v1.1 — OnePage executiva para notebook.** Toolkit de agentes e skills reutilizáveis para transformar dados analíticos em **diagnóstico, hipóteses e direcionamento**.

O método é genérico. **KPIs, filtros, modelos, objetivos e definições locais pertencem ao projeto autorizado**, não a este repositório público.

## Principal comando
```text
/gerar-onepage
```

Sem pergunta informada, o orquestrador procura: "Onde a entidade ganha/perde espaço versus mercado ou referência, o que pode explicar e onde concentrar atenção comercial?" Se o modelo não sustenta share, usa desvios comparáveis sem inventar participação.

## O que mudou na v1.1
- **Executive Storyteller**: título comercial, até 3 KPIs e insights, 1 comparativo visual legítimo, prioridades e perspectivas para direção, gerência e coordenação.
- **Opportunity Strategist**: primeiro identifica movimentos de negócio *exploratórios*, depois destaca validações que realmente bloqueiam decisões. Não inventa rentabilidade nem ROI.
- **Challenge Reviewer**: critica evidências e se a OnePage é legível e útil para gestão.
- **Orquestrador**: reusa auditoria/contratos/diagnóstico locais, sem repetir etapas nem pedir que execute diversos comandos.
- **Template HTML**: screen-first para notebooks 1366×768 e 1920×1080, responsivo, sem dependências externas; rolagem vertical curta aceita. Não é uma folha A4.

## Atualizar sem PowerShell
Use [docs/upgrade-v1.1.md](docs/upgrade-v1.1.md). No Claude Code, clone/revise via Git (se autorizado) ou use ZIP, copiando **somente arquivos alterados** para `.claude/`. Preserve PBIX, MCP, settings, contratos e relatórios locais.

## Componentes atuais
- `model-cartographer`: inventário semântico via MCP.
- `semantic-validator`: contratos e status dos KPIs.
- `market-diagnostician`: diagnóstico quantitativo.
- `hypothesis-investigator`: hipóteses concorrentes.
- `opportunity-strategist`: prioridades condicionais.
- `challenge-reviewer`: crítica da evidência/narrativa.
- `executive-storyteller`: HTML visual.

**Comandos individuais**: `/mapear-modelo`, `/validar-indicadores`, `/diagnosticar-desempenho`. **Comando integrado**: `/gerar-onepage`.

## Saída principal
`reports/market-intelligence/onepage.html` e `onepage.md` **locais**. A trilha de evidências fica no mesmo diretório ignorado pelo Git.

## Controles
- Dados internos, PBIX, DAX, valores e credenciais **não são publicados** neste GitHub.
- KPI reprovado/bloqueado não fundamenta achado; KPI restrito só no recorte permitido; provisório exige ressalva.
- Sem confirmação do negócio, sinalizar **EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA**. Ações comerciais são investigações/experimentos reversíveis, não decisões definitivas de orçamento.
- Não altera medidas, PBIX, fontes, MCP, RLS ou refresh; não exige PowerShell nem Python.

**Status:** conteúdo da v1.1 publicado e inspecionável. A nova apresentação HTML deve ser testada localmente no Claude Code antes de uso gerencial.
