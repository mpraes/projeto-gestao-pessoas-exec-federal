import requests
from datetime import datetime

def verificar_disponibilidade_arquivo(data):
    link_opcao1 = f"https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20{data}"
    link_opcao2 = f"https://repositorio.dados.gov.br/segrt/cargos%20vagos%20e%20vacancia/CargosVagosVacancias_{data}"
    link_opcao3 = f"https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas_{data}"

    # Lista de opções para verificar
    opcoes = [
        (link_opcao1, "Opção 1"),
        (link_opcao2, "Opção 2"),
        (link_opcao3, "Opção 3")
    ]
    
    # Percorre as opções e verifica se o arquivo existe (ods ou xlsx)
    for link, tipo in opcoes:
        response_ods = requests.get(f"{link}.ods")
        if response_ods.status_code == 200:
            print(f"Acesso bem-sucedido: Arquivo .ods encontrado ({tipo}) para a data {data}")
            return {
                "status": "acessado",
                "formato": "ods",
                "opcao_link": link,
                "data": data,
                "data_hora_acesso": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        response_xlsx = requests.get(f"{link}.xlsx")
        if response_xlsx.status_code == 200:
            print(f"Acesso bem-sucedido: Arquivo .xlsx encontrado ({tipo}) para a data {data}")
            return {
                "status": "acessado",
                "formato": "xlsx",
                "opcao_link": link,
                "data": data,
                "data_hora_acesso": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    # Caso nenhum link tenha sido encontrado
    print(f"Nenhum arquivo encontrado para {data}.")
    return {
        "status": "não encontrado",
        "formato": None,
        "opcao_link": None,
        "data": data,
        "data_hora_acesso": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }