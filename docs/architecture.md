# Arquitetura do MVP v1.0

```text
PBIX / modelo analítico / arquivos locais autorizados
    ↓
Model Cartographer (inventário; reusar se já existe)
    ↓
Semantic Validator (contratos; reusar se já existe)
    ↓
Market Diagnostician (achados; reusar se já existe)
    ↓
Hypothesis Investigator (explicações concorrentes)
    ↓
Opportunity Strategist (ações condicionais por evidência/risco/esforço)
    ↓
Executive Storyteller (rascunho visual)
    ↓
Challenge Reviewer (controle final; uma revisão se necessário)
    ↓
onepage.html + onepage.md + trilha de evidências (local)
```

## Um só comando
`/gerar-onepage` coordena tudo, reaproveitando etapas presentes. Seu nome é propositalmente genérico, assim como os especialistas.

## Compartimentos
- **Método público:** agentes, skills, contratos e template de HTML, sem informações exclusivas do projeto.
- **Contexto local:** fontes, filtros, objetivos, definições, evidências e KPIs. Mudança de regra atualiza **contratos e achados dependentes**, não o método do especialista.
- **Saídas locais:** `reports/`, com proteção Git. Não realizar upload.

## Confiabilidade
1. Achados só usam indicadores permitidos pelo catálogo de KPIs.
2. Hipóteses são rotuladas e acompanhadas de possíveis testes/refutações.
3. Priorização é de **ações reversíveis de aprendizagem** na ausência de métricas econômicas validadas.
4. A OnePage é **exploratória** enquanto faltarem definições de negócio.
5. Revisor crítico pode forçar ressalva, correção pontual ou registrar bloqueio; não altera modelo nem valida KPIs unilateralmente.
6. OnePage estática local sem dependências externas, para leitura em navegador/possível impressão A4.
