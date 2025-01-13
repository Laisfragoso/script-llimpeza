import os
import time
from datetime import datetime

# Configuração
DIRECTORIES = ["/tmp", "/var/tmp"]  # Diretórios de arquivos temporários
RETENTION_DAYS = 7  # Tempo de retenção em dias

def delete_old_files(directory, retention_seconds):
    """
    Remove arquivos mais antigos que o tempo de retenção especificado.
    
    Args:
        directory (str): Caminho do diretório a ser limpo.
        retention_seconds (int): Tempo de retenção em segundos.
    """
    now = time.time()
    deleted_files = 0
    deleted_dirs = 0

    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            # Deletar arquivos antigos
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    file_age = now - os.path.getmtime(file_path)
                    if file_age > retention_seconds:
                        try:
                            os.remove(file_path)
                            deleted_files += 1
                        except Exception as e:
                            print(f"Erro ao deletar arquivo {file_path}: {e}")

            # Deletar diretórios vazios
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    os.rmdir(dir_path)  # Remove apenas diretórios vazios
                    deleted_dirs += 1
                except OSError:
                    pass  # Diretório não está vazio
    except Exception as e:
        print(f"Erro ao acessar {directory}: {e}")

    print(f"Diretório {directory}: {deleted_files} arquivos e {deleted_dirs} diretórios removidos.")

def main():
    """
    Função principal para limpeza de arquivos temporários.
    """
    retention_seconds = RETENTION_DAYS * 86400  # Converter dias para segundos
    print(f"Iniciando limpeza de arquivos temporários. Retenção: {RETENTION_DAYS} dias.")
    print(f"Data/Hora de início: {datetime.now()}")

    for directory in DIRECTORIES:
        if os.path.exists(directory):
            print(f"Limpando {directory}...")
            delete_old_files(directory, retention_seconds)
        else:
            print(f"Diretório {directory} não encontrado. Pulando.")

    print("Limpeza concluída.")

if __name__ == "__main__":
    main()
