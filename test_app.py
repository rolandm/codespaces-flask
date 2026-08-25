import unittest

from app import app


class DefaultUrlTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_default_url_is_served(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Moi</title>", response.data)

    def test_owl_url_uses_owl_image(self):
        response = self.client.get("/owl")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"owl.svg", response.data)


if __name__ == "__main__":
    unittest.main()