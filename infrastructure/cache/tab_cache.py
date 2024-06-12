import redis
import ipdb
from config import connections


redis_host = connections["REDIS"]["host"]
redis_port = connections["REDIS"]["port"]

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


def get_value(key):
    return r.get(key)
