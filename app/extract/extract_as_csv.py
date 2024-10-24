import pandas as pd
import os

def extract_from_ods(link_ods: str, output_dir: str = None):
    """
    Extrai os dados em formato Ods do link fornecido e salva em um arquivo csv, gerando um nome de arquivo a partir do link.
    """
        # Lê o arquivo ODS
    try:
        df = pd.read_excel(link_ods)
    except Exception as e:
        print(f"Erro ao ler o arquivo ODS: {e}")
        raise e
    # Extrai o nome do arquivo a partir do link
    nome_arquivo = os.path.basename(link_ods).replace(".ods", ".csv")
        # Define o diretório de saída dinamicamente
    if output_dir:
        caminho_saida = os.path.join(output_dir, nome_arquivo)
    else:
        caminho_saida = os.path.join(os.getcwd(), nome_arquivo)
        # Salva o arquivo CSV
    try:
        df.to_csv(caminho_saida, index=False, sep=';')
        print(f'Arquivo salvo com sucesso em {caminho_saida}')
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')
        raise e
    

if __name__ == "__main__":
    link_ods = "https://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20201601.ods"
    
    # Exemplo de uso com diretório de saída
    output_dir = "C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data"
    extract_from_ods(link_ods, output_dir)

