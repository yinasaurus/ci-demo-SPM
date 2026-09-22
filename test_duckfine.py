import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_initializes_member_id(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.member_id, "member-123")

    def test_initializes_total_owed_to_zero(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.total_owed, 0.0)

    def test_grace_period_charges_no_fee(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(2), 0.0)

    def test_standard_charge_uses_chargeable_days(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(5), 1.50)

    def test_deluxe_charge_doubles_the_fee(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(5, deluxe=True), 3.00)

    def test_single_charge_does_not_exceed_maximum(self):
        fine = DuckFine("member-123")

        self.assertEqual(fine.charge(20), 5.00)

    def test_charges_accumulate_in_total_owed(self):
        fine = DuckFine("member-123")

        fine.charge(3)
        fine.charge(4)

        self.assertEqual(fine.total_owed, 1.50)

    def test_negative_days_late_raise_value_error(self):
        fine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            fine.charge(-1)


if __name__ == "__main__":
    unittest.main()
