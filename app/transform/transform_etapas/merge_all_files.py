import pandas as pd

def merge_all_files(data: str) -> pd.DataFrame:
    df = pd.read_csv(f"data/{data}.csv", sep=";")
    df = pd.concat([df, pd.read_csv(f"data/{data}_2.csv", sep=";")], ignore_index=True)
    return df


def remover_colunas_fixas(df):
    """
    Remove colunas específicas do DataFrame.
    
    Args:
        df: DataFrame original
        
    Returns:
        DataFrame sem as colunas removidas
    """
    # Lista de colunas para remover
    colunas_remover = [
        'AMBIENTE_EXECUCAO',
        'VERSAO_SCRIPT',
        'RESPONSAVEL',
        'DATA_ACESSO',
        'FORMATO_ORIGEM',
        'PERIODICIDADE',
        'DATA_CARGA', 
        'FONTE',
        'TEMA',
        'CLIENTE'

        # Adicione ou remova colunas conforme necessário
    ]
    
    # Cria uma cópia do DataFrame
    df_limpo = df.copy()
    
    # Remove apenas as colunas que existem no DataFrame
    colunas_existentes = [col for col in colunas_remover if col in df_limpo.columns]
    
    if colunas_existentes:
        df_limpo = df_limpo.drop(columns=colunas_existentes)
        print(f"Colunas removidas: {colunas_existentes}")
    else:
        print("Nenhuma das colunas especificadas foi encontrada no DataFrame")
    
    return df_limpo