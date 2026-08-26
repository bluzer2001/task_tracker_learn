from src.redis_client import redis_client

client = redis_client()
client.publish("notifica")