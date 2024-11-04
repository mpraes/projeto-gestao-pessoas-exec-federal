import pandas as pd
import pandas as pd
import numpy as np

def tratar_nulos(df, metodo='relatorio', **kwargs):
    """
    Analisa e trata valores nulos em um DataFrame.
    
    Args:
        df: DataFrame a ser analisado/tratado
        metodo: Tipo de operação a ser realizada
            - 'relatorio': Apenas gera relatório de nulos (default)
            - 'remover_linhas': Remove linhas com nulos
            - 'remover_colunas': Remove colunas com nulos
            - 'preencher': Preenche nulos conforme estratégia
        **kwargs:
            - limite_nulos: % máximo de nulos permitido em uma coluna (0 a 100)
            - estrategia: Dicionário com estratégia de preenchimento por coluna
            
    Returns:
        DataFrame tratado ou relatório de nulos
    """
    
    def gerar_relatorio(df):
        """Gera relatório detalhado sobre valores nulos"""
        total_registros = len(df)
        
        relatorio = pd.DataFrame({
            'tipo_dados': df.dtypes,
            'total_nulos': df.isnull().sum(),
            'pct_nulos': (df.isnull().sum() / total_registros * 100).round(2),
            'valores_unicos': df.nunique(),
            'amostra_valores': df.apply(lambda x: list(x.dropna().unique())[:3])
        })
        
        # Ordena pelo percentual de nulos (decrescente)
        relatorio = relatorio.sort_values('pct_nulos', ascending=False)
        
        # Adiciona total de registros ao relatório
        relatorio.loc['RESUMO'] = ['', 
                                 df.isnull().sum().sum(),
                                 (df.isnull().sum().sum() / (total_registros * len(df.columns)) * 100).round(2),
                                 '',
                                 f'Total Registros: {total_registros}']
        
        return relatorio
    
    def remover_colunas_nulos(df, limite_nulos=None):
        """Remove colunas com nulos acima do limite especificado"""
        if limite_nulos is None:
            return df.dropna(axis=1)
        
        pct_nulos = (df.isnull().sum() / len(df) * 100).round(2)
        colunas_manter = pct_nulos[pct_nulos <= limite_nulos].index
        return df[colunas_manter]
    
    def preencher_nulos(df, estrategia=None):
        """Preenche valores nulos conforme estratégia definida"""
        df_tratado = df.copy()
        
        # Se não houver estratégia definida, usa estratégia padrão
        if estrategia is None:
            estrategia = {}
            for coluna in df.columns:
                if df[coluna].dtype in ['int64', 'float64']:
                    estrategia[coluna] = 'media'
                elif df[coluna].dtype == 'datetime64[ns]':
                    estrategia[coluna] = 'ffill'
                elif df[coluna].dtype == 'object' or df[coluna].dtype == 'string':
                    estrategia[coluna] = 'N/A'  
                else:
                    estrategia[coluna] = 'moda'
        
        # Aplica a estratégia para cada coluna
        for coluna, metodo in estrategia.items():
            if coluna not in df.columns:
                continue
                
            if metodo == 'media':
                valor = df[coluna].mean()
            elif metodo == 'mediana':
                valor = df[coluna].median()
            elif metodo == 'moda':
                valor = df[coluna].mode()[0] if not df[coluna].mode().empty else None
            elif metodo == 'zero':
                valor = 0
            elif metodo == 'ffill':
                df_tratado[coluna] = df_tratado[coluna].fillna(method='ffill')
                continue
            elif metodo == 'bfill':
                df_tratado[coluna] = df_tratado[coluna].fillna(method='bfill')
                continue
            else:
                valor = metodo
            
            df_tratado[coluna] = df_tratado[coluna].fillna(valor)
            
        return df_tratado
    
    # Executa o método solicitado
    if metodo == 'relatorio':
        return gerar_relatorio(df)
    
    elif metodo == 'remover_linhas':
        return df.dropna()
    
    elif metodo == 'remover_colunas':
        limite_nulos = kwargs.get('limite_nulos')
        return remover_colunas_nulos(df, limite_nulos)
    
    elif metodo == 'preencher':
        estrategia = kwargs.get('estrategia')
        return preencher_nulos(df, estrategia)
    
    else:
        raise ValueError(f"Método '{metodo}' não reconhecido")
