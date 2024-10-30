from extracao_etapas.limpar_diretorio import deletar_todos_arquivos
from extracao_etapas.verificar_links import verificar_disponibilidade_arquivo
from extracao_etapas.extrair_dados_arquivos import acessar_arquivos_extrair_dados
from extracao_etapas.adicionar_metadados_salvar import adicionar_metadados_e_salvar
import json
from datetime import datetime, timedelta

#Configurando dinamicamente o mês anterior
def mes_passado():
    # Pega a data de hoje e define o primeiro dia do mês atual
    hoje = datetime.today().replace(day=1)
    # Subtrai um dia para ir para o último dia do mês anterior
    mes_anterior = hoje - timedelta(days=1)
    # Retorna o ano e o mês no formato 'YYYYMM'
    return mes_anterior.strftime('%Y%m')

data = mes_passado()

# 1 - Deletando todos arquivos
diretorio = f"C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data/{data}.csv"
deletar_todos_arquivos(diretorio)

# 2 - Verificando disponibilidade de arquivos
resultados = []
resultado = verificar_disponibilidade_arquivo(data)
resultados.append(resultado)
# Salva todos os resultados em um único arquivo JSON
with open("data/resultados_acesso_mes_passado.json", "w", encoding="utf-8") as json_file:
    json.dump(resultados, json_file, indent=4, ensure_ascii=False)

#3 - Extraindo arquivos para gravar em csv
with open("data/resultados_acesso_mes_passado.json", "r", encoding="utf-8") as file:
    dados_acesso = json.load(file)

for entrada in dados_acesso:
    if entrada["status"] == "acessado":
        link_base = entrada["opcao_link"]
        formato_arquivo = entrada["formato"]
        data_acesso = entrada["data_hora_acesso"]
        # Chama a função com os parâmetros extraídos
        resultado_df = acessar_arquivos_extrair_dados(link_base, formato_arquivo)
        adicionar_metadados_e_salvar(resultado_df, entrada["data"], formato_arquivo, data_acesso)

