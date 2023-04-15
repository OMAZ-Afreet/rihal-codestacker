import redis

r = redis.Redis(host='bc', port=6379, decode_responses=True)