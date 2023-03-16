import unittest

def divide(x, y):
    return x / y

class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(14, 2), 8)

if __name__ == '__main__':
    unittest.main()
