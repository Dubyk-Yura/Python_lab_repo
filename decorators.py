"""
This module provides custom decorators for enhancing the functionality of functions.
"""
import functools


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
