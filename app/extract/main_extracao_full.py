from extracao_etapas.limpar_diretorio import deletar_todos_arquivos
from extracao_etapas.verificar_links import verificar_disponibilidade_arquivo
from extracao_etapas.extrair_dados_arquivos import acessar_arquivos_extrair_dados
from extracao_etapas.adicionar_metadados_salvar import adicionar_metadados_e_salvar
import json

# 1 - Deletando todos arquivos
diretorio = "C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data"
deletar_todos_arquivos(diretorio)

# 2 - Verificando disponibilidade de arquivos
lista_datas = [
    '201601', '201602', '201603', '201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611', '201612',
    '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711', '201712',
    '201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812',
    '201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910', '201911', '201912',
    '202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010', '202011', '202012',
    '202101', '202102', '202103', '202104', '202105', '202106', '202107', '202108', '202109', '202110', '202111', '202112',
    '202201', '202202', '202203', '202204', '202205', '202206', '202207', '202208', '202209', '202210', '202211', '202212',
    '202301', '202302', '202303', '202304', '202305', '202306', '202307', '202308', '202309', '202310', '202311', '202312',
    '202401', '202402', '202403', '202404', '202405', '202406', '202407', '202408', '202409', '202410', '202411', '202412',
]

resultados = []

# Percorre todas as datas e armazena os resultados dos acessos em json
for data in lista_datas:
    resultado = verificar_disponibilidade_arquivo(data)
    resultados.append(resultado)
    # Salva todos os resultados em um único arquivo JSON
    with open("data/resultados_acesso_full.json", "w", encoding="utf-8") as json_file:
        json.dump(resultados, json_file, indent=4, ensure_ascii=False)

#3 - Extraindo arquivos para gravar em csv
with open("data/resultados_acesso_full.json", "r", encoding="utf-8") as file:
    dados_acesso = json.load(file)

for entrada in dados_acesso:
    if entrada["status"] == "acessado":
        link_base = entrada["opcao_link"]
        formato_arquivo = entrada["formato"]
        data_acesso = entrada["data_hora_acesso"]
        # Chama a função com os parâmetros extraídos
        resultado_df = acessar_arquivos_extrair_dados(link_base, formato_arquivo)
        adicionar_metadados_e_salvar(resultado_df, entrada["data"], formato_arquivo, data_acesso)

