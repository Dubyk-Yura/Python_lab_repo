class Bicycle:
    """
    A class representing a bicycle.

    Attributes:
    -----------
    BIKE_PRICE : int
        The base price for all bikes (class variable).
    instance : Bicycle or None
        Singleton instance of the Bicycle class (class variable).
    bike_type : str
        The type of bike (e.g. mountain bike, road bike, etc.).
    bike_brand : str
        The brand of the bike.
    current_speed : int
        The current speed of the bike.
    max_speed : int
        The maximum speed of the bike.

    Methods:
    --------
    __init__(self, bike_type="no information", bike_brand="no information", current_speed=0, max_speed=0):
        Initializes a new Bicycle object with the specified attributes.
    accelerate(self, speed):
        Increases the current speed of the bike by the specified amount.
    brake(self):
        Stops the bike and sets the current speed to zero.
    increase_price(self, price):
        Adds the base price to the specified price and prints the result.
    get_instance():
        Returns the singleton instance of the Bicycle class.
    __str__(self):
        Returns a string representation of the Bicycle object.
    """
    BIKE_PRICE = 10000
    instance = None

    def __init__(self, bike_type="no information", bike_brand="no information", current_speed=0, max_speed=0):
        self.__bike_type = bike_type
        self.__bike_brand = bike_brand
        self.__current_speed = current_speed
        self.__max_speed = max_speed

    def accelerate(self, speed):
        """
        Increases the current speed of the bike by the specified amount.

        Parameters:
        -----------
        speed : int
        The amount to increase the current speed by.
        """
        if (self.__current_speed + speed) > self.__max_speed:
            print("Speed with accelerate is more than maximum speed")
            return
        self.__current_speed += speed
        print(f"Current speed is changed and it equal to {self.__current_speed}")

    def brake(self):
        """
        Stops the bike and sets the current speed to zero.
        """
        self.__current_speed = 0
        print(f"bike {self.__bike_brand} was stopped;")

    def increase_price(self, price):
        """
        Adds the base price to the specified price and prints the result.

        Parameters:
        -----------
        price : int
        The price to increase by the base price.
        """
        price += self.BIKE_PRICE
        print(f"Price of bicycle after increase is {price}")

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of the Bicycle class.
        If no instance exists, a new instance is created.

        Returns:
        --------
        Bicycle
            The singleton instance of the Bicycle class.
        """
        if not Bicycle.instance:
            Bicycle.instance = Bicycle()
        return Bicycle.instance

    def __str__(self):
        return f"Bike type - {self.__bike_type}, Bike brand = {self.__bike_brand}, Current speed = " \
               f"{self.__current_speed}, Bike max speed = {self.__max_speed}"

    @property
    def bike_type(self):
        return self.__bike_type

    @property
    def bike_brand(self):
        return self.__bike_brand

    @property
    def current_speed(self):
        return self.__current_speed

    @property
    def max_speed(self):
        return self.__max_speed

    @bike_type.setter
    def bike_type(self, new_bike_type):
        self.__bike_type = new_bike_type

    @bike_brand.setter
    def bike_brand(self, new_bike_brand):
        self.__bike_brand = new_bike_brand

    @current_speed.setter
    def current_speed(self, new_bike_current_speed):
        self.__current_speed = new_bike_current_speed

    @max_speed.setter
    def max_speed(self, new_bike_max_speed):
        self.__max_speed = new_bike_max_speed
