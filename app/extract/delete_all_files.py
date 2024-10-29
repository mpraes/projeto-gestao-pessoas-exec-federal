import os
import glob

def deletar_todos_arquivos(diretorio):
    # Obtém todos os arquivos do diretório especificado
    arquivos = glob.glob(os.path.join(diretorio, "*"))
    
    for arquivo in arquivos:
        try:
            os.remove(arquivo)  # Remove cada arquivo
            print(f"Arquivo {arquivo} deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar o arquivo {arquivo}: {e}")

# Exemplo de uso
diretorio = "C:/Users/smart/Documents/1.Estudos-Profissional/projeto-gestao-pessoas-exec-federal/data"
deletar_todos_arquivos(diretorio)
