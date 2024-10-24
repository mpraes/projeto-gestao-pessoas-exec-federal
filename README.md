# Bem-vindo à Documentação do Projeto ETL Python - Dados Abertos Governo Federal - Gestão de Pessoas

## Introdução

Este projeto tem como objetivo extrair, transformar e carregar dados dos links do Portal de Dados Abertos do Governo Federal para o banco de dados do projeto ETL Python - Dados Abertos Governo Federal - Gestão de Pessoas.
Este é o link fonte com todos os dados em formato .ods: [Portal de Dados Abertos do Governo Federal - Gestão de Pessoas](https://dados.gov.br/dados/conjuntos-dados/gestao-de-pessoas-executivo-federal---cargos-vagos-e-vacancias)

## Modelagem de Dados

Para este projeto, utilizarei o banco de dados PostgreSQL estanciado no site render.com

Essa será a estrutura do banco de dados, modelagem star schema simples:

```mermaid
    Dim_Tempo {
        int ID_Tempo PK
        string Nome_Mes
        int Ano
        int Trimestre
        int Mes
        int Semana
    }

    Dim_Orgao {
        int ID_Orgao PK
        string Nome_Orgao
        string Sigla_Orgao
        string Categoria
    }

    Fato_Cargos {
        int ID_Orgao FK
        int ID_Tempo FK
        int Aprovada
        int Distribuida
        int Ocupada
        int Vagas
    }

    Fato_Cargos }|--|| Dim_Tempo : "ID_Tempo (FK)"
    Fato_Cargos }|--|| Dim_Orgao : "ID_Orgao (FK)"
```

## Tecnologias Utilizadas

- Python
- PostgreSQL
- Power BI

## Observações Finais

O projeto ainda está em desenvolvimento, e os dados do Portal de Dados Abertos do Governo Federal estão sendo atualizados constantemente, logo, é importante manter o projeto atualizado para não perder dados importantes.
Além disso, são diversos arquivos ods em links de períodos diferentes, logo preciso analisar se crio somente um etl para todos os dados ou faço um etl para cada período.