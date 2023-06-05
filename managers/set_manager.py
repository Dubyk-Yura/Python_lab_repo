# pylint: disable=line-too-long
"""
set_manager.py

This module provides the SetManager class, which represents a manager for a collection of sets of best shops.

The SetManager class allows iterating over the best shops from the managed bicycles.

Example:
    bicycles_manager = BicycleManager()
    # Add bicycles to the manager
    set_manager = SetManager(bicycles_manager)
    for shop in set_manager:
        print(shop)
    ...

"""
from managers.bicycle_manager import BicycleManager


class SetManager:
    """
    SetManager class represents a manager for a collection of sets of best shops.

    Attributes:
        bicycle_manager (BicycleManager): The bicycle manager object.
        current_index (int): The current index for iteration.

    Methods:
        __len__: Get the total number of best shops in the manager.
        __iter__: Iterate over the best shops from the managed bicycles.
        __getitem__: Get the best shop at the specified index.
        __next__: Get the next best shop in the iteration.

    """

    def __init__(self, bicycle_manager):
        """
        Initialize a SetManager instance.

        Args:
            bicycle_manager (BicycleManager): The bicycle manager object.
        """
        if not isinstance(bicycle_manager, BicycleManager):
            raise TypeError("field in constructor is no object of class BicycleManager")
        self.bicycle_manager = bicycle_manager
        self.current_index = 0

    def __len__(self):
        """
        Get the total number of best shops in the manager.

        Returns:
            int: The total number of best shops.
        """
        return sum(len(bicycle.best_shops) for bicycle in self.bicycle_manager)

    def __iter__(self):
        """
        Iterate over the best shops from the managed bicycles.

        Yields:
            object: The next best shop in the iteration.
        """
        for bicycle in self.bicycle_manager:
            yield from bicycle.best_shops

    def __getitem__(self, item):
        """
        Get the best shop at the specified index.

        Args:
            item (int): The index of the best shop.

        Returns:
            object: The best shop at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        temp = 0
        for bicycle in self.bicycle_manager:
            if temp <= item < temp + len(bicycle.best_shops):
                return list(bicycle.best_shops)[item - temp]
            temp += len(bicycle.best_shops)
        raise IndexError

    def __next__(self):
        """
        Get the next best shop in the iteration.

        Returns:
            object: The next best shop.

        Raises:
            StopIteration: If there are no best shops to iterate over.
        """
        if self.current_index < len(self):
            item = self[self.current_index]
            self.current_index += 1
            return item
        raise StopIteration
