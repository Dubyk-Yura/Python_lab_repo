"""
This module provides custom decorators for enhancing the functionality of functions.
"""
import functools
import time


def return_name(func):
    """
    Decorator that prints the name of the function before calling it.
    Wrapper function that prints the function name and calls the original function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(*args)
        print(**kwargs)
        print(f"Name of function -> {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


def from_iter_to_tuple(func):
    """
    Decorator that converts the output of a function to a tuple.
    Wrapper function that calls the original function and converts the output to a tuple.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return tuple(result)

    return wrapper


def measure_time(func):
    """
    A decorator that measures the execution time of a function.
    The wrapper function that measures the execution time of the decorated function.

    Args:
        func: The function to be measured.

    Returns:
        The wrapped function.

    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        finish_time = time.perf_counter()
        time_func = finish_time - start_time
        print(f"time of func is {time_func}")
        return func(*args, **kwargs)

    return wrapper
