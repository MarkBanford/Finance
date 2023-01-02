import time


def timer(func):
    """
    A decorator function that measures the runtime of a function.
    """

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Runtime: {end - start:.2f} seconds")
        return result

    return wrapper


# @timer
# def my_function(a, b):
#     time.sleep(1)
#     return a + b
#
#
# result = my_function(1, 2)
# print(f"Result: {result}")
