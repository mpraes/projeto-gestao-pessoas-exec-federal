CREATE TABLE dim_orgao (
    ID_Orgao SERIAL PRIMARY KEY,
    Nome_Orgao VARCHAR(255) NOT NULL,
    Sigla_Orgao VARCHAR(10),
    Data_Inclusao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Data_Alteracao TIMESTAMP
)
