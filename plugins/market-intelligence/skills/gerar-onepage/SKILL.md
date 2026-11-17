---
name: gerar-onepage
description: "Orquestra diagnóstico, hipóteses, ações e revisão crítica em uma OnePage executiva HTML screen-first, sem alterar dados e reutilizando evidências existentes."
argument-hint: "[pergunta comercial / recorte / público opcional]"
---

# Gerar OnePage — orquestração v1.1 para notebook

## Objetivo
**Uma execução, uma OnePage web para notebook**, não um relatório de auditoria nem uma folha A4. Priorize uma mensagem comercial, comparativos, hipóteses testáveis e próximos movimentos. Reaproveite trabalho anterior; não repita mapeamento/auditoria sem necessidade.

## Pergunta orientadora (adaptável)
Se `$ARGUMENTS` trouxer pergunta, use-a. Caso contrário: **"Onde a entidade analisada ganha ou perde espaço versus mercado/referência, o que pode explicar os movimentos e onde concentrar a investigação e o esforço comercial?"**
Se share não estiver disponível ou confiável, use **crescimento relativo ou outro desvio comparável**. Não force medidas específicas. A pergunta é um padrão, não uma regra de negócio engessada.

## Etapas em UMA chamada
1. Leia no projeto autorizado os arquivos existentes em `reports/powerbi-model-audit/`, `reports/semantic-validation/01-catalogo-kpis.json` e `reports/performance-diagnostics/`. Reuse se escopo, período e KPI IDs continuarem compatíveis; se faltar algo essencial, execute apenas a menor etapa necessária. Sem repetição de auditoria completa.
2. **Diagnóstico**: use `market-diagnostician` e `performance-diagnostics` apenas para atualizar achados que não respondam à pergunta. Se o diagnóstico anterior já responde, use-o. Para novo recorte, apenas consultas agregadas pequenas e exclusivamente leitura, se permitidas.
3. **Investigação**: acione `hypothesis-investigator` e `hypothesis-analysis` para até 2 hipóteses concorrentes e respectivos testes.
4. **Prioridades**: acione `opportunity-strategist` e `action-prioritization`. Diferencie claramente (a) movimento comercial exploratório, por região/produto/concorrente ou dimensão disponível, e (b) validação de qualidade estritamente necessária. Até 3 movimentos com dono por função, passo e indicador. Se não houver informação econômica aprovada, só propor investigação ou experimento reversível, **nunca alocação definitiva**.
5. **OnePage**: acione `executive-storyteller` e `executive-storytelling`, **versão screen-first v1.1**, usando `assets/onepage-template.html`. Faça HTML estático local responsivo para notebook, com corpo legível, 3 KPIs coerentes, **um comparativo visual verdadeiro** quando houver dados, até 3 insights e 3 ações. Conteúdo metodológico secundário fica recolhível em `<details>`. Não deixar nenhum `{{PLACEHOLDER}}` no HTML: omita seções sem informação. Gere também Markdown equivalente.
6. **Revisão**: acione `challenge-reviewer` e `evidence-review`. Verifique status dos KPIs, universos, janelas, causalidade, risco das ações, legibilidade em notebook e ausência de extrapolações. Corrija apenas pontos relevantes na OnePage **uma vez**. Caso bloqueio persista, sinalize e entregue um rascunho exploratório.
7. Preserve trilha local em `reports/market-intelligence/`: `01-diagnostico-base.md`, `02-hipoteses.md`, `03-prioridades.md`, `04-revisao-critica.md`, `05-manifesto.md`, `onepage.md` e `onepage.html`.

## Evidência e segurança
- `approved`: utilizar dentro do escopo certificado; `provisional`/ `restricted`: exploração e ressalvas, restrito só se condição checada; `rejected`/ `blocked`: **excluir**.
- Zero KPI aprovado → aviso visível **EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA**, inclusive no HTML.
- Não usar crescimento/participação como prova de rentabilidade, sinistralidade, ROI ou causa. Nunca invente comparações, metas, números, sinistros, visuais ou projeções.
- Não alterar PBIX, DAX, relações, fontes, refresh, RLS, MCP ou configurações. Não buscar dados individuais ou pessoais. Não instalar programas, usar PowerShell, publicar HTML, commitar, fazer push ou upload. Os relatórios ficam exclusivamente no projeto local, ignorados pelo Git.
- Não pergunte por definições desconhecidas se conseguir entregar um **rascunho com suposições/limites claros**. Não reescreva skills; mantenha regras específicas apenas nos contratos e contexto do projeto.

## Critério de sucesso (autoavaliação)
- Leitura no notebook: um leitor entende **o que mudou, por que importa, o que investigar e quem faz o quê** em cerca de 1 minuto.
- Título curto e comercial, parágrafos breves; termos como DAX, IDs técnicos, tautologia, cadastro, janelas sobrepostas pertencem às notas, exceto se forem o verdadeiro achado de negócio.
- HTML legível em 1366×768/1920×1080, sem scroll horizontal; rolagem vertical curta é aceitável. A4 NÃO é restrição de design.
- Ao terminar, informe caminho de `onepage.html`, uma frase de achado, três movimentos no máximo, nível de confiança e estado da revisão. Não recontar toda a auditoria.
