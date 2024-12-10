class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Entity):
    def move(self):
        return "Running"


class Bird(Entity):
    def move(self):
        return "Flying"


class Car(Entity):
    def move(self):
        return "Driving"


class Plane(Entity):
    def move(self):
        return "Flying"


def demonstrate_movement(entities):
    for entity in entities:
        print(f"{entity.__class__.__name__}: {entity.move()}")


entities = [Dog(), Bird(), Car(), Plane()]

demonstrate_movement(entities)
