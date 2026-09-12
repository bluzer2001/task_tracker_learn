from time import sleep
from src.models import AnalyticMessage


class AnalyticService:

    def calc_analytics(self, message: AnalyticMessage):
        print("Обрабатываем полученное значение")
        sleep(4)
        print(f"Обработали event {message.event_name}")
        return {"message": message.event_name}