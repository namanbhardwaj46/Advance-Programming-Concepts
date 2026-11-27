# Generic Comparison Function

## Problem Statement
You are tasked with implementing a generic comparison function `compare` in Python that can compare two objects of the same type. The function should support direct comparison of objects as well as comparison based on a provided key function that extracts a comparable key from each object.

## Requirements
The `compare` function should have the following signature:

1. compare:
    - The function should accept the following arguments:
        - x (type T): The first object to compare.
        - y (type T): The second object to compare.
        - key (type Callable[[T], any], optional): A function that extracts a comparable key from each object. If not provided, the function should perform direct comparison of the objects.
    - The function should return an integer value based on the comparison result:
        - -1 if x is less than y.
        - 0 if x is equal to y.
        - 1 if x is greater than y.
2. The function should handle both direct comparison of objects and comparison based on a provided key function.

## Instructions
- Implement the `compare` function according to the specified requirements.
- Ensure that the function handles both direct comparison and comparison using a key function.
- You can extract the value of object x to compare by calling key(x) if a key function is provided for the object.