from Bicycle import Bicycle

if __name__ == "__main__":
    bicycles = [Bicycle() for _ in range(4)]
    bicycles[0] = Bicycle()
    bicycles[1] = Bicycle("Some type", "Some brand ", 10, 20)
    bicycles[2] = Bicycle.get_instance()
    bicycles[3] = Bicycle.get_instance()

    for bicycle in bicycles:
        print(f"Bicycle : {bicycle.__str__()}")
