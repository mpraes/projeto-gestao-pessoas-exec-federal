from transform_etapas.merge_all_files import merge_all_files, remover_colunas_fixas
from transform_etapas.converter_data import converter_data
from transform_etapas.preencher_nulos import tratar_nulos

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

for data in lista_datas:
    df = merge_all_files(data)
    df_select = remover_colunas_fixas(df)
    df_conv = converter_data(df_select)
    # 1. Gerar relatório de nulos
    relatorio = tratar_nulos(df_conv, metodo='relatorio')
    # print(relatorio)

    # 2. Remover todas as linhas com valores nulos
    df_sem_nulos = tratar_nulos(df, metodo='remover_linhas')

    # 3. Remover colunas com mais de 30% de nulos
    df_sem_colunas_nulos = tratar_nulos(df, metodo='remover_colunas', limite_nulos=50)

    # 4. Preencher nulos com estratégia personalizada
    estrategia = {
        'NIVEL': 'N/A',      # Preenche com a média
        'SIGLA_ORGAO': 'N/A',    # Preenche com a mediana
        'NOME_ORGAO': 'N/A',       # Preenche com a moda
        'NOME_CARGO': 'N/A',       # Preenche com zero
        'CARGO_EM_EXTINCAO': 'N/A',      # Preenche com o último valor válido
        'PLANO_CARREIRA': 'N/A',      # Preenche com o próximo valor válido
        'VACANCIA_POR_EXONERACAO': 'zero',      # Preenche com zero
        'VACANCIA_POR_DEMISSAO': 'zero',      # Preenche com zero
        'VACANCIA_POR_PROMOCAO': 'zero',      # Preenche com zero
        'VACANCIA_POR_READAPTACAO': 'zero',      # Preenche com zero
        'VACANCIA_POR_APOSENTADORIA': 'zero',      # Preenche com zero
        'VACANCIA_POR_POSSE_CARGO_INAC': 'zero',      # Preenche com zero
        'VACANCIA_POR_FALECIMENTO': 'zero',      # Preenche com zero
        'VAGO': 'zero',      # Preenche com zero
        'DISTRIBUIDA': 'zero',      # Preenche com zero
        'OCUPADA': 'zero',      # Preenche com zero
        'APROVADA': 'zero',      # Preenche com zero
    }
    df_preenchido = tratar_nulos(df, metodo='preencher', estrategia=estrategia)

    # 5. Exportar para CSV
    df_preenchido.to_csv(f'dataset_final.csv', index=False, encoding='utf-8', sep=';')