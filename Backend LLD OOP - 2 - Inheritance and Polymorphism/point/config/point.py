import copy


class Point:
    def __init__(self, x, y):
        # TODO: Initialize the Point class with x and y coordinates
        self.x = x
        self.y = y

    def __eq__(self, other):
        # TODO: Implement equality comparison between two points

        # Right Way
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

        # if self.x == other.x and self.y == other.y:
        #     return True
        # else:
        #     return False


    def __str__(self):
        # TODO: Return a string representation of the point in the format "(x, y)"
        return F"({self.x}, {self.y})"

    def __copy__(self):
        # TODO: Create a shallow copy of the point
        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        # TODO: Create a deep copy of the point using the copy module
        return Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))
