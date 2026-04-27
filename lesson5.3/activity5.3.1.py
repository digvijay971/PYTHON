class a:
    def __init__(self, name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class b(a):
    pass
school_bus = b("School Bus", 120, 15)
print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)