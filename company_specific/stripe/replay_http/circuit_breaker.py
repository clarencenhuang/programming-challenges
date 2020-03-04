from functools import wraps
import time

def circuit_breaker(failure_thresh=5, reset_timeout=3):

    def decorator(func):
        failure_count, last_failure_time = 0, 0

        def wrapper(*args, **kwargs):
            nonlocal failure_count, last_failure_time
            ts = time.time()
            if failure_count < failure_thresh or ts - last_failure_time > reset_timeout:
                try:
                    res = func(*args, **kwargs)
                    failure_count = 0
                    return res
                except:
                    if failure_count < failure_thresh:
                        failure_count += 1
                    last_failure_time = ts
                    raise
            else:
                return None

        return wrapper

    return decorator



