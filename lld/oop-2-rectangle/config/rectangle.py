import copy

from config.point import Point


class Rectangle:
    def __init__(self, *args):
        """
        Initialize a Rectangle object.

        Args:
            *args: Variable number of arguments. The constructor can be called in three ways:
                - With two Point objects representing the top-left and bottom-right corners.
                - With four integers representing the x and y coordinates of the top-left and bottom-right corners.
                - With a single Rectangle object for copying.

        Raises:
            ValueError: If invalid arguments are provided.
        """
        # # Case 1: Copy constructor
        # if len(args) == 1 and isinstance(args[0], Rectangle):
        #     other = args[0]
        #     self.topLeft = copy.deepcopy(other.topLeft)
        #     self.bottomRight = copy.deepcopy(other.bottomRight)
        # # Case 2: Two Point objects
        # elif len(args) == 2 and all(isinstance(arg, Point) for arg in args):
        #     tl, br = args
        #     # Ensure coordinates form a valid rectangle
        #     if tl.x > br.x or tl.y > br.y:
        #         raise ValueError(f"Invalid corner points: {tl}, {br}")
        #     self.topLeft = copy.deepcopy(tl)
        #     self.bottomRight = copy.deepcopy(br)
        # # Case 3: Four integers
        # elif len(args) == 4 and all(isinstance(arg, int) for arg in args):
        #     x1, y1, x2, y2 = args
        #     # Validate coordinates
        #     if x1 > x2 or y1 > y2:
        #         raise ValueError(f"Invalid coordinates: ({x1}, {y1}), ({x2}, {y2})")
        #     self.topLeft = Point(x1, y1)
        #     self.bottomRight = Point(x2, y2)
        # else:
        #     raise ValueError("Rectangle __init__ expects either: - a Rectangle instance, - two Point instances, - or four integer coordinates"
        #     )

        if len(args) == 2:
            # If two Point objects are provided, initialize from points
            self.topLeft = copy.deepcopy(args[0])
            self.bottomRight = copy.deepcopy(args[1])
        elif len(args) == 4:
            # If four integer coordinates are provided, initialize from coordinates
            self.topLeft = Point(args[0], args[1])
            self.bottomRight = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], Rectangle):
            # If a Rectangle object is provided, initialize by copying
            self.topLeft = copy.deepcopy(args[0].topLeft)
            self.bottomRight = copy.deepcopy(args[0].bottomRight)
        else:
            raise ValueError("Invalid arguments provided.")

