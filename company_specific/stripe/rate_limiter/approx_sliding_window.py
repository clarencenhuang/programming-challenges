from functools import wraps
from flask import jsonify
import time


def approx_sliding_window(window_size=3, limit=1):

    def decorator(func):
        window_start, last_count, cur_count = 0, 0, 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal window_start, last_count, cur_count
            ts = time.time()
            if ts > window_start + window_size:
                window_start = ts
                last_count, cur_count = cur_count, 0
            this_window_portion = min(ts - window_start, 3.0) / 3.0
            last_window_portion = 1.0 - this_window_portion
            approx_count = last_window_portion * last_count + this_window_portion * cur_count
            if approx_count > limit:
                return jsonify(error='too many requests'), 429
            else:
                cur_count += 1
                return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == '__main__':
    from flask import Flask, request
    app = Flask(__name__)

    @app.route('/')
    @approx_sliding_window()
    def hello_world():
        return 'Hello World!'

    app.run()



