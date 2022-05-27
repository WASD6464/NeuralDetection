import unittest
from flask import Flask
app = Flask(__name__)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)
    def test_something(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 404)
    def test_something(self):
        tester = app.test_client(self)
        response = tester.get('/track', content_type='html/text')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
