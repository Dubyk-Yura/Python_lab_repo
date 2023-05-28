import sys

from models.abstract_bicycle import AbstractBicycle


class Bicycle(AbstractBicycle):
    """
    A class representing a bicycle.

    Attributes:
        BIKE_PRICE (int): The base price of a bicycle.
        instance (Bicycle): The singleton instance of the Bicycle class.
        bike_type (str): The type of the bicycle.
        bike_brand (str): The brand of the bicycle.
        current_speed (float): The current speed of the bicycle.
        max_speed (float): The maximum speed of the bicycle.

    Methods:
        accelerate(speed): Increase the current speed of the bicycle.
        brake(): Stop the bicycle.
        increase_price(price): Increase the price of the bicycle.
        __str__(): Return a string representation of the bicycle.
        get_max_distance(): Get the maximum distance the bicycle can travel.

    """
    BIKE_PRICE = 10000
    instance = None

    def __init__(self, bike_type="no information", bike_brand="no information", current_speed=0, max_speed=0):
        """
        Initialize a Bicycle instance.

        Args:
            bike_type (str, optional): The type of the bicycle. Defaults to "no information".
            bike_brand (str, optional): The brand of the bicycle. Defaults to "no information".
            current_speed (float, optional): The current speed of the bicycle. Defaults to 0.
            max_speed (float, optional): The maximum speed of the bicycle. Defaults to 0.
        """
        self.bike_type = bike_type
        self.best_shops = {"velo shop", "bike shop"}
        super().__init__(bike_brand, current_speed, max_speed)

    def accelerate(self, speed):
        """
        Increase the current speed of the bicycle.

        Args:
            speed (float): The speed to increase.
        """
        if (self.current_speed + speed) > self.max_speed:
            print("Speed with accelerate is more than maximum speed")
            return
        self.current_speed += speed
        print(f"Current speed is changed and it equal to {self.current_speed}")

    def brake(self):
        """
        Stop the bicycle.

        """
        self.current_speed = 0
        print(f"bike {self.bike_brand} was stopped;")

    @classmethod
    def increase_price(cls, price):
        """
        Increase the price of the bicycle.

        Args:
            price (int): The price to increase.
        """
        price += cls.BIKE_PRICE
        print(f"Price of bicycle after increase is {price}")

    def __str__(self):
        """
        Return a string representation of the bicycle.

        Returns:
            str: The string representation of the bicycle.
        """
        return f'Bike type - {self.bike_type}, {super().__str__()}'

    @staticmethod
    def get_max_distance():
        """
        Get the maximum distance the bicycle can travel.

        Returns:
            int: The maximum distance the bicycle can travel.
        """
        return sys.maxsize
