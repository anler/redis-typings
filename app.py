from redis import Redis


class App:
    def __init__(self, redis: Redis) -> None:
        self.redis = redis


redis = Redis("localhost", 3306)
app = App(redis)
print(app)
