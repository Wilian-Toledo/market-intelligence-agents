---
name: evidence-review
description: "Revisão adversarial de evidências e de OnePage para notebook, garantindo indicadores permitidos, comparações justas, prioridades proporcionais e clareza."
---

# Evidence Review — revisão direcionada v1.1

Audite a **veracidade e utilidade** da OnePage antes de entregar, sem reexecutar toda a análise:
1. **Evidência:** cada número e comparação deve apontar para KPI permitido, fonte, período e recorte. Proibir números fictícios; não presumir que teste executado foi aprovado.
2. **Gates de KPI:** indicadores `rejected` e `blocked` excluídos; `restricted` com condições demonstradas; `provisional` com ressalva. Sem KPI aprovado, modo exploratório visível.
3. **Comparabilidade:** YoY versus sequencial identificado, período parcial tratado, população/unidade/filtros compatíveis, pp vs %. Se gráfico compara grandezas diferentes, sinalizar.
4. **Hipóteses:** nenhuma causalidade atribuída sem evidência, hipótese com teste discriminante; sem conjecturas apresentadas como conclusões.
5. **Movimento comercial:** pelo menos um próximo movimento ligado a achado (quando existe sinal aproveitável). Validação de dados pode coexistir, mas não deve substituir automaticamente todas as prioridades comerciais. Não recomendar investimento sem dados econômicos/risco aprovados.
6. **Notebook:** headline compreensível, corpo legível (>=14px), comparativo visual se há dados adequados, até 3 insights/ações, notas técnicas discretas, sem rolagem horizontal em 1366px. Não exigir A4 nem reduzir fonte para impressão.
7. **Segurança:** HTML e relatórios locais, sem script, CDN, imagem de rede, dados pessoais, compartilhamento ou Git push.

Saída curta em `reports/market-intelligence/04-revisao-critica.md`: `pass_with_caveats` ou `needs_revision`, problemas `blocker/major/minor` e correções. Uma revisão da OnePage por execução basta; se ainda houver bloqueio, declarar, sem fingir aprovação.
