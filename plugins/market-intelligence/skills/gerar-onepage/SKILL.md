---
name: gerar-onepage
description: "Orquestra uma primeira OnePage completa de inteligência de desempenho com diagnóstico, hipóteses, prioridades condicionais, revisão crítica e storytelling, reutilizando auditorias locais."
argument-hint: "[pergunta de negócio / recorte / público opcional]"
---

# Gerar OnePage — MVP integrado v1.0

**Objetivo:** Entregar em UMA execução um rascunho visual de OnePage local, bem como seus artefatos de sustentação. Não interrompa o fluxo para pedir detalhes que podem ser inferidos dos arquivos locais; use premissas explícitas. **Não peça para o usuário executar mais quatro skills separadamente.**

## Contexto e limites (obrigatórios)
- A pergunta do usuário pode vir em `$ARGUMENTS`. Sem ela, padrão: "Quais são os principais desvios de desempenho observados, suas possíveis explicações e as próximas verificações prioritárias?".
- Leia a auditoria e o catálogo de KPIs já gerados no projeto local. Contratos e objetivos do projeto **prevalecem** sobre exemplos do toolkit.
- O repositório contém **apenas métodos genéricos**. Contexto, resultados, nomes internos, medidas, filtros, DAX, dados e saídas ficam **somente no projeto autorizado**, nunca em GitHub público.
- Nunca modificar PBIX, DAX, fontes, relações, RLS, refresh, MCP, settings, credenciais, nem executar git add/commit/push ou uploads. Consultas MCP, se indispensáveis, apenas agregadas, pequenas e em operações inequivocamente de leitura.
- Não extrair linhas individuais nem dados pessoais. Não instalar dependências ou executar PowerShell.

## Sequência única de execução
1. **Reusar antes de recalcular.** Inspecione a existência e pertinência de:
   - `reports/powerbi-model-audit/` (mapeamento);
   - `reports/semantic-validation/01-catalogo-kpis.json` (contratos);
   - `reports/performance-diagnostics/01-achados.json` e síntese (diagnóstico).
   Se qualquer item estiver faltando, acione apenas a skill correspondente (`mapear-modelo`, `validar-indicadores`, `diagnosticar-desempenho`) **na mesma execução**, respeitando leitura apenas. Se estiver presente e adequado, reutilize. Se houver mudança explícita de versão/escopo que invalide o documento, atualize apenas etapa afetada; não faça auditoria completa desnecessária.
2. **Diagnóstico.** Se um diagnóstico local válido já foi gerado, verifique superficialmente a compatibilidade com os KPIs, a pergunta e o período. Não reexecute se puder reutilizar.
3. **Hipóteses.** Acione `hypothesis-investigator` com a skill `hypothesis-analysis` para obter até duas hipóteses concorrentes por achado relevante. Se subagentes não estiverem disponíveis, siga a skill diretamente.
4. **Prioridades.** Acione `opportunity-strategist` com a skill `action-prioritization`. Quando faltarem definições de negócio ou dados econômicos, priorize ações de validação e experimentos reversíveis, **nunca** investimento financeiro por ROI inventado.
5. **Primeira narrativa.** Acione `executive-storyteller` com `executive-storytelling` para produzir `onepage.md` e `onepage.html` estático. Use a referência visual `executive-storytelling/assets/onepage-template.html`, escapando texto dinâmico e eliminando campos não utilizados. Não deixar `{{PLACEHOLDERS}}` no documento final.
6. **Revisão crítica.** Acione `challenge-reviewer` com `evidence-review`; confronte cada afirmação e prioridade com contrato, achados e limites. Se encontrar problemas `blocker` ou `major`, faça **uma revisão** da OnePage. Não reinicie toda a orquestração; se o bloqueio persistir, mantenha rascunho claramente sinalizado e liste o problema.
7. **Encerramento.** Confirme que `reports/` está excluído de versionamento e grave localmente em `reports/market-intelligence/`:
   - `01-diagnostico-base.md` (ou referência ao diagnóstico anterior);
   - `02-hipoteses.md`;
   - `03-prioridades.md`;
   - `04-revisao-critica.md`;
   - `onepage.md`;
   - `onepage.html`;
   - `05-manifesto.md` (arquivos, data, KPI IDs, status, limitações e versões do fluxo).
   Não suba nada à nuvem, não publique HTML, não compartilhe dados sem autorização.

## Política de evidência
- `approved`: pode sustentar afirmação dentro do recorte aprovado; exigem-se fontes e períodos.
- `provisional` ou `restricted`: somente exploração. Restrito exige restrição verificada. Se não houver KPIs aprovados, a OnePage **obrigatoriamente** leva a marca **EXPLORATÓRIO — NÃO VALIDADO PARA DECISÃO EXECUTIVA** visível em tela e impressão.
- `rejected` e `blocked`: **NÃO usar** no diagnóstico/hipóteses/prioridades quantitativas.
- Não criar taxas de sinistro, margem, ROI, "oportunidade econômica", causalidade ou projeções sem bases apropriadas e aprovadas.
- Nunca converter uma hipótese em explicação confirmada; explicitar próximos testes.
- Não preencher lacunas com valores fictícios; use "Não disponível" ou omita o bloco.
- Não monte narrativa triunfalista; prefira uma decisão/checagem pequena e clara.

## Resposta final no Claude Code
Responda com:
1. Caminho para abrir `reports/market-intelligence/onepage.html` localmente.
2. Uma frase com o principal diagnóstico **e seu nível de confiança**.
3. Até três prioridades com ações táticas ou de investigação.
4. Três limitações principais.
5. Status da revisão e aviso de que não houve alteração no modelo.

O objetivo é **entregar um rascunho útil agora**, não alcançar perfeição metodológica. Se algo estiver bloqueado, entregue a melhor OnePage claramente condicionada pelos dados existentes, com lacunas explícitas e sem números fabricados.
