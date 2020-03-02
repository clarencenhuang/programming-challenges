from functools import wraps
import time
from bisect import bisect_left
from flask import jsonify


def sliding_window_log(window_size=3, limit=1):

    def decorator(func):
        logs = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal logs
            ts = time.time()
            idx = bisect_left(logs, ts - window_size)
            logs = logs[idx:]
            if len(logs) >= limit:
                return jsonify(error='too many requests'), 429
            else:
                logs.append(ts)
                return func(*args, **kwargs)
        return wrapper

    return decorator

if __name__ == '__main__':
    from flask import Flask, request
    app = Flask(__name__)

    @app.route('/')
    @sliding_window_log()
    def hello_world():
        return 'Hello World!'

    app.run()




