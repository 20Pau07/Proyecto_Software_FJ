# LOGS DEL SISTEMA
# PROYECTO: SOFTWARE FJ
# Persona 3: Paula Andrea Briñez

import logging
from pathlib import Path

RUTA_LOGS = Path(__file__).resolve().parent / "logs_software_fj.txt"

logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.DEBUG)
logger.propagate = False 

if not logger.handlers:
    handler = logging.FileHandler(RUTA_LOGS, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def registrar_evento(mensaje: str):
    """Registra acciones generales del sistema."""
    logger.info(mensaje)


def registrar_advertencia(mensaje: str):
    """Registra situaciones que requieren atención."""
    logger.warning(mensaje)


def registrar_error(error, incluir_traza: bool = False):
    """Registra errores ocurridos durante la ejecución."""
    logger.error(str(error), exc_info=incluir_traza)


def registrar_debug(mensaje: str):
    """Registra información detallada para depuración."""
    logger.debug(mensaje)


if __name__ == "__main__":
    registrar_evento("Inicio de prueba del módulo de logs.")
    registrar_advertencia("Advertencia de prueba.")
    registrar_error("Error de prueba.")
    print(f"Logs guardados en: {RUTA_LOGS}")