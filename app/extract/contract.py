from pydantic import BaseModel, field_validator, Field, ValidationError
from datetime import datetime
from typing import Optional

class DataContrato(BaseModel):
    ANO_MES: str
    ORGAO: int
    NOME_ORGAO: str
    SIGLA_ORGAO: str
    NIVEL: str
    CARGO: int
    NOME_CARGO: str
    APROVADA: int
    DISTRIBUIDA: int
    OCUPADA: int
    VAGO: int
    VACANCIA_POR_EXONERACAO: int
    VACANCIA_POR_DEMISSAO: int
    VACANCIA_POR_PROMOCAO: int
    VACANCIA_POR_READAPTACAO: int
    VACANCIA_POR_APOSENTADORIA: int
    VACANCIA_POR_POSSE_CARGO_INAC  : int
    VACANCIA_POR_FALECIMENTO: int

def validar_dados(df):
    try:
        # Validar cada linha do DataFrame com o modelo DataContrato
        for index, row in df.iterrows():
            contrato = DataContrato(**row.to_dict())
        print("Todos os dados foram validados com sucesso!")
    except ValidationError as e:
        print(f"Erro de validação: {e}")