import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(5, 7), 12)
        self.assertEqual(add_numbers(10, 20), 30)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -5), -8)
        self.assertEqual(add_numbers(-10, -20), -30)

    def test_add_decimal_numbers(self):
        self.assertAlmostEqual(add_numbers(3.14, 1.59), 4.73, places=2)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=1)
        
    def test_add_large_numbers(self):
        self.assertEqual(add_numbers(1000000000, 2000000000), 3000000000)
        self.assertEqual(add_numbers(-999999999, -999999998), -1999999997)

if __name__ == '__main__':
    unittest.main()
