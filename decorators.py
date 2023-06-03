# pylint: disable=line-too-long
"""
This module provides custom decorators for enhancing the functionality of functions.
"""
from datetime import datetime
import time
import logging


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


# pylint: disable=invalid-name
def logged(exception, mode):
    """
    A decorator that logs exceptions raised by the decorated function.

    Args:
        exception (Exception): The exception class to be caught and logged.
        mode (str): The logging mode, either "console" or "file".

    Returns:
        function: The decorated function.

    Raises:
        ValueError: If an invalid logging mode is provided.

    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.info(" Exception %s occurred in %s", e, function.__name__)
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename="logging.txt")
                    logging.info(" Exception %s occurred in %s -> %s", e, function.__name__, datetime.now())
                else:
                    raise ValueError("You selected the wrong mode. Choose 'file' or 'console' mode") from e
                return None

        return wrapper

    return decorator
