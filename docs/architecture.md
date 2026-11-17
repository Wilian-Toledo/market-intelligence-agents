# Arquitetura do toolkit — v1.1

```text
Modelo e fontes autorizadas (somente leitura)
  → Model Cartographer (inventário existente)
  → Semantic Validator (contratos e confiabilidade)
  → Market Diagnostician (achados reutilizáveis)
  → Hypothesis Investigator (hipóteses concorrentes)
  → Opportunity Strategist (movimento comercial + validação necessária)
  → Executive Storyteller (OnePage HTML para notebook)
  → Challenge Reviewer (credibilidade e clareza)
  → reports/market-intelligence/onepage.html
```

O comando `/gerar-onepage` executa o fluxo completo e **reutiliza** evidências anteriores.

## Separação e portabilidade
Especialistas e métodos ficam em agentes/skills genéricos. Regras de negócio, nomes de organizações, séries, KPIs, parâmetros e limites ficam em **contexto e contratos locais**. Atualização de regra não obriga reescrever especialistas; requer revalidar indicadores afetados e achados dependentes.

## Padrão do produto final
- Pergunta central focada na diferença de desempenho vs. referência; fallback se share indisponível.
- História concisa: mensagem → KPIs alinhados → visual comparativo → insights → hipóteses → movimentos → lentes por nível.
- HTML estático de notebook: texto >=14px, sem scroll horizontal, até 1440px de conteúdo, notas metodológicas recolhíveis. PDF/A4 não define o layout.
- Com KPIs provisórios, **somente exploração** e propostas reversíveis, sem alocação de investimento por retorno presumido.
- Saídas e dados específicos ficam exclusivamente no projeto local e fora do Git.
