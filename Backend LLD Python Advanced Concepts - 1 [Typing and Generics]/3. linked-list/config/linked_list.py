from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T):
        #todo
        self.data: T = data # the value stored in this node
        self.next = None    # link to next node (None if last)

class LinkedList(Generic[T]):
    def __init__(self):
        #todo
        self.head = None    # start of the list
        self.tail = None    # end of the list

    def append(self, data: T):
        #todo
        """
        Add a new node with the given data to the end of the list.
        """
        new_node = Node(data)
        if not self.head:
            # If list is empty, new node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, link it after tail and update tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:

# Create a linked list of integers
ll_int = LinkedList[int]()
ll_int.append(1)
ll_int.append(2)
ll_int.append(3)
ll_int.print_list()  # Output: 1 -> 2 -> 3 -> None

# Create a linked list of strings
ll_str = LinkedList[str]()
ll_str.append("a")
ll_str.append("b")
ll_str.append("c")
ll_str.print_list()  # Output: a -> b -> c -> None