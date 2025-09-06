# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # calling the parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}")

    def charge(self):
        print(f"🔋 Charging {self.device_info()}... Battery at {self.battery}%")

    # Encapsulation example (private method)
    def __optimize_performance(self):
        print("⚡ Optimizing system performance...")

    def run_diagnostics(self):
        self.__optimize_performance()
        print("🛠️ Diagnostics completed successfully!")


# Example usage
phone = Smartphone("Samsung", "Galaxy S24", "256GB", 80)
phone.make_call("0712345678")
phone.charge()
phone.run_diagnostics()




class Vehicle:
    def move(self):
        print("This vehicle moves in some way...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Same method name, different behavior



