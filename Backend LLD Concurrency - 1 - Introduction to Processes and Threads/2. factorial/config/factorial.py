import math
import threading


# Todo: implement the factorial thread class
class FactorialThread(threading.Thread):
    # write code here
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None

    def run(self):
        self.result = math.factorial(self.n)



def compute_large_factorial(n):
    # Todo: Create a factorial thread
    factorial_thread = FactorialThread(n)
    factorial_thread.start()

    # Todo: wait for calc to finish by calling the join method
    factorial_thread.join()

    # Todo: return the result
    return factorial_thread.result
    