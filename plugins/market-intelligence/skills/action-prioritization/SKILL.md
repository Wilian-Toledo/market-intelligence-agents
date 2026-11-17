---
name: action-prioritization
description: "Prioriza movimentos comerciais e verificações de dados com base em evidência, impacto possível, esforço, risco e reversibilidade, sem fabricar retorno financeiro."
---

# Action Prioritization — perspectiva de desenvolvimento comercial v1.1

## Missão
Não confunda "corrigir indicadores" com o objetivo do negócio. Partindo dos achados rastreáveis, responda: **onde vale concentrar atenção gerencial agora, qual teste/comportamento concreto realizar e o que observar para decidir a seguir?** Este é um método genérico, não um playbook fixo de seguros.

## Dois trilhos obrigatórios
1. **Movimentos de negócio (primeiro, quando houver sinal utilizável):** investigar recorte de perda/ganho relativo (região, produto, concorrente, canal etc. se disponível), comparar desempenhos equivalentes, testar hipótese reversível, examinar composição da carteira ou capacidade/execução mediante dados autorizados. Não garantir causalidade. Não direcionar verbas/produção definitiva com KPIs provisórios.
2. **Destravamento de confiabilidade:** confirmar definições essenciais, reconciliar dado ou verificar filtros que realmente impedem o movimento acima. Não transformar todo o direcionamento em um backlog técnico.

Quando não houver recorte confiável, priorize **um teste exploratório de dados comerciais + uma validação de definição**; deixe claro que não há decisão comercial confiável ainda.

## Classificação
Para até 3 prioridades, registre:
- `tipo`: `investigar`, `validar`, `experimento reversível`, `executar` (a última exige evidência aprovada e condições econômicas apropriadas).
- `por_que_agora`: insight/finding ID e observação mais forte.
- `impacto_possivel`: alto/médio/baixo/desconhecido com justificativa e sem atribuir valor de retorno não calculado.
- `esforco`: baixo/médio/alto/desconhecido.
- `risco`: baixo/médio/alto/desconhecido; desconhecido não é baixo.
- `dono`: equipe/função, não pessoa inventada.
- `passo_exato`: o que fazer primeiro com o que está disponível.
- `medir`: indicador, período e condição para reavaliar.
- `condicoes`: o que precisa ser validado antes de adotar a decisão.

Se houver empate sem score defensável, prefira maior valor de aprendizagem, menor risco, menor esforço e reversibilidade. **Não usar scoring arbitrário.**

## Lentes de gestão
- **Diretoria**: exposição, cenários condicionais, concentração e alocação futura somente se houver base econômica válida.
- **Gerência**: quais segmentos/regionais devem ser observados ou comparados primeiro, qual alavanca testar e quem executa.
- **Coordenação**: checagem de campo, rotina simples e métrica de acompanhamento.

## Regras de segurança
Baixo share não implica oportunidade rentável. Queda de mercado não prova que houve perda operacional. Diferença entre crescimento e mercado sem controlar mix não prova eficiência. Sem margem/sinistralidade/custo confirmados, **priorize investigação comercial**, não investimento. Não crie percentual-alvo, ranking financeiro, ROI ou recomendações irreversíveis.

## Saída
Grave em `reports/market-intelligence/03-prioridades.md` uma matriz com até 3 linhas e separação explícita entre **movimento comercial exploratório** e **validação de dados**. A OnePage deve mostrar o próximo passo e o dono, não todos os critérios técnicos.
