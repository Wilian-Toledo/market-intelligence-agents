# Segurança e governança

Este repositório é público e contém somente **framework genérico**. Não faça commit de arquivos corporativos nem inclua configurações específicas da máquina.

## Nunca subir
PBIX/PBIP, DAX proprietários, nomes internos e estruturas sensíveis, dados de clientes, segurados, apólices ou sinistros; bases extraídas, relatórios de auditoria, `.mcp.json`, tokens, secrets e credenciais.

## Controles
- Obtenha autorização corporativa para o uso do GitHub pessoal e ferramentas de IA.
- Consulte apenas o modelo autorizado e somente via operações de leitura.
- Considere que **metadados e resultados podem ser transmitidos ao provedor de IA**; não os trate como inofensivos.
- Grave saídas específicas da empresa localmente em `reports/powerbi-model-audit/`, ignorado pelo Git do projeto.
- Não execute git push, deploy, upload ou configuração de integrações automaticamente.
- Revise mudanças de scripts antes de atualizar a versão instalada.
