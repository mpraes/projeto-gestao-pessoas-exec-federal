---

# 📊 **Projeto ETL Python - Dados Abertos Governo Federal - Gestão de Pessoas** 🇧🇷

## 🚀 **Introdução**

Este projeto visa a **extração**, **transformação** e **carga** (ETL) de dados do Portal de Dados Abertos do Governo Federal, com foco na análise de cargos vagos e vacâncias no executivo federal.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python** para a automação do ETL
- **PostgreSQL** como banco de dados final para armazenar as tabelas de análise
- **Power BI** para criação de dashboards e monitoramento de KPIs

## 📝 **Passos do Projeto**

1. **Estruturação do projeto** - Concluído ✅
2. **Modelagem e criação de tabelas** - Concluído ✅
3. **Extração e transformação dos arquivos** - Em Andamento 🕑


---

## 📈 **Próximos Passos: Carga no PostgreSQL**

1. **Preparação da Área de Staging**:
   - Configure tabelas temporárias e esquemas necessários para acomodar os dados inicialmente.

2. **Carga dos Dados**:
   - Implemente o processo de inserção para garantir consistência e evitar duplicação de dados.
   
3. **Otimização do Desempenho**:
   - Crie índices nas tabelas para acelerar consultas.
   - Programe a carga incremental para atualizações periódicas.

---

# 🌎 **Project Documentation - Federal Executive Human Resource Management**

## **Introduction**

This project focuses on ETL processes to **extract**, **transform**, and **load** data from the Brazilian Government Open Data Portal, specifically analyzing vacancies within the federal executive branch.

## **Technologies Used**

- **Python** for ETL automation
- **PostgreSQL** as the final database for analysis tables
- **Power BI** for dashboards and KPI monitoring

## **Project Steps**

1. **Project setup** - Completed ✅
2. **Data Modeling and Table Creation** - Completed ✅
3. **Data Extraction and Transformation** - Ongoing 🕑

---

## 📈 **Next Steps: PostgreSQL Data Loading**

1. **Staging Area Preparation**:
   - Set up temporary tables and schemas to stage incoming data.

2. **Data Loading**:
   - Implement insertion processes ensuring data consistency and avoiding duplication.

3. **Performance Optimization**:
   - Index tables to speed up querying.
   - Schedule incremental loads for periodic updates. 

---
## Desenho do fluxo e modelagem

Para este projeto, utilizarei o banco de dados PostgreSQL estanciado no site render.com

Essa será a estrutura do banco de dados, modelagem star schema simples:

![diagramaer](https://github.com/user-attachments/assets/6711f9f5-2560-4de5-a577-e84d2caa92c2)


![fluxo](https://github.com/user-attachments/assets/8093ceab-fa77-48c8-9e4f-36210cece445)


Claro! Vou ajustar a documentação mantendo o foco no fluxo e modelagem, enquanto destacamos a estrutura e os próximos passos para a carga no PostgreSQL.
