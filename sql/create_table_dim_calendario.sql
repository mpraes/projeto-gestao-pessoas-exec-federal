CREATE TABLE dim_calendario (
    id_tempo SERIAL PRIMARY KEY,
    ano_mes INTEGER NOT NULL,
    nome_mes VARCHAR(50),
    ano INTEGER NOT NULL,
    trimestre INTEGER,
    mes INTEGER,
    semana INTEGER,
)
