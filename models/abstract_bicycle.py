from abc import ABC, abstractmethod


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

    @staticmethod
    @abstractmethod
    def get_max_distance():
        """
        Get the maximum distance the bicycle can travel.

        Returns:
            float: The maximum distance the bicycle can travel.

        """
        pass

    def __str__(self):
        """
        Return a string representation of the bicycle.

        Returns:
            str: The string representation of the bicycle.

        """
        return f", Bike brand = {self.bike_brand}, Current speed = {self.current_speed}," \
               f" Bike max speed = {self.max_speed}"
