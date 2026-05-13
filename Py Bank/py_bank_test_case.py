import unittest

from py_bank import (
    validate_email,
    calculate_balance,
    is_strong_password,
    apply_intrest,
    get_transaction_summary
)


class TestFunctions(unittest.TestCase):

#validate email

    def test_valid_email(self):
        self.assertTrue(validate_email("testing123@gmail.com"))

    def test_email_without_at_symbol(self):
        self.assertFalse(validate_email("testing123gmail.com"))

    def test_email_ending_with_at(self):
        self.assertFalse(validate_email("123456789@"))

    def test_short_email(self):
        self.assertFalse(validate_email("a@b.c"))

    def test_email_starting_with_at(self):
          self.assertFalse(
          validate_email("@testing123")
     )
# calculate balance 

    def test_calculate_balance_positive_and_negative(self):
        self.assertEqual(calculate_balance([5, -10]), -5)

    def test_calculate_balance_empty_list(self):
        self.assertEqual(calculate_balance([]), 0)

    def test_calculate_balance_positive_values(self):
        self.assertEqual(calculate_balance([100, 200, 300]), 600)

    def test_calculate_balance_zero_values(self):
        self.assertEqual(
            calculate_balance([0, 0, 0]),
            0
        )
# is strong password

    def test_vali_password(self):
       self.assertTrue(
            is_strong_password("12345678")
        )

    def test_short_password(self):
        self.assertFalse(
            is_strong_password("1234")
        )

    def test_exactly_eight_characters(self):
        self.assertTrue(
            is_strong_password("abcdefgh")
        )

    def test_long_password(self):
        self.assertTrue(
            is_strong_password("verystrongpassword")
        )

    def test_empty_password(self):
        self.assertFalse(
            is_strong_password("")
        )

# apply interest

    def test_apply_interest_valid(self):
        self.assertEqual(apply_intrest(1000, 0.05, 2), 1102.5)

    def test_apply_interest_invalid_rate(self):
        with self.assertRaises(ValueError):
            apply_intrest(1000, -0.05, 2)

    def test_apply_interest_invalid_years(self):
        with self.assertRaises(ValueError):
            apply_intrest(1000, 0.05, 0)


# get transaction summary
    def test_transaction_summary(self):

        transactions = [
            ["credit", 2000],
            ["debit", 500],
            ["credit", 300]
        ]

        expected = {
            "total_credits": 2300,
            "total_debit": 500,
            "net_balance": 1800,
            "transaction_count": 3
        }

        self.assertEqual(
            get_transaction_summary(transactions),
            expected
        )



if __name__ == "__main__":
    unittest.main()
