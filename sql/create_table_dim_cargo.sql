CREATE TABLE dim_cargo (
    id_cargo SERIAL PRIMARY KEY,
    nivel_escolaridade VARCHAR(50),
    plano_carreira VARCHAR(100),
    nome_cargo VARCHAR(255),
    codigo_cargo INTEGER,
    cargo_em_extincao CHAR(1) CHECK (cargo_em_extincao IN ('S', 'N')),
    data_inclusao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_alteracao TIMESTAMP
)