import os
import tempfile
from app.extract.extracao_etapas.limpar_diretorio import deletar_todos_arquivos
import glob

def test_deletar_todos_arquivos():
    # Cria um diretório temporário
    with tempfile.TemporaryDirectory() as temp_dir:
        # Cria arquivos de teste no diretório temporário
        for i in range(3):
            open(os.path.join(temp_dir, f"file_{i}.txt"), 'w').close()

        # Verifica se os arquivos foram criados
        arquivos_iniciais = glob.glob(os.path.join(temp_dir, "*"))
        assert len(arquivos_iniciais) == 3

        # Executa a função para deletar os arquivos
        deletar_todos_arquivos(temp_dir)

        # Verifica se todos os arquivos foram deletados
        arquivos_finais = glob.glob(os.path.join(temp_dir, "*"))
        assert len(arquivos_finais) == 0


