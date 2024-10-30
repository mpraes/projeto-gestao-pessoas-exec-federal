import pandas as pd

lista_datas = 

def cria_dimensao_orgao(data)

df  = pd.read_csv(r"C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data/201601.csv", encoding='utf-8', sep=";")
# Selecionar colunas e obter valores únicos
df_distinct = df[['ORGAO', 'NOME_ORGAO', 'SIGLA_ORGAO']].drop_duplicates()

# Exibir o resultado
print(df_distinct.sample(10))


