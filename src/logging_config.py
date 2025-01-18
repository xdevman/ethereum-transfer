import sys

from loguru import logger


def setup_logging():
    logger.remove()

    logger.add(
        "logs/wallets.log",
        rotation="1 week",
        compression="zip",
        level="INFO",
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    )

    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <level>{message}</level>",
    )
