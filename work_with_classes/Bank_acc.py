class Bank_acc:
    def __init__(self, name, balance):
        self.name = name

        self.__balance = balance

    @property
    def my_balance(self):
        return f'{self.name} {self.__balance}'

    @my_balance.setter
    def my_balance(self, value):
        self.__balance = value
