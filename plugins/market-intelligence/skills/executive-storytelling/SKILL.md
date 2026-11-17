---
name: executive-storytelling
description: "Storytelling executivo e design de OnePage para leitura no notebook, com hierarquia de decisão, comparativos visuais e rastreabilidade proporcional à confiança."
---

# Executive Storytelling — OnePage screen-first v1.1

## Objetivo
Escreva para direção de desenvolvimento comercial/planejamento: em menos de 60 segundos, o leitor deve captar **qual movimento merece atenção, por quê e qual decisão ou teste fazer**. Não seja um auditor narrando tudo que verificou. Skill portável: **não embuta marca, medida, setor, limiar ou recorte fixo**.

## Pergunta central
Receba a pergunta do orquestrador ou do projeto. Na ausência, investigue **onde o objeto analisado ganha/perde espaço versus seu mercado ou referência, o que pode explicar a diferença e quais próximos movimentos merecem atenção**.
Se não existir share comparável e habilitado, substitua pelo desvio de crescimento/performance e assinale a limitação. Não force análises que o modelo não suporta.

## Storytelling: decisório, não descritivo
1. **Título com uma conclusão observável**, em até 14 palavras, com verbo e período contextualizado. Não usar títulos técnicos (ex.: "diferença por aritmética de janelas sobrepostas") ou causais sem prova.
2. **Uma frase "por que importa"**: explique a tensão entre desempenho interno e mercado/benchmark, sem confundir períodos.
3. **Até 3 KPIs ligados à mesma mensagem**, com unidade (%, pp, R$, etc.), janela e status discretos. Não misture 3M YoY com 12M YoY como se fossem mesmo período.
4. **Visual comparativo principal** e 1 pequeno recorte opcional, *somente* quando existem observações verificáveis. Exemplos: barras com base zero para valores positivos, linhas com eixo temporal coerente, barras divergentes para variações com sinal, ranking de regiões com mesmo universo. Nunca invente série nem usar escala distorcida. Se falta base, use um painel de "contraste a investigar" com dados confiáveis.
5. **Até 3 insights comerciais**, cada um no formato: observação numérica → interpretação limitada → implicação ("merece examinar X"). Preferir produto/UF/concorrência quando esses recortes forem permitidos e comparáveis.
6. **2 hipóteses concorrentes, no máximo**, com teste necessário. Não fingir causalidade.
7. **Até 3 próximos movimentos**: ação, responsável *por função*, verificação e indicador de acompanhamento. Separar visualmente **movimento comercial exploratório** de **higiene/validação do dado**. Havendo dados provisórios, ação comercial só pode ser investigação/experimento reversível, nunca alocação definitiva.
8. **Públicos**: uma linha de implicação para diretoria (trade-off e risco), gerência (onde testar/acompanhar) e coordenação (o que verificar/operar). Não criar três OnePages.
9. **Notas de método** discretas (rodapé ou `<details>` expansível): fontes locais, janelas, restrições, dúvidas. Não ocupar o corpo principal com DAX, IDs técnicos, cadastros ou parágrafos de auditoria.

## Layout notebook-first — obrigatório
- Entrega **HTML local** em `reports/market-intelligence/onepage.html` + `onepage.md`, usando `assets/onepage-template.html`.
- Destino principal: navegador no notebook, 1366×768 e 1920×1080. Conteúdo em área central até 1440px, responsivo, **sem rolagem horizontal**; rolagem vertical curta é permitida, nunca comprimir fonte para caber numa folha.
- Fonte normal >=14px, rótulos auxiliares idealmente >=12px, headline 26–32px, KPIs >=26px. Contraste alto, espaçamento claro e no máximo 2 colunas em notebook; 1 em tela estreita.
- Estrutura: topo/narrativa → faixa de KPIs → diagnóstico visual e insights → movimentos priorizados → perspectivas + notas recolhíveis. Uma página **web** contínua, não uma página física A4. CSS de impressão é **opcional**, sem dirigir o design.
- Visuais sem JavaScript, CDN, imagens externas nem bibliotecas: CSS ou SVG inline gerados a partir de dados já verificados, com legenda, eixos/unidade, título, período e `aria-label`. Para gráficos de barras, represente eixo zero corretamente e não use escalas enganosas.
- Edite/omita seções sem evidência, não preencha com dados sintéticos; não deixe `{{PLACEHOLDERS}}` residuais. Escape `& < > " '` de textos provenientes dos dados antes de inserir HTML. Fragmentos SVG/HTML gerados devem ser seguros e autocontidos.
- O HTML produzido não será hospedado/publicado; apenas aberto localmente em navegador autorizado.

## Política de confiança
- `approved`: só dentro dos escopos comprovados.
- `provisional` e `restricted`: conteúdo **exploratório** e restrições respeitadas. Se não houver KPI aprovado, mantenha um aviso visível: **EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA**.
- Não expor KPI `rejected`/`blocked`, causa sem teste, rentabilidade/ROI/sinistralidade sem base suficiente ou "oportunidade" monetária inventada.
- Advertência de confiabilidade não é licença para despejar todo o inventário de riscos na tela. Limitações importantes no próprio insight; demais em notas.

## Check visual rápido
Confirme em código: fonte legível, títulos curtos, nenhuma seção excede 3 bullets/insights, ausência de overflow horizontal, imagens externas/scripts/CDN ausentes, `<details>` com notas e aviso de confiabilidade. Se puder usar navegador local autorizado, confira 1366×768; não afirme validação visual se não verificou.
