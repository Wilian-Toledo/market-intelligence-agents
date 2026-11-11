# Market Intelligence Agents

**MVP completo v1.0.0 — Claude Code.** Toolkit de especialistas reutilizáveis para transformar dados analíticos em diagnóstico, hipóteses, prioridades, revisão crítica e uma OnePage visual.

> O método é genérico. Cada projeto mantém **seus próprios KPIs, dimensões, objetivos, evidências e regras de negócio localmente**. Nenhum contexto corporativo entra neste GitHub público.

## Uma instalação → um comando

Se você já instalou a v0.3, siga [docs/upgrade-v1.0.md](docs/upgrade-v1.0.md) para instalar **somente os módulos novos** por clone ou ZIP, sem PowerShell.

Depois, em uma sessão local do Claude Code:

```text
/gerar-onepage
```

Opcionalmente passe uma pergunta:

```text
/gerar-onepage Onde estão os principais desvios de crescimento, quais hipóteses testar e o que priorizar?
```

O orquestrador reusa auditoria, contratos e diagnóstico local **sem recalcular tudo**; se alguma etapa estiver faltando, tenta executá-la na mesma chamada. Trabalha em leitura apenas, sem modificar PBIX ou MCP.

## Especialistas disponíveis

| Módulo | Responsabilidade |
|---|---|
| `model-cartographer` | Mapa semântico e auditoria |
| `semantic-validator` (skill) | Contratos de KPIs e estados de uso |
| `market-diagnostician` | Diagnóstico quantitativo |
| `hypothesis-investigator` | Explicações concorrentes e testes |
| `opportunity-strategist` | Priorização condicional por benefício, esforço e risco |
| `challenge-reviewer` | Revisão crítica e bloqueio de afirmações frágeis |
| `executive-storyteller` | Narrativa e OnePage para níveis gerenciais |

**Comando principal:** `/gerar-onepage`, que coordena esses módulos. As skills antigas permanecem utilizáveis individualmente.

## Saídas do MVP (somente local)
```text
reports/market-intelligence/
  01-diagnostico-base.md
  02-hipoteses.md
  03-prioridades.md
  04-revisao-critica.md
  05-manifesto.md
  onepage.md
  onepage.html
```

Abra `onepage.html` localmente no navegador para visualizar e, se permitido, imprimir como PDF. O template é responsivo, HTML/CSS estático, sem bibliotecas ou imagens externas.

## Limites de confiança
- Sem definições de negócio confirmadas, qualquer OnePage permanece marcada como **EXPLORATÓRIA — NÃO VALIDADA PARA DECISÃO EXECUTIVA**.
- Indicadores reprovados ou bloqueados são excluídos; indicadores restritos exigem recorte comprovadamente compatível.
- Hipóteses são **hipóteses**, não causas comprovadas. Não inventamos ROI, margem, potencial financeiro, sinistralidade comparável nem projeções.
- A prioridade inicial pode ser **investigar/validar/experimentar**, em vez de recomendar investimento.
- Nunca publicamos dados, PBIX, DAX interno, credenciais ou relatórios no GitHub público.

## Segurança / implantação
Use somente ambiente e fontes autorizados pela organização. O toolkit não altera medidas, PBIX, RLS, refresh, modelo, credenciais, configurações ou MCP. Não executa PowerShell por padrão. Não exige Python: verificadores automáticos são opcionais.

**Estado:** os arquivos são versionados e podem ser revisados publicamente. A integração completa no Claude Code + Power BI do usuário ainda precisa de teste local.
