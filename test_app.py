import unittest
from flask import session
from app import app

class FlaskTestCase(unittest.TestCase):
    # Setting up the test client for Flask
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    # Test for the index page
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Test for the checkout page with products
    def test_checkout(self):
        response = self.app.post('/checkout', data=dict(product=['1', '2']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fishing Rod', response.data)
        self.assertIn(b'Fishing Net', response.data)
        self.assertNotIn(b'Fishing Bait', response.data)

    # Test for the checkout page without products
    def test_checkout_no_product(self):
        response = self.app.post('/checkout', data=dict(product=[]))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Fishing Rod', response.data)
        self.assertNotIn(b'Fishing Net', response.data)
        self.assertNotIn(b'Fishing Bait', response.data)

    # Test for the confirmation page with total price
    def test_confirmation(self):
        with self.app.session_transaction() as sess:
            sess['total_price'] = 150
        response = self.app.post('/confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'150', response.data)

    # Test for the confirmation page without total price
    def test_confirmation_no_total_price(self):
        with self.app.session_transaction() as sess:
            sess['total_price'] = None
        response = self.app.post('/confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0', response.data)

if __name__ == '__main__':
    unittest.main()