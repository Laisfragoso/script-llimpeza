import logging
import argparse
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Configuração de Logging para visibilidade em operações de segurança (SOC/SIEM)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Configurações Padrão
DEFAULT_DIRECTORIES = ["/tmp", "/var/tmp"]
DEFAULT_RETENTION_DAYS = 7

def get_file_age_days(file_path: Path) -> float:
    """Calcula a idade do arquivo em dias de forma precisa."""
    stat = file_path.stat()
    last_modified = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
    age = datetime.now(timezone.utc) - last_modified
    return age.days

def clean_directory(target_dir: Path, retention_days: int, dry_run: bool = False):
    """
    Executa a limpeza de arquivos antigos e diretórios vazios.
    """
    if not target_dir.exists():
        logger.warning(f"Diretório não encontrado: {target_dir}")
        return

    logger.info(f"Iniciando varredura em: {target_dir} (Retenção: {retention_days} dias)")
    
    files_removed = 0
    dirs_removed = 0

    # Itera de forma recursiva (rglob) do fundo para o topo (útil para remover dirs vazios)
    for item in sorted(target_dir.rglob("*"), reverse=True):
        try:
            if item.is_file():
                if get_file_age_days(item) >= retention_days:
                    if not dry_run:
                        item.unlink()
                    logger.debug(f"Arquivo removido: {item}")
                    files_removed += 1
            
            elif item.is_dir() and not any(item.iterdir()):
                # Remove apenas se estiver vazio
                if not dry_run:
                    item.rmdir()
                logger.debug(f"Diretório vazio removido: {item}")
                dirs_removed += 1

        except Exception as e:
            logger.error(f"Falha ao processar {item}: {e}")

    action = "[DRY-RUN]" if dry_run else "[EXECUTADO]"
    logger.info(f"{action} {target_dir}: {files_removed} arquivos e {dirs_removed} pastas removidos.")

def main():
    # Uso de argparse para flexibilidade via Terminal (CLI)
    parser = argparse.ArgumentParser(description="Automação de Limpeza de Arquivos Temporários")
    parser.add_argument("--days", type=int, default=DEFAULT_RETENTION_DAYS, help="Dias de retenção")
    parser.add_argument("--dry-run", action="store_true", help="Simula a operação sem deletar nada")
    args = parser.parse_args()

    start_time = datetime.now()
    logger.info("Iniciando rotina de manutenção.")

    for path_str in DEFAULT_DIRECTORIES:
        clean_directory(Path(path_str), args.days, args.dry_run)

    duration = datetime.now() - start_time
    logger.info(f"Manutenção finalizada em {duration.total_seconds():.2f}s.")

if __name__ == "__main__":
    main()