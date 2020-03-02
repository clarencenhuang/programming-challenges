from functools import wraps
from flask import Flask, request, jsonify
import time

def fixed_window(window_size=3, limit=1):

    def decorator(func):
        counter, window_end = 0, 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter, window_end
            ts = time.time()
            if ts > window_end:
                counter = 0
                window_end = ts + window_size
            counter += 1
            if counter > limit:
                return jsonify(error='too many requests'), 429
            else:
                return func(*args, **kwargs)
        return wrapper

    return decorator


if __name__ == '__main__':

    app = Flask(__name__)

    @app.route('/')
    @fixed_window()
    def hello_world():
        return 'Hello World!'
    app.run()