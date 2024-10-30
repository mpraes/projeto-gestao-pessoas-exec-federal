import pytest
import requests_mock
from app.extract.extracao_etapas.verificar_links import verificar_disponibilidade_arquivo  # Substitua 'seu_script' pelo nome do seu arquivo

def test_verificar_disponibilidade_arquivo_ods_encontrado():
    data = "2024-10-30"
    link_base = f"https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20{data}"
    
    # Usando requests-mock para simular a resposta da requisição
    with requests_mock.Mocker() as m:
        m.get(f"{link_base}.ods", status_code=200)  # Simula que o arquivo .ods foi encontrado
        m.get(f"{link_base}.xlsx", status_code=404)  # Simula que o arquivo .xlsx não foi encontrado
        
        # Executa a função
        resultado = verificar_disponibilidade_arquivo(data)
        
        # Verifica o resultado
        assert resultado["status"] == "acessado"
        assert resultado["formato"] == "ods"
        assert resultado["opcao_link"] == link_base  # Verifica o link base sem extensão
        assert resultado["data"] == data
        assert "data_hora_acesso" in resultado  # Verifica se o campo data_hora_acesso existe

def test_verificar_disponibilidade_arquivo_nao_encontrado():
    data = "2024-10-30"
    link_base1 = f"https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20{data}"
    link_base2 = f"https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_{data}"
    link_base3 = f"https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas_{data}"
    
    # Usando requests-mock para simular a resposta da requisição
    with requests_mock.Mocker() as m:
        m.get(f"{link_base1}.ods", status_code=404)  # Simula que o arquivo .ods não foi encontrado
        m.get(f"{link_base1}.xlsx", status_code=404)  # Simula que o arquivo .xlsx não foi encontrado
        m.get(f"{link_base2}.ods", status_code=404)  # Simula que o arquivo .ods não foi encontrado
        m.get(f"{link_base2}.xlsx", status_code=404)  # Simula que o arquivo .xlsx não foi encontrado
        m.get(f"{link_base3}.ods", status_code=404)  # Simula que o arquivo .ods não foi encontrado
        m.get(f"{link_base3}.xlsx", status_code=404)  # Simula que o arquivo .xlsx não foi encontrado
        
        # Executa a função
        resultado = verificar_disponibilidade_arquivo(data)
        
        # Verifica o resultado
        assert resultado["status"] == "não encontrado"
        assert resultado["formato"] is None
        assert resultado["opcao_link"] is None
        assert resultado["data"] == data
        assert "data_hora_acesso" in resultado  # Verifica se o campo data_hora_acesso existe
