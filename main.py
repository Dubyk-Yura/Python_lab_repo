import sys
from managers.bicycle_manager import BicycleManager
from models.bicycle import Bicycle
from models.electro_bicycle import ElectroBicycle
from models.tricycle import Tricycle
from models.unicycle import Unicycle

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
