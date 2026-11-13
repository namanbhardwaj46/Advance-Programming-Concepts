import threading


# Define the Adder class that inherits from threading.Thread
class Adder(threading.Thread):
    # TODO: Implement the logic to print "I am the Adder class"
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("I am the Adder class")

# Define the Subtractor class that inherits from threading.Thread
class Subtractor(threading.Thread):
    # TODO: Implement the logic to print "I am the Subtractor class"
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("I am the Subtractor class")

# Define the Client class with a static main method to manage thread execution
class Client:
    @staticmethod
    def main():
        # TODO: Print "I am the main class"
        print("I am the main class")

        # TODO: Initialize and start instances of Adder and Subtractor threads
        adder = Adder()
        adder.start()
        subtractor = Subtractor()
        subtractor.start()

        # TODO: Ensure that the main method waits for both threads to complete
        adder.join()
        subtractor.join()


if __name__ == "__main__":
    Client.main()
