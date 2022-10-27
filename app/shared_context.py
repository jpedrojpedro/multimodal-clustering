import redis
import logging
import uvicorn
from fastapi.logger import logger


# TODO: load values from .env file
# constants
REDIS_HOST = "redis"
REDIS_PORT = 6379

QUEUE_TXT = "txt_queue"
QUEUE_IMG = "img_queue"

API_PORT = 8080
API_HOST = "0.0.0.0"
API_DESCRIPTION = """
## Multimodal Clustering using Product Quantization 🚀
"""

# single instances
api_app = None
api_logger = None
api_redis_cli = None


def start_queueing():
    redis_client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
    )
    return redis_client


def start_logging():
    uvicorn_logger = logging.getLogger("uvicorn.access")
    logger.handlers = uvicorn_logger.handlers
    console_formatter = uvicorn.logging.ColourizedFormatter("{message}", style="{", use_colors=False)
    logger.handlers[0].setFormatter(console_formatter)
    logger.setLevel(uvicorn_logger.level)
    return logger
