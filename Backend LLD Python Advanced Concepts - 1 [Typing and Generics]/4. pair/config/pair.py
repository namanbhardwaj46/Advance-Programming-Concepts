from typing import TypeVar

# TODO: Declare two type variables `T` and `U`.
T = TypeVar('T')
U = TypeVar('U')

class Pair:
    #TODO: Implement the constructor to initialize the two pair values
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    # TODO: Implement this method to return the string representation of the pair as shown in the readme
    def __repr__(self):
        return f"Pair({self.first}, {self.second})"


# Example usage:

# Create a pair of integers and strings
pair1 = Pair(1, "apple")
print(pair1)  # Output: Pair(1, apple)

# Create a pair of float and list
pair2 = Pair(3.14, [1, 2, 3])
print(pair2)  # Output: Pair(3.14, [1, 2, 3])

# Create a pair of tuple and dictionary
pair3 = Pair((1, 2), {"a": 1, "b": 2})
print(pair3)  # Output: Pair((1, 2), {'a': 1, 'b': 2})
