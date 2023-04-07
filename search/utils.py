import time

def bench(func, *args, **kwargs):
    t = time.perf_counter_ns()
    r = func(*args, **kwargs)
    d = time.perf_counter_ns() - t
    print(f'{func.__name__}:      {d/1000000}  ms')
    return r