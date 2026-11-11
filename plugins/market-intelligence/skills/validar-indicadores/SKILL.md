---
name: validar-indicadores
description: "Classifica e estabelece contratos de KPIs a partir de auditoria existente, para uso seguro em diagnósticos exploratórios e relatórios executivos."
argument-hint: "[questão analítica ou conjunto de indicadores]"
---

# Validar indicadores — comando v0.2

Use a skill `semantic-validator` como método de trabalho. Este comando **não** cria um novo agente nem substitui o mapeador.

1. Identifique a pergunta analítica em `$ARGUMENTS`, se houver; caso contrário, use "diagnóstico de desempenho e comparação de crescimento/participação".
2. Leia **localmente** a auditoria atual em `reports/powerbi-model-audit/`, se existir, especialmente resumo, dicionário, riscos/testes e pendências. Não compartilhe nem publique arquivos.
3. Identifique as definições confirmadas pelo usuário; qualquer definição ausente deve continuar `pending`. Não invente natureza de receita, sinistro, competência ou grupo econômico.
4. Selecione um conjunto pequeno (até 12) de indicadores de maior utilidade e valide conforme `semantic-validator`, em leitura apenas; aproveite evidências já presentes e faça novas consultas MCP agregadas só se forem necessárias e autorizadas. Nunca modificar o PBIX.
5. Classifique indicadores com status `approved`, `provisional`, `restricted`, `rejected` ou `blocked`. Não permita `approved` por inspeção sintática ou sem validação de negócio.
6. Gere exclusivamente arquivos locais em `reports/semantic-validation/`, preservando os relatórios originais. Use o contrato JSON da skill e, **se Python estiver disponível e permitido**, rode seu verificador local; caso contrário, confira manualmente e informe.
7. Responda com contagem por status, indicadores que podem suportar exploração, indicadores vetados e três decisões pendentes mais importantes. Não gere OnePage, projeções ou correções neste comando.

Se a auditoria não existir, explique e recomende `/mapear-modelo`. Se não for possível estabelecer evidência suficiente, retorne um diagnóstico **bloqueado**, sem improvisar resultados.
