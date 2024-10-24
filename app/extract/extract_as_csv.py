import pandas as pd

def extract_from_ods(link_ods: str):
    """
    Extrai os dados em formato Ods do link fornecido e salva em um arquivo csv
    """
    df = pd.read_excel(link_ods)
    print(df)

if __name__ == "__main__":
    link_ods = "https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20201601.ods"
    extract_from_ods(link_ods)

