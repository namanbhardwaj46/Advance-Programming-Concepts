# Rentable Vehicles Management System

## Overview
This Python code outlines a system for managing rentable objects, including cars and bicycles. The script utilizes 
abstract classes and methods to define a common interface for handling rental operations.

## Implementation Details

### Abstract Class `Rentable`
- This class is an abstract base class (ABC) that defines two abstract methods:
  - `rent()`: Method to rent the vehicle.
  - `return_item()`: Method to return the rented vehicle.

### Class `Car`
- Inherits from the `Rentable` class.
- Represents a car object with variables `car_model` and `is_rented`.
- Has the `rent()` and `return_item()` methods specific to cars.

### Class `Bicycle`
- Inherits from the `Rentable` class.
- Represents a bicycle object with variables `bicycle_model` and `is_rented`.
- Has the `rent()` and `return_item()` methods specific to bicycles.

## Instructions
1. Implement the `Rentable` class by providing implementations for the `rent()` and `return_item()` methods.
2. Implement the `Car` class and its methods:
   - Complete the `__init__()` method by initializing the `car_model` variable and a boolean variable `is_rented` which tells
    if the current car is rented or not.
   - Implement the `rent()` method in which if the car is already rented then print "`Car <car_model> is already rented`",otherwise
   mark the current car as rented and print "`Car <car_model> is now rented`".
   - Implement the `return_item()` method in which, if the car is rented then return the car back and print "`Car <car_model> is now returned`" otherwise print
   "`Car <car_model> is not rented`".
3. Implement the `Bicycle` class and its methods:
   - Complete the `__init__()` method by initializing the `bicycle_model` variable and a boolean variable `is_rented` which tells
    if the current bicycle is rented or not.
   - Implement the `rent()` method in which if the bicycle is already rented then print "`Cycle <bicycle_model> is already rented`",otherwise
   mark the current bicycle as rented and print "`Cycle <bicycle_model> is now rented`".
   - Implement the `return_item()` method in which, if the cycle is rented then return the cycle back and print "`Cycle <bicycle_model> is now returned`" otherwise print
   "`Cycle <bicycle_model> is not rented`".
- The unit tests will only verify the  `is_rented` variable of a vehicle, but you have to write relevant messages for renting and returning a vehicle.
- Ensure that the methods are properly implemented to manage object rentals effectively.

