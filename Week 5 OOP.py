class Gadget:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_details(self):
        return f"Brand: {self.brand}, Price: ${self.price}"


class Smartphone(Gadget):
    def __init__(self, brand, price, model, storage, battery_capacity):
        super().__init__(brand, price)
        self.__model = model
        self.storage = storage
        self.battery_capacity = battery_capacity

    def get_model(self):
        return self.__model

    def get_details(self):
        return (f"Smartphone - Brand: {self.brand}, Model: {self.__model}, Price: ${self.price}, "
                f"Storage: {self.storage}GB, Battery: {self.battery_capacity}mAh")

    def make_call(self, number):
        return f"Calling {number} from your {self.__model}..."


class Smartwatch(Gadget):
    def __init__(self, brand, price, model, fitness_tracking):
        super().__init__(brand, price)
        self.model = model
        self.fitness_tracking = fitness_tracking

    def get_details(self):
        return (f"Smartwatch - Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, "
                f"Fitness Tracking: {'Yes' if self.fitness_tracking else 'No'}")


phone = Smartphone("Samsung", 999, "Galaxy S21", 128, 4000)
watch = Smartwatch("Apple", 399, "Apple Watch Series 8", True)

print(phone.get_details())
print(phone.make_call("123-456-7890"))
print(watch.get_details())                
