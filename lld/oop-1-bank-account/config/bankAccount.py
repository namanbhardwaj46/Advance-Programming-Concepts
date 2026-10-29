class BankAccount:
    # TODO: Initialize the constructor
    def __init__(self, accountNumber, balance, roi):
        self._accountNumber = accountNumber
        self.__balance = balance
        self._roi = roi

    # TODO: Implement this method to calculate the simple interest
    def getSimpleInterest(self, time):
        return float((self.__balance * self._roi * time) / 100)

    #TODO: Implement this method to return the total amount after adding the interest
    def getBalanceWithInterest(self, time):
        return float(self.__balance + self.getSimpleInterest(time))
