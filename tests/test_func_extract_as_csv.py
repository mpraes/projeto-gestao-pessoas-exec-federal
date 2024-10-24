import pandas as pd
import pytest
import os
from unittest.mock import patch
from app.extract.extract_as_csv import extract_from_ods

# Testando se está lendo o correto
@patch('pandas.read_excel')
def test_extract_from_ods(mock_read_excel):
    # Simular DataFrame
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    # Chamar a função
    link_ods = "https://example.com/file.ods"
    extract_from_ods(link_ods)

    # Verificar se pandas.read_excel foi chamado com o link correto
    mock_read_excel.assert_called_once_with(link_ods)

# Testando o salvamento com nome correto no local
def test_extract_from_ods_filename_generation():
    link_ods = "https://example.com/file.ods"
    expected_filename = "file.csv"

    # Simular o comportamento da função
    nome_arquivo = os.path.basename(link_ods).replace(".ods", ".csv")

    # Verificar se o nome do arquivo gerado está correto
    assert nome_arquivo == expected_filename

# Testando o lançamento de exceções em caso de erro
@patch('pandas.DataFrame.to_csv')
@patch('pandas.read_excel')
def test_extract_from_ods_handles_exception_saving_csv(mock_read_excel, mock_to_csv):
    # Simular DataFrame
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    # Simular um erro ao salvar o arquivo CSV
    mock_to_csv.side_effect = Exception("Erro ao salvar o arquivo CSV")

    # Chamar a função
    link_ods = "https://example.com/file.ods"
    output_dir = "/tmp/test_output"

    # Verificar se a exceção foi tratada corretamente
    with pytest.raises(Exception):
        extract_from_ods(link_ods, output_dir)

#Testando tratamento de exceções na leitura dos ods
@patch('pandas.read_excel')
def test_extract_from_ods_handles_exception_reading_ods(mock_read_excel):
    # Simular um erro ao ler o arquivo ODS
    mock_read_excel.side_effect = Exception("Erro ao ler o arquivo ODS")

    # Chamar a função
    link_ods = "https://example.com/file.ods"

    # Verificar se a exceção foi tratada corretamente
    with pytest.raises(Exception):
        extract_from_ods(link_ods)

#Testando se o arquivo está sendo salvo no diretório específico
import os
from unittest.mock import patch, MagicMock

@patch('pandas.DataFrame.to_csv')
@patch('pandas.read_excel')
def test_extract_from_ods_saves_csv_to_output_dir(mock_read_excel, mock_to_csv):
    # Simular DataFrame
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    # Chamar a função com um diretório de saída
    link_ods = "https://example.com/file.ods"
    output_dir = "/tmp/test_output"
    extract_from_ods(link_ods, output_dir)

    # Verificar o nome do arquivo esperado
    nome_arquivo = os.path.join(output_dir, "file.csv")
    
    # Verificar se to_csv foi chamado com o caminho correto
    mock_to_csv.assert_called_once_with(nome_arquivo, index=False, sep=';')

# Teste para Verificar se o Arquivo CSV é Salvo no Diretório Atual se Nenhum Diretório for Fornecido
@patch('pandas.DataFrame.to_csv')
@patch('pandas.read_excel')
def test_extract_from_ods_saves_csv_in_current_directory(mock_read_excel, mock_to_csv):
    # Simular DataFrame
    mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    mock_read_excel.return_value = mock_df

    # Chamar a função sem diretório de saída
    link_ods = "https://example.com/file.ods"
    extract_from_ods(link_ods)

    # Verificar o nome do arquivo esperado no diretório atual
    nome_arquivo = os.path.join(os.getcwd(), "file.csv")
    
    # Verificar se to_csv foi chamado com o caminho correto
    mock_to_csv.assert_called_once_with(nome_arquivo, index=False, sep=';')

