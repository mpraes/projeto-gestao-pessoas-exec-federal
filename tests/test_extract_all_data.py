import pytest
from unittest.mock import Mock
import pandas as pd
from app.extract.extract_all_data import verificar_tipo_arquivo, adicionar_metadados_e_salvar  # Substitua 'my_module' pelo nome correto do seu módulo

# Teste para adicionar metadados e salvar o arquivo
def test_adicionar_metadados_e_salvar(mocker):
    # Criação de um DataFrame de exemplo para simular o comportamento
    mock_df = pd.DataFrame({'coluna': [1, 2, 3]})
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    # Mock da função validar_dados
    mocker.patch("app.extract.extract_all_data.validar_dados")  # Substitua 'my_module' pelo nome correto do seu módulo

    # Chama a função para adicionar metadados e salvar
    adicionar_metadados_e_salvar(mock_df, "201703", "xlsx")

    # Verifica se o DataFrame foi salvo como CSV
    mock_to_csv.assert_called_once_with(
        "C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data/201703.csv",
        index=False,
        encoding="utf-8-sig",
        sep=";"
    )