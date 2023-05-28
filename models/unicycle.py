from models.abstract_bicycle import AbstractBicycle


class Unicycle(AbstractBicycle):
    """
    A class representing a unicycle.

    Attributes:
        seat_lift_height_in_meter (float): The seat lift height of the unicycle in meters.
        wheel_radius (float): The radius of the wheel of the unicycle.
        bike_brand (str): The brand of the unicycle.
        current_speed (float): The current speed of the unicycle.
        max_speed (float): The maximum speed of the unicycle.

    Methods:
        get_max_distance(): Get the maximum distance the unicycle can travel.
        __str__(): Return a string representation of the unicycle.

    """

    def __init__(self, seat_lift_height_in_meter=0, wheel_radius=0, bike_brand="no information",
                 current_speed=0, max_speed=0):
        """
        Initialize a Unicycle instance.

        Args:
            seat_lift_height_in_meter (float, optional): The seat lift height of the unicycle in meters. Defaults to 0.
            wheel_radius (float, optional): The radius of the wheel of the unicycle. Defaults to 0.
            bike_brand (str, optional): The brand of the unicycle. Defaults to "no information".
            current_speed (float, optional): The current speed of the unicycle. Defaults to 0.
            max_speed (float, optional): The maximum speed of the unicycle. Defaults to 0.

        """
        self.seat_lift_height_in_meter = seat_lift_height_in_meter
        self.wheel_radius = wheel_radius
        self.best_shops = {"velo planeta ", "velo sklad"}
        super().__init__(bike_brand, current_speed, max_speed)

    @staticmethod
    def get_max_distance():
        """
        Get the maximum distance the unicycle can travel.

        Returns:
            float: The maximum distance the unicycle can travel.

        """
        return 0.1

    def __str__(self):
        """
        Return a string representation of the unicycle.

        Returns:
            str: The string representation of the unicycle.

        """
        return f"Bike seat lift height - {self.seat_lift_height_in_meter}, Bike wheel radius - {self.wheel_radius}," \
               f" {super().__str__()}"
