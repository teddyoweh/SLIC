import functools
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info(f"Starting function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' finished with result: {result}. Execution time: {elapsed_time:.4f} seconds")
        return result
    return wrapper

# Example usage:

@logger_decorator
def add(a, b):
    return a + b

@logger_decorator
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    add(1, 2)
    multiply(3, 4)
