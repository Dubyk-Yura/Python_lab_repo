from models.abstract_bicycle import AbstractBicycle


class ElectroBicycle(AbstractBicycle):
    """
    A class representing an electric bicycle.

    Attributes:
        bike_battery_capacity (float): The battery capacity of the electric bicycle.
        bike_consumption_per_100m (float): The energy consumption per 100 meters of the electric bicycle.
        bike_brand (str): The brand of the electric bicycle.
        current_speed (float): The current speed of the electric bicycle.
        max_speed (float): The maximum speed of the electric bicycle.

    Methods:
        get_max_distance(): Get the maximum distance the electric bicycle can travel.
        __str__(): Return a string representation of the electric bicycle.

        """

    def __init__(self, bike_battery_capacity=0, bike_consumption_per_100m=0, bike_brand="no information",
                 current_speed=0, max_speed=0):
        """
        Initialize an ElectroBicycle instance.

        Args:
            bike_battery_capacity (float, optional): The battery capacity of the electric bicycle. Defaults to 0.
            bike_consumption_per_100m (float, optional): The energy consumption per 100 meters of the electric bicycle. Defaults to 0.
            bike_brand (str, optional): The brand of the electric bicycle. Defaults to "no information".
            current_speed (float, optional): The current speed of the electric bicycle. Defaults to 0.
            max_speed (float, optional): The maximum speed of the electric bicycle. Defaults to 0.

        """
        self.bike_consumption_per_100m = bike_consumption_per_100m
        self.bike_battery_capacity = bike_battery_capacity
        self.best_shops = {"veloGO", "bikeGO"}
        super().__init__(bike_brand, current_speed, max_speed)

    def get_max_distance(self):
        """
        Get the maximum distance the electric bicycle can travel.

        Returns:
            float: The maximum distance the electric bicycle can travel.

        """
        if self.bike_consumption_per_100m != 0:
            return self.bike_battery_capacity / self.bike_consumption_per_100m
        else:
            print("Error -> bike consumption is 0")
            return None

    def __str__(self):
        """
        Return a string representation of the electric bicycle.

        Returns:
            str: The string representation of the electric bicycle.

        """
        return f"Bike battery capacity - {self.bike_battery_capacity}, Bike consumption - " \
               f"{self.bike_consumption_per_100m}, {super().__str__()}"
