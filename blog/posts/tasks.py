from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name="send_news")
def send_news():
    logger.info("Email sended")
