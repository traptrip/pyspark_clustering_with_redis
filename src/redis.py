import redis


class RedisBroker:
    def __init__(self, config) -> None:
        self.redis_client = redis.Redis(host=config.host, port=config.port)

    def set(self, key, value):
        self.redis_client.set(key, value)

    def get(self, key):
        return self.redis_client.get(key)
