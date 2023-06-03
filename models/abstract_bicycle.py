# pylint: disable=line-too-long
"""
This module provides classes and functions related to bicycles.

"""
from abc import ABC, abstractmethod

from exception import NegativeValue


class AbstractBicycle(ABC):
    """
    An abstract base class representing a bicycle.

    Attributes:
        bike_brand (str): The brand of the bicycle.
        current_speed (float): The current speed of the bicycle.
        max_speed (float): The maximum speed of the bicycle.

    Methods:
        get_max_distance(): Get the maximum distance the bicycle can travel.
        __str__(): Return a string representation of the bicycle.
        keys_and_values(type_of_elements): Get the dictionary of attribute keys and values of the specified type.
        __iter__(): Iterate over the best shops associated with the bicycle.

    """

    def __init__(self, bike_brand="no information", current_speed=0, max_speed=0):
        """
        Initialize an AbstractBicycle instance.

        Args:
            bike_brand (str, optional): The brand of the bicycle. Defaults to "no information".
            current_speed (float, optional): The current speed of the bicycle. Defaults to 0.
            max_speed (float, optional): The maximum speed of the bicycle. Defaults to 0.
        """
        self.bike_brand = bike_brand
        self.current_speed = current_speed
        self.max_speed = max_speed
        if self.current_speed < 0 or self.max_speed < 0:
            raise NegativeValue("current_speed or max_speed")
        self.best_shops = set()

    @staticmethod
    @abstractmethod
    def get_max_distance():
        """
        Get the maximum distance the bicycle can travel.

        Returns:
            float: The maximum distance the bicycle can travel.

        """

    def __str__(self):
        """
        Return a string representation of the bicycle.

        Returns:
            str: The string representation of the bicycle.

        """
        return f" Bike brand = {self.bike_brand}, Current speed = {self.current_speed}," \
               f" Bike max speed = {self.max_speed}"

    def keys_and_values(self, type_of_elements):
        """
        Get the dictionary of attribute keys and values of the specified type.

        Args:
            type_of_elements (type): The type of elements to include in the dictionary.

        Returns:
            dict: The dictionary of attribute keys and values of the specified type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, type_of_elements)}

    def __iter__(self):
        """
        Iterate over the best shops associated with the bicycle.

        Yields:
            object: The next best shop associated with the bicycle.
        """
        return iter(self.best_shops)
