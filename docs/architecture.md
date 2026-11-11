# Arquitetura

```text
Fontes autorizadas / MCP existente
    -> Inventário do modelo (Model Cartographer)
    -> Contratos e status de KPIs (Semantic Validator)
    -> Diagnóstico (planejado)
    -> Investigação e priorização (planejados)
    -> Revisão crítica (planejada)
    -> Storytelling e OnePage (planejados)
```

## Separação de responsabilidades
1. **Especialistas reutilizáveis:** agentes e skills descrevem procedimentos de auditoria, estatística, comparabilidade, priorização e narrativa. Não conhecem marcas, setores, medidas ou regras locais por padrão.
2. **Contexto do projeto:** dados, objetivos, métricas específicas, glossário, decisões de negócio e evidências vivem apenas no ambiente autorizado.
3. **Contratos:** cada KPI descreve origem, população, unidade, janela, filtros, evidência, estado e uso permitido. Mudanças de negócio alteram contratos e testes afetados, não o método genérico.
4. **Portões de qualidade:** rejeitar ou bloquear indicadores com falhas; permitir exploração sinalizada quando evidência técnica existe mas definição de negócio ainda está pendente.
5. **Ferramentas:** consultas agregadas e leitura via MCP já configurado. Scripts de verificação podem ser usados se runtime for permitido; não são exigência para o workflow.

## Limitações intencionais
- Nenhuma alteração automática no PBIX, relações, medidas, fontes ou refresh.
- Nenhum diagnóstico causal sem teste de hipótese.
- Nenhuma recomendação de investimento com base apenas em share ou crescimento.
- Nenhuma projeção sem condições mínimas de histórico e comparação.
- Nenhum dado ou metadata corporativa no repositório público.

Status: v0.2 contém apenas mapeamento e validação semântica. O restante está no roadmap.
