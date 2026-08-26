from time import sleep
from src.models import Notification


class EmailService:

    def send(self, notification: Notification):
        print("Начало отправки уведомления")
        sleep(3)
        print(f"Email отправлен to: {notification.email}")
