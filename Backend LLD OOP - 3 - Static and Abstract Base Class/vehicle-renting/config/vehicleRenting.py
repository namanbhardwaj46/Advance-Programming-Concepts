from abc import ABC, abstractmethod


# TODO: Implement Rentable class
class Rentable(ABC):
    @abstractmethod
    def rent(self):
        """Rent the item. Implement in subclasses."""
        pass


    @abstractmethod
    def return_item(self):
        """Return the rented item. Implement in subclasses."""
        pass



# TODO: Implement the Car class and its methods
class Car(Rentable):
    def __init__(self, car_model):
        self.car_model = car_model
        self.is_rented: bool = False


    def rent(self):
        if not self.is_rented:
            # Complete the code
            self.is_rented = True
            return f"Car {self.car_model} is now rented"
        else:
            # Complete the code
            return f"Car {self.car_model} is already rented"

    def return_item(self):
        if self.is_rented:
            # Complete the code
            self.is_rented = False
            return f"Car {self.car_model} is now returned"
        else:
            # code here
            return f"Car {self.car_model} is not rented"


# TODO: Implement the Bicycle class and its methods
class Bicycle(Rentable):
    def __init__(self, bicycle_model):
        self.bicycle_model = bicycle_model
        self.is_rented: bool = False


    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            return f"Cycle {self.bicycle_model} is now rented"
        else:
            return f"Cycle {self.bicycle_model} is already rented"


    def return_item(self):
        if self.is_rented:
            self.is_rented = False
            return f"Cycle {self.bicycle_model} is now returned"
        else:
            return f"Cycle {self.bicycle_model} is not rented"

