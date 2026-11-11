---
name: diagnosticar-desempenho
description: "Gera diagnóstico exploratório de desempenho e um rascunho de OnePage a partir de KPIs já validados, sem mudar o modelo nem inferir causalidade."
argument-hint: "[pergunta analítica / recorte opcional]"
---

# Diagnóstico orientado por evidências — v0.3

1. Trate `$ARGUMENTS` como a pergunta/recorte principal. Sem argumentos, use "Onde estão os principais desvios de desempenho e crescimento observados nos períodos comparáveis?". Não suponha setor, métricas específicas ou linha de negócios.
2. Verifique `reports/semantic-validation/01-catalogo-kpis.json`. Se não existir, peça executar `/validar-indicadores` e interrompa. Leia `reports/powerbi-model-audit/` só se necessário.
3. Use o agente `market-diagnostician` e a skill `performance-diagnostics`; se delegação não estiver disponível, aplique a metodologia no contexto atual.
4. **Política de status:** use apenas `approved` e `provisional` habilitados para o uso; `restricted` somente após conferir suas condições. Exclua `rejected` e `blocked`. Não reclassifique.
5. Não existe "conclusão aprovada" quando faltam definições de negócio. Faça **diagnóstico exploratório** com rótulo visível; não apresente recomendações executivas de investimento, afirmações causais ou projeções.
6. Analise até 5 achados com janelas comparáveis e rastreabilidade. Se dados agregados faltarem, faça consultas **pequenas, estritamente leitura e autorizadas** via ferramenta já conectada. Não altere modelo, PBIX, medidas, MCP ou configurações.
7. Grave quatro relatórios **somente localmente** em `reports/performance-diagnostics/`, confirmando `.gitignore`. Não faça commit, push, upload ou exportação de dados.
8. Mostre resumo com quantidade de KPIs utilizados por status, achados (sem exagerar a confiança), limitações e 3 investigações prioritárias. Ao usuário externo, compartilhe apenas resumo sanitizado e autorizado.

Se o catálogo estiver incompatível com a pergunta, entregue um bloqueio explicado e a menor ação para desbloquear; não substitua automaticamente por medidas reprovadas.
