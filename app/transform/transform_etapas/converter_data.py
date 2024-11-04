import pandas as pd
from datetime import datetime

def converter_data(df, coluna='ANO_MES'):
    """
    Converte a coluna de data do dataframe que está em diferentes formatos para o padrão YYYY-MM-DD
    
    Formatos aceitos de entrada:
    - 'mmm YYYY' (ex: 'dez 2016')
    - int ou str no formato YYYYMM (ex: 202002)
    
    Args:
        df: DataFrame com a coluna de data
        coluna: Nome da coluna que contém as datas (padrão: 'ANO_MES')
    
    Returns:
        DataFrame com a coluna convertida
    """
    
    # Dicionário para mapear nomes dos meses em português para números
    meses = {
        'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04', 'mai': '05', 'jun': '06',
        'jul': '07', 'ago': '08', 'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
    }
    
    def converter_valor(valor):
        try:
            # Se for inteiro, converte para string
            if isinstance(valor, (int, float)):
                valor = str(int(valor))  # Converte para int primeiro para remover decimais
            
            # Agora valor é string, remove espaços extras
            valor = str(valor).strip()
            
            # Verifica se está no formato 'YYYYMM' (como string ou número)
            if valor.isdigit() and len(valor) == 6:
                ano = valor[:4]
                mes = valor[4:]
                return f"{ano}-{mes}-01"
            
            # Verifica se está no formato 'mmm YYYY'
            elif ' ' in valor:
                mes, ano = valor.split()
                mes = mes.lower()[:3]  # Pega apenas as 3 primeiras letras e converte para minúsculo
                if mes in meses:
                    return f"{ano}-{meses[mes]}-01"
            
            raise ValueError(f"Formato de data não reconhecido: {valor}")
            
        except Exception as e:
            print(f"Erro ao converter valor '{valor}': {str(e)}")
            return None
    
    # Faz uma cópia do DataFrame para não modificar o original
    df_novo = df.copy()
    
    # Aplica a conversão na coluna
    df_novo[coluna] = df_novo[coluna].apply(converter_valor)
    
    # Converte a coluna para datetime
    df_novo[coluna] = pd.to_datetime(df_novo[coluna])
    
    return df_novo



