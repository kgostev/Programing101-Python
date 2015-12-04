import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rado", 0, "$")

    def test_init(self):
        self.assertEqual(
            str(self.account), 'Bank account for Rado with balance of 0$')

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.balance(), 1000)

    def test_int(self):
        self.account.deposit(1000)
        self.assertEqual(int(self.account), self.account.balance())

    def test_withdrow(self):
        self.account.deposit(1000)
        self.account.withdrow(1000)
        self.assertEqual(int(self.account), 0)

    def test_history(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.history(), [
                         'Account was created', 'Deposited 1000$'])

    def test_transfer(self):
        account2 = BankAccount("Bat Georgi", 100, "$")
        account2.transfer_to(self.account, 100)
        self.assertEqual(account2.balance(), 0)
        self.assertEqual(self.account.balance(), 100)


if __name__ == '__main__':
    unittest.main()
