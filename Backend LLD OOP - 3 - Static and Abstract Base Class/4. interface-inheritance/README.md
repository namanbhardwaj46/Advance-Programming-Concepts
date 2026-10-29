#Interface Inheritance and Implementation
## Problem Statement
You are tasked with creating a Python class hierarchy that demonstrates the implementation of multiple interfaces and inheritance between interfaces. The system should provide functionality for defining and implementing interfaces with abstract methods.


## Requirements
The class hierarchy should include the following components:
1. Interface I1:
    - Abstract methods:
        - fun1(self)
        - fun(self)
2. Interface I2:
    - Abstract methods:
        - fun2(self)
        - fun(self)
3. Interface I (derived from I1 and I2):
    - Inherits the abstract methods from both I1 and I2.
4. Class C (implementing I):
    - This class implements the interface I and provides concrete implementations for the abstract methods defined in I.
5. Ensure that interfaces I1 and I2 contain only abstract method signatures without any implementation details.

## Instructions
- Implement the I1, I2, and I interfaces according to the specified requirements.
- Implement the C class, which inherits from the I interface and provides concrete implementations for the abstract methods.
