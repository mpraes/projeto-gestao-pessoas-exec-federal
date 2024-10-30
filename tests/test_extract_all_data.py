import pandas as pd
from app.extract.extract_all_data import adicionar_metadados_e_salvar, verificar_tipo_arquivo
from unittest.mock import Mock
import io
import pytest

# https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_202406.xlsx

# Teste para verificar o acesso ao link e identificar o formato do arquivo
@pytest.mark.parametrize("data, status_code_ods, status_code_xlsx, expected_link, expected_format", [
    ("202406", 404, 200, "https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_202406", "xlsx"),  # Link específico para .xlsx
])
def test_verificar_tipo_arquivo(mocker, data, status_code_ods, status_code_xlsx, expected_link, expected_format):
    # Mock de `requests.get` para simular respostas para .ods e .xlsx com conteúdo
    mock_get = mocker.patch("requests.get")

    # Configura o side_effect para simular .ods (404) e .xlsx (200 com conteúdo)
    mock_get.side_effect = [
        Mock(status_code=status_code_ods),  # Primeira chamada para .ods
        Mock(status_code=status_code_xlsx, content=io.BytesIO(b"conteudo xlsx").getvalue())  # Segunda chamada para .xlsx
    ]

    # Executa a função e verifica o resultado
    result = verificar_tipo_arquivo(data)
    assert result == (expected_link, expected_format)




# Teste para adicionar metadados e salvar o arquivo
def test_adicionar_metadados_e_salvar(mocker):
    # Criação de um DataFrame de exemplo para simular o comportamento
    mock_df = pd.DataFrame({'coluna': [1, 2, 3]})
    mock_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    # Mock da função validar_dados
    mocker.patch("app.extract.extract_all_data.validar_dados")  # Substitua 'my_module' pelo nome correto do seu módulo

    # Chama a função para adicionar metadados e salvar
    adicionar_metadados_e_salvar(mock_df, "202001", "xlsx")

    # Verifica se o DataFrame foi salvo como CSV
    mock_to_csv.assert_called_once_with(
        "C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data/202001.csv",
        index=False,
        encoding="utf-8-sig",
        sep=";"
    )

