import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("deepseek")

class RequestLogger:
    @staticmethod
    def log_request(prompt: str, response: str):
        logger.info(
            f"[{datetime.now()}] Запрос: {prompt[:50]}... | Ответ: {response[:100]}..."
        )