# Multi-threaded Addition Program

## Overview
This Python program demonstrates multi-threaded addition functionality using the `Client` and `Adder` classes. The program takes two numbers as input from the user, creates a new thread, and invokes the `Adder` class to calculate and print the sum of the two numbers.

## Implementation Details

### Class `Adder`
- Inherits from the `threading.Thread` class.
- Represents a thread that performs addition of two numbers.
- Initializes with two numbers (`num1` and `num2`) provided as input.
- Overrides the `run()` method to calculate and print the sum of `num1` and `num2`.

### Class `Client`
- Contains a static method `main()` that serves as the entry point of the program.
- Prompts the user to enter two numbers.
- Creates an instance of the `Adder` class with the provided numbers.
- Starts the thread and waits for its completion.

## Instructions
To run the program:
1. Execute the `Client` class's `main()` method.
2. Enter two numbers when prompted.
3. The program will create a new thread to calculate and print the sum of the provided numbers.

Ensure that the program runs in a Python environment with threading support.

