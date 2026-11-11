---
name: semantic-validator
description: "Valida contratos semânticos de indicadores em qualquer modelo analítico: significado, granularidade, filtros, período, comparações, evidências e condições de uso. Não corrige dados nem medidas."
---

# Semantic Validator — método reutilizável v0.2

## Missão
Transformar um inventário e evidências já existentes em **contratos de KPIs verificáveis**, sem assumir regras específicas de setor ou de empresa. Os fatos locais vêm dos arquivos do projeto, não desta skill. Seja pragmático: priorize os indicadores necessários para responder à pergunta de negócio, não a auditoria interminável de todas as medidas.

## Entradas
- Questão de negócio e público-alvo (se não informados, assumir "diagnóstico exploratório de desempenho").
- Relatório prévio de auditoria, dicionário de medidas ou metadados de um modelo acessível por ferramenta existente.
- Definições de negócio **confirmadas**, **não confirmadas** e decisões metodológicas fornecidas pelo usuário.
- Metadados de origem, períodos, dimensões, fórmulas e testes, quando disponíveis.

O relatório existente é **evidência**, não uma ordem para reescrever o modelo. Se não houver auditoria, sinalize a lacuna e ofereça mapear primeiro. Não invente dados, nomes, fórmulas, relações ou verificações.

## Procedimento mínimo
1. **Seleção por utilidade:** escolha até 12 indicadores prioritários para a questão proposta (quantidade ajustável). Considere primeiro medidas-base, crescimento, participação, risco e composição, somente quando existirem. Não assuma que um setor específico possui os mesmos KPIs.
2. **Contrato:** para cada indicador, anote ID, nome local, finalidade, unidade, base, origem, período, população/denominador, dimensões, filtros, dependências, testes, pendências, riscos e usos permitidos.
3. **Checagem temporal:** se houver crescimento, declarar explicitamente `yoy` (mesma janela do ano anterior) ou `sequential` (janela imediatamente anterior de mesma duração). Compare períodos fechados e equivalentes; nunca use total de ano parcial contra ano completo. Se o método de comparação não for conhecido, bloquear o indicador comparativo.
4. **Checagem de razões:** para share, taxa ou índice, conferir compatibilidade entre numerador e denominador (unidade, período, universo, filtros, recorte, exclusões). Denominador igual ao numerador por construção é alerta de tautologia; taxa econômica não prova margem se faltam despesas.
5. **Checagem de filtros:** verificar estabilidade ao alternar filtros relevantes. Atenção a hardcodes de empresa/segmento, relacionamentos ambíguos, datas sem fechamento e chaves órfãs. Não presumir erro só por relacionamento bidirecional.
6. **Evidências:** reutilizar testes anteriores com origem e limitações claras. Novos testes somente se necessários, autorizados, agregados, estritamente leitura e sem alterar o modelo. Nunca alegar reconciliação externa sem realizá-la.
7. **Classificação e liberação:** aplique a política de status abaixo; registre o motivo e não promova indicadores automaticamente. Produza um pequeno conjunto utilizável para exploração, mostrando ressalvas.

## Política de status — separação técnica x negócio
- `approved`: definição de negócio formalmente confirmada **e** testes técnicos relevantes aprovados. Pode compor conclusão executiva dentro do escopo validado.
- `provisional`: cálculo tecnicamente coerente, porém significado de negócio/origem ainda pendente; **somente análise exploratória** claramente rotulada.
- `restricted`: resultado coerente apenas sob filtros, períodos, populações ou recortes documentados; **somente exploração dentro das condições** até aprovação completa.
- `rejected`: há prova de erro de fórmula, período, população, unidade ou significado incompatível. **Não usar**.
- `blocked`: evidência indispensável inexistente ou teste crítico não executado; **não usar para decisão**.

Prioridade de segurança: `rejected` ou `blocked` prevalecem sobre aparente plausibilidade. Se houver teste técnico falho, `rejected`. Se falta evidência crítica, `blocked`. Se a semântica não foi validada mas o cálculo é coerente, `provisional` (exploração apenas). Não confundir "teste executado" com "teste passou".

## Regras de consumo
- Para diagnóstico exploratório, podem entrar `provisional` e `restricted`, sempre com alertas e condições explícitas.
- Para recomendação executiva factual sem ressalvas, somente `approved` e somente dentro de seu escopo; se não houver indicador aprovado, produzir **rascunho exploratório, sem recomendar investimento**.
- Não inferir causalidade, retorno, margem, sinistralidade ou oportunidade econômica usando apenas crescimento ou participação.
- O status é **por indicador, contexto e versão de evidência**; mudança na regra demanda revalidação somente dos contratos afetados.

## Artefatos locais
Grave somente no ambiente autorizado, em `reports/semantic-validation/`, sempre fora de Git:
- `00-resultado.md`: síntese, número de KPIs por status e quais análises exploratórias são permitidas.
- `01-catalogo-kpis.json`: formato em `references/kpi-contract.schema.json`, com as evidências locais (não versionar).
- `02-matriz-e-pendencias.md`: status, testes, limites, perguntas de maior impacto e correções propostas, sem aplicar alterações.

O schema e o verificador opcional acompanham esta skill em `references/` e `scripts/`. **Não dependa de Python disponível:** se não houver runtime autorizado, faça validação estrutural manual baseada no schema e declare o teste automatizado como não executado.

## Segurança e encerramento
Nunca alterar PBIX, medidas, relações, fontes, RLS ou refresh; nunca exportar linhas individuais, dados sensíveis, código interno ou relatórios para repositório público. Confira o `.gitignore` antes de gravar. Não criar commits/pushes. Diferencie claramente "confirmado", "inferido" e "pendente". Liste as próximas **3 ações mais úteis**, não uma lista interminável de reparos.
