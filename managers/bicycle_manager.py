from models.bicycle import Bicycle
from models.electro_bicycle import ElectroBicycle
from models.tricycle import Tricycle
from models.unicycle import Unicycle


class BicycleManager:
    def __init__(self):
        self.bicycles = []

    def add_bicycle(self, bicycle):
        self.bicycles.append(bicycle)

    def find_all_with_max_speed_higher_than(self, max_speed):
        return [bicycle for bicycle in self.bicycles if bicycle.max_speed > max_speed]

    def find_all_with_current_speed_lower_than(self, current_speed):
        return [bicycle for bicycle in self.bicycles if bicycle.current_speed < current_speed]

    def __len__(self):
        return len(self.bicycles)

    def __getitem__(self, idx):
        return self.bicycles[idx]

    def __iter__(self):
        return iter(self.bicycles)

    def print_max_distance(self):
        return [bicycle.get_max_distance() for bicycle in self.bicycles]

    def use_enumerate(self):
        return [f"Index: {index}, Bicycle information: {bicycle}" for index, bicycle in
                enumerate(self.bicycles)]

    def use_zip_to_connect_object(self):
        list_max_distances = self.print_max_distance()
        return [f"Max distance of {bicycle} is {max_distance}" for bicycle, max_distance in
                zip(self.bicycles, list_max_distances)]

    def check_objects(self, conditions):
        result = {'all': all(conditions(obj) for obj in self.bicycles),
                  'any': any(conditions(obj) for obj in self.bicycles)}
        return result
