---
name: hypothesis-analysis
description: "Disciplina de investigação de desempenho: explicações concorrentes, refutação e testes, preservando a diferença entre fato, hipótese e causalidade."
---

# Hypothesis Analysis

1. Consuma **somente achados rastreáveis** da análise. Para cada um, registre `finding_id`, KPI e janela. Não trate o nome de um indicador ou uma associação como motivo demonstrado.
2. Gere no máximo **duas explicações concorrentes** por achado prioritário e, quando plausível, uma hipótese de falha de cobertura/medição. Use conhecimento do domínio como gerador de hipóteses, não como evidência de que um fator ocorreu.
3. Preencha: `hipótese | mecanismo | evidência favorável | evidência contrária | o que falta | teste que a distingue | resultado que a refutaria`.
4. Sinalize estágio: `untested`, `partial` ou `supported` (apoio observacional, não prova causal). Não chame "causa" se não houve desenho causal adequado.
5. Procure explicações simples e falsificáveis: composição do mix, sazonalidade, base de comparação, cobertura, canais, alteração de cadastro, diferenças de classificação, preço, capacidade, competição etc. Não presuma disponibilidade dessas dimensões.
6. Proponha até **três verificações** de maior informação esperada, e separe as que podem ser realizadas com a base atual das que dependem de dados externos ou validação humana.
7. Saída concisa em `reports/market-intelligence/02-hipoteses.md`, sem relatórios longos, nomes de pessoas ou dados sensíveis compartilhados externamente.
