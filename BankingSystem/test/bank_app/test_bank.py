import unittest
from src.bank_app.bank import Bank



class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("United Bank")
        self.bank.create_account("Alice Sender", 30, "09071151567", 1234)
        self.bank.create_account("Bob Receiver", 28, "09078951567", 4321)


    def test_deposit_increases_balance(self):
        self.assertEqual(0, self.bank.check_balance("9071151567", 1234))
        self.bank.deposit("9071151567", 5000)
        self.assertEqual(5000, self.bank.check_balance("9071151567", 1234))

    def test_deposit_negative_does_not_change_balance(self):
        self.bank.deposit("9071151567", 3000)
        self.assertEqual(3000, self.bank.check_balance("9071151567", 1234))
        self.bank.deposit("9071151567", -1000)
        self.assertEqual(3000, self.bank.check_balance("9071151567", 1234))


    def test_withdraw_valid_amount(self):
        self.bank.deposit("9071151567", 5000)
        self.bank.withdraw("9071151567", 2000, 1234)
        self.assertEqual(3000, self.bank.check_balance("9071151567", 1234))

    def test_withdraw_more_than_balance_raises_exception(self):
        self.bank.deposit("9071151567", 1000)
        with self.assertRaises(ValueError):
            self.bank.withdraw("9071151567", 2000, 1234)
        self.assertEqual(1000, self.bank.check_balance("9071151567", 1234))

    def test_withdraw_wrong_pin_raises_exception(self):
        self.bank.deposit("9071151567", 2000)
        with self.assertRaises(ValueError):
            self.bank.withdraw("9071151567", 500, 9999)
        self.assertEqual(2000, self.bank.check_balance("9071151567", 1234))


    def test_transfer_reduces_sender_and_increases_receiver(self):
        self.bank.deposit("9071151567", 5000)
        self.bank.transfer("9071151567", 1234, "9078951567", 2000)
        self.assertEqual(3000, self.bank.check_balance("9071151567", 1234))
        self.assertEqual(2000, self.bank.check_balance("9078951567", 4321))

    def test_transfer_with_wrong_pin_raises_exception(self):
        self.bank.deposit("9071151567", 5000)
        with self.assertRaises(ValueError):
            self.bank.transfer("9071151567", 9999, "9078951567", 1000)
        self.assertEqual(5000, self.bank.check_balance("9071151567", 1234))
        self.assertEqual(0, self.bank.check_balance("9078951567", 4321))

    def test_transfer_insufficient_balance_raises_exception(self):
        self.bank.deposit("9071151567", 1000)
        with self.assertRaises(ValueError):
            self.bank.transfer("9071151567", 1234, "9078951567", 2000)
        self.assertEqual(1000, self.bank.check_balance("9071151567", 1234))
        self.assertEqual(0, self.bank.check_balance("9078951567", 4321))

    def test_transfer_to_nonexistent_account_raises_exception(self):
        self.bank.deposit("9071151567", 1000)
        with self.assertRaises(ValueError):
            self.bank.transfer("9071151567", 1234, "0000000000", 500)
        self.assertEqual(1000, self.bank.check_balance("9071151567", 1234))


    def test_delete_account_removes_account(self):
        self.assertEqual(2, self.bank.get_no_of_number_acc())
        self.bank.delete_account("9078951567")
        with self.assertRaises(ValueError):
            self.bank.check_balance("9078951567", 4321)
        self.assertEqual(1, self.bank.get_no_of_number_acc())

    def test_delete_nonexistent_account_does_not_change_count(self):
        self.assertEqual(2, self.bank.get_no_of_number_acc())
        self.bank.delete_account("0000000000")
        self.assertEqual(2, self.bank.get_no_of_number_acc())


if __name__ == "__main__":
    unittest.main()