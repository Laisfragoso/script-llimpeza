Script de Manutenção e Limpeza Automatizada (SecOps)  
    Este repositório contém uma ferramenta de automação desenvolvida em Python para a manutenção proativa de diretórios temporários. 
    O foco principal é a eficiência operacional e a redução de riscos, garantindo que arquivos antigos sejam removidos de forma segura e auditável.  

   🚀 Diferenciais Técnicos (Sênior Level)Diferente de scripts simples, esta versão foi construída seguindo princípios de Clean Code e DevSecOps:  
       Manipulação Segura de Path: Utiliza a biblioteca pathlib para garantir compatibilidade e segurança no tratamento de caminhos em sistemas Unix/Linux.    
       Logging para SOC/SIEM: Implementação completa de logs via biblioteca logging, permitindo a rastreabilidade de todas as ações de exclusão (essencial para trilhas de auditoria e conformidade ISO 27001).    
       Modo de Simulação (Dry Run): Recurso de segurança que permite visualizar o impacto da limpeza antes da execução real, mitigando o risco de deleção acidental de dados críticos.    
       Gestão de Timezone: Uso de UTC para cálculos de retenção, evitando erros de fuso horário em ambientes multicloud (AWS/Azure).    
   🛠️ Tecnologias Utilizadas Linguagem: Python 3.12+Linters/Formatadores: Ruff e Black (Garantia de padronização PEP 8)
       Security Scan: Bandit (Análise estática de vulnerabilidades no código)
