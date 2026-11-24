# Concurrent Counter Management

## Problem statement
This Python program is created to implement multithreading concepts. The program has a `Counter` class with 
methods to increment, decrement, and retrieve the counter value. It then creates multiple threads to perform concurrent 
increment and decrement operations on the counter.

## Requirements

### Class `Counter`
- Represents a counter object with an initial count.
- Provides methods for incrementing, decrementing, and retrieving the counter value.
- Methods:
  - `__init__(self, initial_count)`: Initializes the counter with the specified initial count.
  - `incValue(self, offset)`: Increments the counter value by the specified `offset`.
  - `decValue(self, offset)`: Decrements the counter value by the specified `offset`.
  - `getValue(self)`: Retrieves the current value of the counter.

### Concurrent Operations
- Functions `concurrent_inc()` and `concurrent_dec()` perform concurrent increment and decrement operations on the 
counter.
- Each function is executed by multiple threads to simulate concurrent operations.

## Instructions
1. Implement the methods of the `Counter` class as per the provided TODO comments.
2. The program will create and start multiple threads for concurrent increment and decrement operations.
3. After all threads complete execution, the final value of the counter will be printed.

Ensure that the Python environment supports threading to execute the program effectively.

