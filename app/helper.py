import redis
import numpy as np


def create_connection_ivfadc():
    redis_client = redis.Redis(host='redis', port=6369)
    keys_array = redis_client.keys('txt-*')
    for key_name in keys_array:
        key = redis_client.hgetall(key_name)
        i = np.arange(28*28).reshape(28, 28)
        y = np.frombuffer(key[b'embedding'], dtype=i.dtype)
        y.shape
