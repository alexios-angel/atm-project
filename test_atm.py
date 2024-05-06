import io
import unittest.mock
from atm import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM(1000, 2000, 0.05)

    def test_display_balance(self):
        expected_output = "Checking Balance: $1000.00\nSavings Balance: $2000.00\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.display_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_check_balance_checking(self):
        expected_output = "Checking Balance: $1000.00\n"
        with unittest.mock.patch('builtins.input', side_effect=['c']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.check_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_check_balance_savings(self):
        expected_output = "Savings Balance: $2000.00\nYour monthly interest is $8.33.\n"
        with unittest.mock.patch('builtins.input', side_effect=['s', 'y']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.check_balance()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_deposit_checking(self):
        with unittest.mock.patch('builtins.input', side_effect=['checking', '500']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.deposit()
            self.assertEqual(self.atm.checking_balance, 1500)

    def test_deposit_savings(self):
        with unittest.mock.patch('builtins.input', side_effect=['savings', '1000']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.deposit()
            self.assertEqual(self.atm.savings_balance, 3000)

    def test_withdraw_checking_sufficient(self):
        with unittest.mock.patch('builtins.input', side_effect=['checking', '500']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.withdraw()
            self.assertEqual(self.atm.checking_balance, 500)

    def test_withdraw_checking_insufficient(self):
        with unittest.mock.patch('builtins.input', side_effect=['checking', '1500']):
            self.atm.withdraw()
            self.assertEqual(self.atm.checking_balance, 1000)

    def test_withdraw_savings_sufficient(self):
        with unittest.mock.patch('builtins.input', side_effect=['savings', '1000']), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.withdraw()
            self.assertEqual(self.atm.savings_balance, 1000)

    def test_withdraw_savings_insufficient(self):
        with unittest.mock.patch('builtins.input', side_effect=['savings', '3000']):
            self.atm.withdraw()
            self.assertEqual(self.atm.savings_balance, 2000)

    def test_calculate_monthly_interest(self):
        expected_output = "Your monthly interest is $8.33.\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.atm.calculate_monthly_interest()
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()