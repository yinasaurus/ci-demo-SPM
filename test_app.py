import unittest

from app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_returns_ok(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_fine_returns_fee_as_json(self):
        response = self.client.get("/fine?days=5")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"fee": 1.5})

    def test_deluxe_flag_reaches_fee_calculation(self):
        response = self.client.get("/fine?days=5&deluxe=1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"fee": 3.0})

    def test_non_numeric_days_returns_bad_request(self):
        response = self.client.get("/fine?days=abc")

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_negative_days_returns_bad_request(self):
        response = self.client.get("/fine?days=-1")

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()