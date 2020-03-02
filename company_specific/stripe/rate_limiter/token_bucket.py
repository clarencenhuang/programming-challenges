from functools import wraps
import time
from flask import Flask, jsonify


def token_bucket(rate=1, capacity=2):

    def decorator(func):
        counter, last_time = 0, 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter, last_time, func
            ts = time.time()
            new_counter = min(capacity, counter + (ts - last_time) * rate)
            if new_counter >= 1:
                counter = new_counter - 1
                last_time = ts
                return func(*args, **kwargs)
            else:
                return jsonify(error='too many requests'), 429

        return wrapper

    return decorator

if __name__ == '__main__':
    app = Flask(__name__)
    @app.route('/')
    @token_bucket()
    def hello_world():
        return 'Hello World!'
    app.run()
