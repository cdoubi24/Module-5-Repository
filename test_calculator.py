
import unittest
from calculator import add  # Import the function to test

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 2 + 3 should be 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 should be 0
        self.assertEqual(add(0, 0), 0)  # 0 + 0 should be 0

if __name__ == "__main__":
    unittest.main()
