import pandas as pd
import pytest
from pydantic import ValidationError
from app.extract.extracao_etapas.contract import criar_modelo_dinamico, validar_dados  # Substitua 'seu_script' pelo nome do seu arquivo

def test_criar_modelo_dinamico():
    # Cria um DataFrame de exemplo
    data = {
        'ANO_MES': ['2024-10'],
        'ORGAO': [123],
        'NOME_ORGAO': ['Ministério da Saúde'],
        'SIGLA_ORGAO': ['MS'],
        'NIVEL': ['Federal'],
        'CARGO': [456],
        'APROVADA': [1],
        'DISTRIBUIDA': [0],
        'OCUPADA': [1],
        'VAGA': [0]
    }
    df = pd.DataFrame(data)

    # Executa a função para criar o modelo dinâmico
    ModeloDinamico, campos_presentes = criar_modelo_dinamico(df)

    # Verifica se o modelo dinâmico foi criado com os campos esperados
    assert 'ANO_MES' in campos_presentes
    assert 'ORGAO' in campos_presentes
    assert 'NOME_ORGAO' in campos_presentes
    assert 'SIGLA_ORGAO' in campos_presentes
    assert 'NIVEL' in campos_presentes
    assert 'CARGO' in campos_presentes
    assert 'VAGA' in campos_presentes
    assert campos_presentes['ANO_MES'][1] == 'N/A'  # Valor padrão para ANO_MES
    assert campos_presentes['ORGAO'][1] == 0  # Valor padrão para ORGAO

def test_validar_dados_com_sucesso():
    # Cria um DataFrame válido
    data = {
        'ANO_MES': ['2024-10'],
        'ORGAO': [123],
        'NOME_ORGAO': ['Ministério da Saúde'],
        'SIGLA_ORGAO': ['MS'],
        'NIVEL': ['Federal'],
        'CARGO': [456],
        'APROVADA': [1],
        'DISTRIBUIDA': [0],
        'OCUPADA': [1],
        'VAGA': [0]
    }
    df = pd.DataFrame(data)

    # Verifica se a função de validação funciona sem erros para um DataFrame válido
    try:
        validar_dados(df)
        assert True  # A validação foi bem-sucedida
    except ValidationError:
        assert False  # Não deveria ocorrer um erro de validação

def test_validar_dados_com_erro():
    # Cria um DataFrame inválido (coluna 'ORGAO' com valor de tipo incorreto)
    data = {
        'ANO_MES': ['2024-10'],
        'ORGAO': ['texto_incorreto'],  # Deve ser int
        'NOME_ORGAO': ['Ministério da Saúde'],
        'SIGLA_ORGAO': ['MS'],
        'NIVEL': ['Federal'],
        'CARGO': [456],
        'APROVADA': [1],
        'DISTRIBUIDA': [0],
        'OCUPADA': [1],
        'VAGA': [0]
    }
    df = pd.DataFrame(data)

    # Verifica se a função de validação lança um erro de ValidationError
    with pytest.raises(ValidationError):
        validar_dados(df)
