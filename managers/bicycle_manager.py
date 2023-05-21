class BicycleManager:
    def __init__(self):
        self.bicycles = list()

    def add_bicycle(self, bicycle):
        self.bicycles.append(bicycle)

    def find_all_with_max_speed_higher_than(self, max_speed):
        return [bicycle for bicycle in self.bicycles if bicycle.max_speed > max_speed]

    # return list(filter(lambda bicycle: bicycle.max_speed > max_speed, self.bicycles))

    def find_all_with_current_speed_lower_than(self, current_speed):
        return [bicycle for bicycle in self.bicycles if bicycle.current_speed < current_speed]

    # return list(filter(lambda bicycle: bicycle.current_speed < current_speed, self.bicycles))
