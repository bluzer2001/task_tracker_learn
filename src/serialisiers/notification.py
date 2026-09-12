from dataclasses import asdict
import json
from src.models import Notification
from .base import Serializer


class NotificationSerializer(Serializer):
    @staticmethod
    def serialize(notification: Notification) -> str:
        obj_dict = asdict(notification)
        return json.dumps(obj_dict)

    @staticmethod
    def deserialize(data: str) -> Notification:
        json_dict = json.loads(data)
        return Notification(**json_dict)