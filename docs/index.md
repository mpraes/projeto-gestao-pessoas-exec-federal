# Bem-vindo à Documentação do Projeto ETL Python - Dados Abertos Governo Federal - Gestão de Pessoas

## Introdução

Este projeto tem como objetivo extrair, transformar e carregar dados dos links do Portal de Dados Abertos do Governo Federal para o banco de dados do projeto ETL Python - Dados Abertos Governo Federal - Gestão de Pessoas.
Este é o link fonte com todos os dados em formato .ods: [Portal de Dados Abertos do Governo Federal - Gestão de Pessoas](https://dados.gov.br/dados/conjuntos-dados/gestao-de-pessoas-executivo-federal---cargos-vagos-e-vacancias)

## Modelagem de Dados

Para este projeto, utilizarei o banco de dados PostgreSQL estanciado no site render.com

Essa será a estrutura do banco de dados, modelagem star schema simples:

```mermaid
erDiagram
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

Obs: Todas as tecnologias citadas acima são de código aberto, onde o custo para o projeto tende a ser mínimo.

## Fluxo de Dados

```mermaid
    flowchart TD
        A[ODS Files on Website] --> B[Apply Data Contract]
        B --> C{Contract Valid?}
        
        C -- Yes --> D[Extract Data]
        D --> E[Test Data]
        E --> F[Validate Data]
    F --> G{Is Data Valid?}
    
    G -- Yes --> H[Transform Data]
    H --> I[Load Data into PostgreSQL]
    
    G -- No --> J[Log Errors]
    C -- No --> K[Reject Data & Log Issues]

    subgraph DataFlowProcess
        D --> E
        E --> F
        F --> G
        G --> H
        H --> I
        G --> J
        C --> K
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#0f0,stroke:#333,stroke-width:2px
    style I fill:#bbf,stroke:#333,stroke-width:2px
    style J fill:#faa,stroke:#333,stroke-width:2px
    style K fill:#faa,stroke:#333,stroke-width:2px
```

## Observações Finais

O projeto ainda está em desenvolvimento, e os dados do Portal de Dados Abertos do Governo Federal estão sendo atualizados constantemente, logo, é importante manter o projeto atualizado para não perder dados importantes.
Além disso, são diversos arquivos ods em links de períodos diferentes, logo preciso analisar se crio somente um etl para todos os dados ou faço um etl para cada período.

## Passos do Projeto

1. Estruturação do projeto (em andamento)