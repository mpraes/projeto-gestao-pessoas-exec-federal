import pandas as pd
from pydantic import BaseModel, ValidationError, create_model

def criar_modelo_dinamico(df):
    # Define os tipos padrão para cada coluna, se existirem no DataFrame
    campos = {
        'ANO_MES': (str, 'N/A'), 
        'ORGAO': (int, 0), 
        'NOME_ORGAO': (str, 'N/A'), 
        'SIGLA_ORGAO': (str, 'N/A'),
        'NIVEL': (str, 'N/A'), 
        'CARGO': (int, 0), 
        'NOME_CARGO': (str, 'N/A'), 
        'APROVADA': (int, 0), 
        'DISTRIBUIDA': (int, 0),
        'OCUPADA': (int, 0), 
        'VAGA': (int, 0), 
        'VACANCIA_POR_EXONERACAO': (int, 0), 
        'VACANCIA_POR_DEMISSAO': (int, 0), 
        'VACANCIA_POR_PROMOCAO': (int, 0),
        'VACANCIA_POR_READAPTACAO': (int, 0), 
        'VACANCIA_POR_APOSENTADORIA': (int, 0), 
        'VACANCIA_POR_POSSE_CARGO_INAC': (int, 0), 
        'VACANCIA_POR_FALECIMENTO': (int, 0),
        'CARGO_EM_EXTINCAO': (str, 'N/A'), 
        'PLANO_CARREIRA': (str, 'N/A'),
        'VAGO': (int, 0)
    }
    
    # Filtra campos para incluir apenas as colunas que estão presentes no DataFrame
    campos_presentes = {col: campos[col] for col in df.columns if col in campos}
    
    # Cria dinamicamente um modelo Pydantic com os campos presentes
    ModeloDinamico = create_model('ModeloDinamico', **{k: (v[0], ...) for k, v in campos_presentes.items()})
    return ModeloDinamico, campos_presentes

def validar_dados(df):
    # Verificar se uma das colunas 'VAGA' ou 'VAGO' existe e renomeá-la para 'VAGA' se necessário
    if 'VAGO' in df.columns and 'VAGA' not in df.columns:
        df.rename(columns={'VAGO': 'VAGA'}, inplace=True)

    # Criar o modelo dinâmico com base nas colunas presentes
    ModeloDinamico, campos_presentes = criar_modelo_dinamico(df)

    # Preencher valores nulos nas colunas presentes com os valores padrão
    for col, (tipo, valor_padrao) in campos_presentes.items():
        df.fillna({col:valor_padrao}, inplace=True)

    # Valida cada linha do DataFrame com o modelo dinâmico
    try:
        for index, row in df.iterrows():
            # Cria uma instância do modelo dinâmico com os dados da linha
            contrato = ModeloDinamico(**row.to_dict())
        print("Todos os dados foram validados com sucesso!")
    except ValidationError as e:
        print(f"Erro de validação: {e}")

# Exemplo de uso com um DataFrame dinâmico
# df = pd.DataFrame(...)  # Substitua pelo seu DataFrame carregado
# validar_dados(df)
