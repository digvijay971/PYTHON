class BMW:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"{self.model} BMW engine started."

    def drive(self):
        return f"Driving the {self.model} BMW smoothly on the highway."

    def fuel_type(self):
        return "Petrol or electric"


class Tata:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"{self.model} Tata engine started."

    def drive(self):
        return f"Driving the {self.model} Tata confidently around the city."

    def fuel_type(self):
        return "Diesel or electric"


def show_car_behavior(car):
    print(car.start_engine())
    print(car.drive())
    print("Fuel type:", car.fuel_type())
    print("---")


if __name__ == "__main__":
    bmw_car = BMW("X5")
    tata_car = Tata("Nexon")

    print("Polymorphism example with BMW and Tata")
    show_car_behavior(bmw_car)
    show_car_behavior(tata_car)
