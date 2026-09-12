from dataclasses import asdict
import json
from src.models import AnalyticMessage
from .base import Serializer


class AnalyticMessageSerializer(Serializer):
    @staticmethod
    def serialize(notification: AnalyticMessage) -> str:
        obj_dict = asdict(notification)
        return json.dumps(obj_dict)

    @staticmethod
    def deserialize(data: str) -> AnalyticMessage:
        json_dict = json.loads(data)
        return AnalyticMessage(**json_dict)