import pytest
import pandas as pd
from unittest.mock import patch
import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from app.transform.transform_etapas.merge_all_files import merge_all_files, remover_colunas_fixas
from app.transform.transform_etapas.converter_data import converter_data
from app.transform.transform_etapas.preencher_nulos import tratar_nulos

@pytest.fixture
def sample_df():
    """Fixture que cria um DataFrame de exemplo para testes."""
    return pd.DataFrame({
        'NIVEL': ['A', None, 'B', 'C'],
        'SIGLA_ORGAO': ['ORG1', 'ORG2', None, 'ORG4'],
        'NOME_ORGAO': ['Orgao 1', None, 'Orgao 3', None],
        'NOME_CARGO': ['Cargo 1', 'Cargo 2', None, 'Cargo 4'],
        'CARGO_EM_EXTINCAO': ['S', None, 'N', 'S'],
        'PLANO_CARREIRA': ['P1', 'P2', None, 'P4'],
        'VACANCIA_POR_EXONERACAO': [1, None, 3, 4],
        'VACANCIA_POR_DEMISSAO': [0, 2, None, 4],
        'VAGO': [10, None, 30, 40],
        'DISTRIBUIDA': [100, 200, None, 400],
        'OCUPADA': [50, None, 70, 80],
        'APROVADA': [1000, 2000, 3000, None],
        'ANO_MES': ['202301', '202301', '202301', '202301']
    })

@pytest.mark.parametrize("data", ['202301', '202302'])
def test_integracao_completa(data, sample_df):
    """Testa o fluxo completo de transformação dos dados usando mock data."""
    with patch('pandas.read_csv', return_value=sample_df):
        # Executa o fluxo completo
        df = merge_all_files(data)
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        
        df_select = remover_colunas_fixas(df)
        assert isinstance(df_select, pd.DataFrame)
        assert not df_select.empty
        
        df_conv = converter_data(df_select)
        assert isinstance(df_conv, pd.DataFrame)
        assert not df_conv.empty
        
        estrategia = {
            'NIVEL': 'N/A',
            'SIGLA_ORGAO': 'N/A',
            'NOME_ORGAO': 'N/A',
            'NOME_CARGO': 'N/A',
            'CARGO_EM_EXTINCAO': 'N/A',
            'PLANO_CARREIRA': 'N/A',
            'VACANCIA_POR_EXONERACAO': 'zero',
            'VACANCIA_POR_DEMISSAO': 'zero',
            'VAGO': 'zero',
            'DISTRIBUIDA': 'zero',
            'OCUPADA': 'zero',
            'APROVADA': 'zero'
        }
        
        df_final = tratar_nulos(df_conv, metodo='preencher', estrategia=estrategia)
        
        # Verificações finais
        assert isinstance(df_final, pd.DataFrame)
        assert not df_final.empty
        assert not df_final.isnull().any().any()

def test_merge_all_files_mock(sample_df):
    """Teste específico para a função merge_all_files."""
    with patch('pandas.read_csv', return_value=sample_df):
        result = merge_all_files("202301")
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert all(col in result.columns for col in sample_df.columns)
        assert len(result) > 0

def test_tratar_nulos_relatorio(sample_df):
    """Testa se o relatório de nulos é gerado corretamente."""
    relatorio = tratar_nulos(sample_df, metodo='relatorio')
    assert isinstance(relatorio, pd.DataFrame)
    assert 'pct_nulos' in relatorio.columns
    assert 'tipo_dados' in relatorio.columns
    assert 'total_nulos' in relatorio.columns