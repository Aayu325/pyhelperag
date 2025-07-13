import tracemalloc

def profile_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Memory usage: Current={current/10**6:.2f}MB, Peak={peak/10**6:.2f}MB")
        tracemalloc.stop()
        return result
    return wrapper
