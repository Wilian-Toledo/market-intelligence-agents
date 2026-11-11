---
name: action-prioritization
description: "Priorização condicionada à evidência de ações, pesquisas e experimentos, considerando impacto possível, esforço, risco, dependências e viabilidade."
---

# Action Prioritization

## Primeiro, escolha o tipo de priorização
- **Confiabilidade insuficiente / sem métricas econômicas:** priorize **investigações, validações e experimentos de baixo risco**, não investimento monetário.
- **Dados econômicos e risco validados:** priorize opções de negócio de acordo com política de risco, custo, capacidade, impacto incremental e incerteza, sem prometer ROI.

## Critérios explícitos
Para cada opção use escala qualitativa documentada:
- `benefit`: benefício esperado como decisão melhor, evidência destravada, mitigação de risco ou melhoria potencial; evite quantificar dinheiro sem fórmula e base aprovadas.
- `effort`: baixo/médio/alto/desconhecido e o que falta para estimar.
- `risk`: baixo/médio/alto/desconhecido; risco desconhecido **não é risco baixo**.
- `evidence`: forte/média/fraca, com referências aos contratos e achados.
- `dependencies`: dados, confirmação de negócio, capacidade operacional ou teste adicional.
- `reversibility`: reversível, parcialmente reversível, irreversível.
Não atribua score numérico arbitrário. Se precisar desempatar, prefira **baixo risco, alta aprendizagem, reversibilidade e menor esforço**, explicitando a regra de seleção.

## Saída
No máximo 3 prioridades, em quadro curto:
`Ação | Motivo e evidência | Benefício esperado (qualitativo) | Esforço | Risco | Dependência | Responsável por função | Indicador de acompanhamento`.

Cada prioridade deve ter próximo passo observável. Se necessário diferencie ações para diretoria, gerência e coordenação como **perspectivas**, não agentes redundantes. Nunca apresente hipótese como fato nem valide rentabilidade a partir apenas de crescimento.
