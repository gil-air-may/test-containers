from infrastructure.cache import tab_cache
import json


def get_cached(id):
    return json.loads(tab_cache.get_value(id))
