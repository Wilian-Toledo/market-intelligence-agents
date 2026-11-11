# Arquitetura do toolkit — v0.3

```text
Modelo/fonte autorizado + ferramenta de leitura
  → Model Cartographer (inventário técnico)
  → Semantic Validator (contratos e usos permitidos)
  → Market Diagnostician (achados de desempenho e rascunho exploratório)
  → [futuro] investigação causal / priorização econômica
  → [futuro] revisão crítica / storytelling executivo aprovado
```

## Separação de conhecimento
- **Agentes:** especialistas reutilizáveis, sem referências a uma empresa.
- **Skills:** métodos analíticos independentes de modelo, setor ou fórmula específica.
- **Contexto local:** catálogo de KPIs, auditoria, filtros, objetivos e regras aprovadas.
- **Contratos de evidência:** cada achado aponta KPIs/recortes/janelas/fontes. Uma mudança na regra afeta apenas contratos e achados dependentes.

## Governança
- Sem `approved`, o relatório é exploratório, não uma recomendação definitiva.
- Não usar métricas rejeitadas ou bloqueadas; `restricted` somente sob condições demonstradas.
- Comparar janelas equivalentes, com população/denominador consistente e tratamento de meses parciais.
- Interpretar causalidade como hipótese até haver evidência específica.
- Não identificar maior crescimento como maior retorno econômico.
- Usar apenas leitura autorizada; não modificar PBIX, credenciais, MCP ou configuração local.
- Saídas reais permanecem em `reports/` ignorado pelo Git, nunca no repositório público.
