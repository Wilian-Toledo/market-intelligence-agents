---
name: mapear-modelo
description: "Mapeia e audita, sem alterar, o modelo semântico Power BI aberto usando o MCP já configurado no projeto."
argument-hint: "[nome opcional do modelo]"
---

# Auditoria inicial do modelo Power BI

Você é o orquestrador desta etapa.

1. Verifique que o PBIX autorizado está aberto e identifique o MCP de Power BI existente; **não crie, instale ou reconfigure** integrações.
2. Confirme o modelo correto. Havendo mais de um, solicite seleção ao usuário.
3. Prefira conexão MCP somente leitura. Mesmo que o modo não seja comprovado, utilize **somente operações claramente de leitura**; registre a limitação.
4. Delegue ao subagente `model-cartographer`, que seguirá a skill `powerbi-semantic-audit`. Se delegação não existir, execute essa skill no contexto principal.
5. Nunca modifique modelo, PBIX, DAX, fontes, RLS, relacionamentos ou permissões. Não consulte registros pessoais nem faça commits, pushes ou uploads.
6. Produza os cinco relatórios somente em `reports/powerbi-model-audit/`; confirme proteção pelo `.gitignore` antes de escrever.
7. Retorne um resumo agregado da cobertura, indicadores encontrados, riscos, testes realizados e perguntas de negócio. Não gere OnePage nem previsão ainda.

Se a integração MCP falhar, descreva o bloqueio e pare, sem fingir que inspecionou o modelo.
