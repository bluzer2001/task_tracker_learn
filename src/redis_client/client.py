from src.config.redis import REDIS_PORT, REDIS_HOST
import redis

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
