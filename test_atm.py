import io
import unittest.mock
from atm import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        self.test_checking_balance = 1000
        self.test_savings_balance = 2000
        self.atm = ATM(self.test_checking_balance, self.test_savings_balance, 0.05)

    def test_display_balance(self):
        expected_output = \
        f"Checking Balance: ${self.test_checking_balance:.2f}\n" + \
        f"Savings Balance: ${self.test_savings_balance:.2f}\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.display_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_check_balance_checking(self):
        expected_output = f"Checking Balance: ${self.test_checking_balance:.2f}\n"
        with unittest.mock.patch('builtins.input', side_effect=['c']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.check_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_check_balance_savings(self):
        expected_output = \
        f"Savings Balance: ${self.test_savings_balance:.2f}\n" + \
        "Your monthly interest is $8.33.\n"
        with unittest.mock.patch('builtins.input', side_effect=['s', 'y']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.check_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_deposit_checking(self):
        amount_to_deposit = 500
        with unittest.mock.patch('builtins.input', side_effect=['checking', str(amount_to_deposit)]), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.deposit()
            self.assertEqual(self.atm.checking_balance, self.test_checking_balance + amount_to_deposit)

    def test_deposit_savings(self):
        amount_to_deposit = 500
        with unittest.mock.patch('builtins.input', side_effect=['savings', str(amount_to_deposit)]), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.deposit()
            self.assertEqual(self.atm.savings_balance, self.test_savings_balance + amount_to_deposit)

    def test_withdraw_checking_sufficient(self):
        amount_to_withdraw = 500
        with unittest.mock.patch('builtins.input', side_effect=['checking', str(amount_to_withdraw)]), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.withdraw()
            self.assertEqual(self.atm.checking_balance, self.test_checking_balance - amount_to_withdraw)

    def test_withdraw_checking_insufficient(self):
        amount_to_withdraw = self.test_checking_balance + 500
        with unittest.mock.patch('builtins.input', side_effect=['checking', str(amount_to_withdraw)]):
            self.atm.withdraw()
            self.assertEqual(self.atm.checking_balance, self.test_checking_balance)

    def test_withdraw_savings_sufficient(self):
        amount_to_withdraw = 1000
        with unittest.mock.patch('builtins.input', side_effect=['savings', str(amount_to_withdraw)]), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.withdraw()
            self.assertEqual(self.atm.savings_balance, self.test_savings_balance - amount_to_withdraw)

    def test_withdraw_savings_insufficient(self):
        amount_to_withdraw = self.test_savings_balance + 1000
        with unittest.mock.patch('builtins.input', side_effect=['savings', str(amount_to_withdraw)]):
            self.atm.withdraw()
            self.assertEqual(self.atm.savings_balance, self.test_savings_balance)

    def test_calculate_monthly_interest(self):
        expected_output = "Your monthly interest is $8.33.\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.calculate_monthly_interest()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()