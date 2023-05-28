# pylint: disable=line-too-long
"""
This module demonstrates the usage of the BicycleManager class and various decorators.

It creates a BicycleManager instance, adds different types of bicycles to it, and performs various operations on
the bicycles.

The module also showcases the usage of decorators 'return_name' and 'from_iter_to_tuple'.
"""
# pylint: disable=import-error
from decorators import return_name
from decorators import from_iter_to_tuple
from managers.bicycle_manager import BicycleManager
from models.bicycle import Bicycle
from models.electro_bicycle import ElectroBicycle
from models.tricycle import Tricycle
from models.unicycle import Unicycle

# pylint: disable=missing-function-docstring
if __name__ == "__main__":
    bicycles_manager = BicycleManager()
    bicycles_manager.add_bicycle(Bicycle("Apple", "mountain", 4, 7))
    bicycles_manager.add_bicycle(Bicycle("Xiaomi", "non-mountain", 30, 40))
    bicycles_manager.add_bicycle(Unicycle(3, 2, "Uni-company", 2, 5))
    bicycles_manager.add_bicycle(Unicycle(1, 2, "Evil Company", 1, 4))
    bicycles_manager.add_bicycle(Tricycle(True, 2, "Tri-company", 5, 10))
    bicycles_manager.add_bicycle(Tricycle(False, 1, "Company", 4, 6))
    bicycles_manager.add_bicycle(ElectroBicycle(2, 10, "Samsung", 32, 45))
    bicycles_manager.add_bicycle(ElectroBicycle(4, 15, "Electro", 30, 35))

    print("Print all bicycles ->")
    for bicycle in bicycles_manager.bicycles:
        print(bicycle)
    print("\n")

    print("Print with some conditions ->\n")
    for bicycle in bicycles_manager.find_all_with_max_speed_higher_than(20):
        print(bicycle)
    print()

    for bicycle in bicycles_manager.find_all_with_current_speed_lower_than(2):
        print(bicycle)

    print(bicycles_manager.print_max_distance())

    print(bicycles_manager.use_enumerate())

    print(bicycles_manager.use_zip_to_connect_object())


    def condition(bicycle2):
        return bicycle2.max_speed > 0


    print(bicycles_manager.check_objects(condition))


    def condition2(bicycle3):
        return bicycle3.max_speed > 10


    print(bicycles_manager.check_objects(condition2))

    print("Test decorators")


    @return_name
    def add_func(first_el, second_el):
        return first_el + second_el


    print(add_func(1, 2))


    @from_iter_to_tuple
    def list_func():
        return [1, 3, 4, 56, 5, ]


    print(list_func())
