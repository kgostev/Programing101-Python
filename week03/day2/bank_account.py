class BankAccount:

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append('Deposited {}{}'.format(amount, self.__currency))

    def balance(self):
        self.__history.append(
            'Balance checked -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance

    def withdrow(self, amount):
        self.__balance -= amount
        self.__history.append('Withdrown {}{}'.format(
            self.__balance, self.__currency))

    def history(self):
        return self.__history

    def transfer_to(self, other, amount):
        self.withdrow(amount)
        other.deposit(amount)

    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = ['Account was created']

    def __str__(self):
        return 'Bank account for {} with balance of {}{}'.format(self.__name, self.__balance, self.__currency)

    def __repr__(self):
        return str(self)

    def __int__(self):
        self.__history.append(
            '__int__ checked -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance
