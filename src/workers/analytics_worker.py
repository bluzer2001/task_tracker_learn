from src.service.analytic_service import AnalyticService
from src.redis_client import redis_client
from src.constants import ANALYSIS_QUEUE, DEAD_ANALYSIS_QUEUE
from src.queues import RedisAnalyticsQueue
from src.workers.base import Worker
from src.service import AnalyticService

class  AnalyticsWorker(Worker):

    def run(self):
        print("worker запущен")
        while True:
            model = self.queue.consume()
            self.service.calc_analytics(model)
            # try:
            #     self.service.calc_analytics(model)
            # except Exception as e:
            #     self._retry_send_message(model, str(e))


if __name__ == "__main__":
    queue = RedisAnalyticsQueue(redis_client, ANALYSIS_QUEUE)
    dead_queue = RedisAnalyticsQueue(redis_client, DEAD_ANALYSIS_QUEUE)
    worker = AnalyticsWorker(queue, dead_queue, AnalyticService())
    worker.run()