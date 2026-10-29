from abc import ABC, abstractmethod

# Interface I1
class I1(ABC):
    ## Implement the abstract methods
    """Abstract method fun1 must be overridden by subclasses."""
    @abstractmethod
    def fun1(self):
        pass

    """Abstract method fun (from I1) must be overridden by subclasses."""
    @abstractmethod
    def fun(self):
        pass

# Interface I2
class I2(ABC):
    ## Implement the abstract methods
    """Abstract method fun2 must be overridden by subclasses."""
    @abstractmethod
    def fun2(self):
        pass

    """Abstract method fun (from I2) must be overridden by subclasses."""
    @abstractmethod
    def fun(self):
        pass

# Interface I extending both I1 and I2
class I(I1, I2):
    """
    Inherits all abstract methods from I1 and I2:
      - fun1(self)
      - fun2(self)
      - fun(self)  (note: declared in both I1 and I2, but only needs to be implemented once)
    """
    pass

# Todo
# Class C implements I (and therefore must implement fun1, fun2, and fun)
class C(I):
    def fun1(self):
        print("fun1 implementation in C")

    def fun2(self):
        print("fun2 implementation in C")

    def fun(self):
        print("fun implementation in C")
