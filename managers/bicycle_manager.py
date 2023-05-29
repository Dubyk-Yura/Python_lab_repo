# pylint: disable=line-too-long
"""
This module provides the BicycleManager class, which represents a manager for a collection of bicycles.

The BicycleManager class allows adding bicycles, finding bicycles based on certain criteria, and performing operations
on the managed bicycles.

"""


class BicycleManager:
    """
        BicycleManager class represents a manager for a collection of bicycles.

        Attributes:
            bicycles (list): List of bicycles managed by the BicycleManager.

        Methods:
            add_bicycle: Add a bicycle to the manager.
            find_all_with_max_speed_higher_than: Find all bicycles with a maximum speed higher than the given value.
            find_all_with_current_speed_lower_than: Find all bicycles with a current speed lower than the given value.
            __len__: Get the number of bicycles in the manager.
            __getitem__: Get the bicycle at the specified index.
            __iter__: Iterate over the bicycles in the manager.
            print_max_distance: Get the maximum distance for each bicycle in the manager.
            use_enumerate: Use enumerate to iterate over the bicycles with their corresponding index.
            use_zip_to_connect_object: Use zip to connect each bicycle with its corresponding maximum distance.
            check_objects: Check the conditions on all bicycles in the manager.

        """

    def __init__(self):
        self.bicycles = []

    def add_bicycle(self, bicycle):
        """
        Add a bicycle to the manager.

        Args:
            bicycle (Bicycle): The bicycle object to be added.
        """
        self.bicycles.append(bicycle)

    def find_all_with_max_speed_higher_than(self, max_speed):
        """
        Find all bicycles with a maximum speed higher than the given value.

        Args:
            max_speed: The maximum speed of bike.

        Returns:
            list: List of bicycles with a maximum speed higher than the given value.
        """
        return [bicycle3 for bicycle3 in self.bicycles if bicycle3.max_speed > max_speed]

    def find_all_with_current_speed_lower_than(self, current_speed):
        """
        Find all bicycles with a current speed lower than the given value.

        Args:
            current_speed: The current speed of bike.

        Returns:
            list: List of bicycles with a current speed lower than the given value.
        """
        return [bicycle2 for bicycle2 in self.bicycles if bicycle2.current_speed < current_speed]

    def __len__(self):
        return len(self.bicycles)

    def __getitem__(self, idx):
        return self.bicycles[idx]

    def __iter__(self):
        return iter(self.bicycles)

    def print_max_distance(self):
        """
        Get the maximum distance for each bicycle in the manager.

        Returns:
            list: List of maximum distances for each bicycle.
        """
        return [bicycle4.get_max_distance() for bicycle4 in self.bicycles]

    def use_enumerate(self):
        """
        Use enumerate to iterate over the bicycles with their corresponding index.

        Returns:
            list: List of strings containing the index and bicycle information.
        """
        return [f"Index: {index}, Bicycle information: {bicycle5}" for index, bicycle5 in
                enumerate(self.bicycles)]

    def use_zip_to_connect_object(self):
        """
        Use zip to connect each bicycle with its corresponding maximum distance.

        Returns:
            list: List of strings containing the bicycle and its maximum distance.
        """
        list_max_distances = self.print_max_distance()
        return [f"Max distance of [{bicycle6}] is {max_distance}" for bicycle6, max_distance in
                zip(self.bicycles, list_max_distances)]

    # pylint: disable=use-dict-literal
    def check_objects(self, conditions):
        """
        Check the conditions on all bicycles in the manager.

        Args:
            conditions (callable): A callable object that takes a bicycle object and returns a boolean.

        Returns:
            dict: Dictionary with 'all' and 'any' keys indicating if all or any bicycles satisfy the conditions.
        """

        result = dict(all=all(conditions(obj) for obj in self.bicycles),
                      any=any(conditions(obj) for obj in self.bicycles))
        return result
