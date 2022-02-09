import redis
from django.conf import settings

def set_redis_value(key:str, value) -> bool:
    
    redis_instance = get_redis_instance()
    result = redis_instance.set(key, value)
    
    return result

def get_redis_value(key:str):
    
    redis_instance = get_redis_instance()
    result = redis_instance.get(key)
    
    if result:
        return result.decode('utf-8')
    
    return None

def get_redis_instance():
    
    redis_instance = redis.Redis(
        host = settings.REDIS_HOST, 
        port = settings.REDIS_PORT, 
    )
    
    return redis_instance