import unittest
import add


class TestAddCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event = {"pathParameters": {"x": "900", "y": "99"}}
        result = add.handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('999', result['body'])


if __name__ == '__main__':
    unittest.main()
