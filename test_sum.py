import unittest
from my_sum.sum_module import sum  # Import the function you're testing

class TestSumFunction(unittest.TestCase):

    def test_sum_of_list(self):
        """Test that sum() correctly adds a list of integers."""
        data = [1, 2, 3]
        self.assertEqual(sum(data), 6)

    def test_sum_of_tuple(self):
        """Test that sum() correctly adds a tuple of numbers."""
        data = (1, 2, 3)
        self.assertEqual(sum(data), 6)

    def test_sum_of_floats(self):
        """Test that sum() correctly handles floating-point numbers."""
        data = [1.5, 2.5, 3.0]
        self.assertAlmostEqual(sum(data), 7.0)

    def test_sum_with_negative_numbers(self):
        """Test that sum() correctly handles negative numbers."""
        data = [-1, -2, -3]
        self.assertEqual(sum(data), -6)

    def test_sum_with_invalid_input(self):
        """Test that sum() raises a TypeError when input is not iterable."""
        with self.assertRaises(TypeError):
            sum(123)  # Should raise an error

if __name__ == "__main__":
    unittest.main()