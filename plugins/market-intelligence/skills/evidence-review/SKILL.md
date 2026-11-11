---
name: evidence-review
description: "Revisão adversarial de consistência analítica e decisões: KPIs permitidos, rastreabilidade, comparabilidade, explicações e integridade da narrativa."
---

# Evidence Review — gate mínimo antes da OnePage

Revise cada achado e afirmação usando os arquivos **locais** do projeto, sem reexecutar a auditoria completa:
1. **Fonte:** todo fato quantitativo tem ID de KPI, período, recorte e referência rastreável? Há números inexistentes ou estimados sem rótulo?
2. **Status:** nenhum KPI `rejected` ou `blocked` usado? `restricted` tem recorte e teste compatíveis? `provisional` tem ressalva?
3. **Comparação:** YoY versus sequencial identificados? População e denominador iguais? Períodos fechados/comparáveis? pp versus % corretos?
4. **Interpretação:** fato, hipótese e causa separados? Lacunas e limitação de origem, sinistro/prêmio, margem, risco e despesas preservadas?
5. **Decisão:** priorização respeita desconhecidos? Nenhuma recomendação irreversível baseada em dados exploratórios?
6. **Design:** título informa sem exagerar? A OnePage cabe em uma página impressa? Alerta exploratório aparece?
7. **Segurança:** só arquivos locais ignorados pelo Git, sem dados pessoais, upload, log de credenciais ou dependências de rede?

Escreva `reports/market-intelligence/04-revisao-critica.md` com `pass_with_caveats` ou `needs_revision`, severidade `blocker/major/minor`, problema, evidência e correção proposta. Com bloqueio grave, **não declare a OnePage executiva**; um rascunho com bloqueios claros ainda pode ser entregue. Não reclassifique KPI.
