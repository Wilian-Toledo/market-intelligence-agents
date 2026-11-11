---
name: executive-storytelling
description: "Storytelling e design de OnePage orientado a decisão, com narrativa de dados, públicos gerenciais e alertas proporcionais à evidência."
---

# Executive Storytelling — OnePage v1

## Narrativa
Escreva para um leitor ocupado. Responda em ordem:
1. **Headline:** a observação principal (não "Análise de indicadores"); nunca inferir causalidade.
2. **Contexto e contraste:** o que ocorreu vs. referência válida, com período e universo.
3. **Três sinais no máximo:** KPIs realmente utilizáveis e com unidades corretas; se faltar evidência, "a confirmar".
4. **Diagnóstico:** até 3 fatos/recortes relevantes, acompanhados de limitações.
5. **O que investigar:** até 2 hipóteses com rótulo e o teste que as diferencia.
6. **Direcionamento:** até 3 prioridades executáveis (pesquisa, validação ou experimento reversível caso dados provisórios); proprietário por **função** e indicador de progresso.
7. **Rodapé:** fonte local, janela, população, definições pendentes, status do rascunho.

## Perspectivas gerenciais (sem agentes extras)
- **Diretoria:** exposição, trade-offs, incerteza e decisões dependentes de evidência.
- **Gerência:** recortes, ações coordenadas, alavancas de resultado e verificação.
- **Coordenação/supervisão:** checagens concretas, cadência de acompanhamento e métrica operacional.

Faça UMA página: apresentação principal executiva e uma breve seção de implicações por nível, sem repetir o diagnóstico três vezes.

## Regras visuais
- Salve um arquivo HTML estático em `reports/market-intelligence/onepage.html`, com estilos CSS embutidos; sem JavaScript, CDN, analytics, imagens externas, downloads nem fontes de rede.
- Use a referência `assets/onepage-template.html` para aparência e estrutura, podendo adaptar blocos e títulos, mas mantenha `@page size: A4 landscape`, faixa de alerta, responsividade, legibilidade e rodapé.
- Salve também `onepage.md` com conteúdo equivalente, para auditoria e correção.
- Escapar `& < > " '` nos textos dinâmicos antes de inserir no HTML para evitar injeção de marcação.
- Nunca inserir números exemplificativos como se fossem reais. Blocos sem evidência recebem "Não disponível" ou são omitidos, sem preencher com suposições.
- Se há KPI `provisional` ou `restricted` usado, ou zero KPI aprovado, destaque: **EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA** na capa e no rodapé.
- Rascunho e template são artefatos, não publicação. Não imprima/envie/compartilhe automaticamente.
