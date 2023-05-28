from models.abstract_bicycle import AbstractBicycle


class Tricycle(AbstractBicycle):
    """
    A class representing a tricycle.

    Attributes:
        with_trunk (bool): Indicates if the tricycle has a trunk.
        rare_wheel_distance (float): The distance between the rare wheels of the tricycle.
        bike_brand (str): The brand of the tricycle.
        current_speed (float): The current speed of the tricycle.
        max_speed (float): The maximum speed of the tricycle.

    Methods:
        get_max_distance(): Get the maximum distance the tricycle can travel.
        __str__(): Return a string representation of the tricycle.

    """

    def __init__(self, with_trunk=True, rare_wheel_distance=0, bike_brand="no information",
                 current_speed=0, max_speed=0):
        """
        Initialize a Tricycle instance.

        Args:
            with_trunk (bool, optional): Indicates if the tricycle has a trunk. Defaults to True.
            rare_wheel_distance (float, optional): The distance between the rare wheels of the tricycle. Defaults to 0.
            bike_brand (str, optional): The brand of the tricycle. Defaults to "no information".
            current_speed (float, optional): The current speed of the tricycle. Defaults to 0.
            max_speed (float, optional): The maximum speed of the tricycle. Defaults to 0.

        """
        self.rare_wheel_distance = rare_wheel_distance
        self.with_trunk = with_trunk
        self.best_shops = {"velo bike", "МTB STOCK"}
        super().__init__(bike_brand, current_speed, max_speed)

    @staticmethod
    def get_max_distance():
        """
        Get the maximum distance the tricycle can travel.

        Returns:
            float: The maximum distance the tricycle can travel.

        """
        return 0

    def __str__(self):
        """
        Return a string representation of the tricycle.

        Returns:
            str: The string representation of the tricycle.

        """
        return f"Bike is with trunk - {self.with_trunk}, Bike rare wheel distance - {self.rare_wheel_distance}," \
               f" {super().__str__()}"
