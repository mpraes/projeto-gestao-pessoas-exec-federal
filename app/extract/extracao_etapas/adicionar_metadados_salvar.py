from datetime import datetime
import pandas as pd
from extracao_etapas.contract import validar_dados

def adicionar_metadados_e_salvar(df, data, formato_arquivo, data_acesso):
    # Adiciona os metadados ao DataFrame
    """
    Adiciona metadados ao DataFrame fornecido e salva-o como um arquivo CSV.

    Esta função insere várias colunas de metadados no DataFrame, como 'Cliente', 'Tema',
    'Fonte', 'Data Carga', entre outros. Em seguida, valida os dados do DataFrame utilizando
    a função `validar_dados` e salva o DataFrame como um arquivo CSV nomeado com a data fornecida.

    Parâmetros:
    - df (pd.DataFrame): O DataFrame ao qual os metadados serão adicionados.
    - data (str): String representando a data, utilizada para nomear o arquivo CSV de saída.

    Retorno:
    - None: A função salva o DataFrame como um arquivo CSV no diretório atual e não retorna nada.
    """
    df['CLIENTE'] = "governo federal"
    df['TEMA'] = "cargos e vacancias"
    df['FONTE'] = "https://dados.gov.br/dados/conjuntos-dados/gestao-de-pessoas-executivo-federal---cargos-vagos-e-vacancias"
    df['DATA_CARGA'] = datetime.now().strftime('%Y-%m-%d')
    df['DATA_ACESSO'] = data_acesso
    df['FORMATO_ORIGEM'] = formato_arquivo
    df['PERIODICIDADE'] = "Mensal"
    df['RESPONSAVEL'] = "Automação de Script"
    df['VERSAO_SCRIPT'] = "1.0"
    df['AMBIENTE_EXECUCAO'] = "Produção"

    # Validar o DataFrame usando pydantic
    validar_dados(df)

    # Salva o DataFrame como CSV
    try: 
        #Esse caminho está fixado, porém precisa ser dinamico conforme o ambiente em que estiver executando o script          
        nome_arquivo = f"data/{data}.csv"
        df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig', sep=';')
        print(f"Arquivo salvo como {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")