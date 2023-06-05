# pylint: disable=line-too-long
"""
Module: exception

This module defines a custom exception class called NegativeValue, which is a subclass of ValueError.
The NegativeValue exception is raised when a field or multiple fields are expected to have positive values,
but a negative value is provided.

Custom Exception:
    - NegativeValue: Raised when a field or multiple fields have negative values.

Usage:
    - To raise the NegativeValue exception, simply instantiate the exception object with the appropriate field name(s).
      For example:
          raise NegativeValue("age")

    - To handle the NegativeValue exception, use a try-except block.
      For example:
          try:
              # Code that may raise NegativeValue exception
          except NegativeValue as e:
              print(str(e))
"""


class NegativeValue(ValueError):
    """
    Custom exception class to raise an error when a negative value is encountered in a specific field.

    Attributes:
        field (str): The name of the field where the negative value was encountered.

    Methods:
        __init__(self, field="This fields can't have negative value"):
            Initializes a NegativeValue object with the provided field name (default: "This fields can't have negative
             value").
        __str__(self):
            Returns a string representation of the exception, specifying the field that must have a positive value.
    """

    def __init__(self, field="This fields can`t have negative value"):
        self.field = field

    def __str__(self):
        return f"Field(s) {self.field} must have positive value"
