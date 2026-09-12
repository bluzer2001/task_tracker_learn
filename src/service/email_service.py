import logging
from time import sleep
from src.models import Notification

logger = logging.getLogger(__name__)


class EmailService:

    def send(self, notification: Notification):
        logger.info("Начало отправки уведомления")
        sleep(3)
        # print(f"Email отправлен to: {notification.email}")
        raise RuntimeError("SMTP сервер недоступен")



