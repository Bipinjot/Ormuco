import unittest
from overlap import check_overlap

class TestOverlap(unittest.TestCase):
    def test_overlap(self):
        # Test cases where line segments overlap
        self.assertTrue(check_overlap(1, 5, 3, 7))
        self.assertTrue(check_overlap(-2, 2, -1, 3))
        self.assertTrue(check_overlap(0, 10, 5, 15))
        self.assertTrue(check_overlap(-10, 0, -5, 5))

    def test_no_overlap(self):
        # Test cases where line segments do not overlap
        self.assertFalse(check_overlap(1, 5, 6, 10))
        self.assertFalse(check_overlap(-2, 2, 3, 7))
        self.assertFalse(check_overlap(0, 10, 15, 20))
        self.assertFalse(check_overlap(-10, 0, 10, 20))

    def test_touching_segments(self):
        # Test cases where line segments touch but do not overlap
        self.assertFalse(check_overlap(1, 5, 5, 10))
        self.assertFalse(check_overlap(-2, 2, 2, 6))
        self.assertFalse(check_overlap(0, 10, 10, 20))
        self.assertFalse(check_overlap(-10, 0, 0, 10))

    def test_negative_coordinates(self):
        # Test cases with negative coordinates
        self.assertTrue(check_overlap(-5, 5, -3, 3))
        self.assertFalse(check_overlap(-10, -5, -4, 0))
        self.assertTrue(check_overlap(-8, -3, -12, -7))

    def test_large_coordinates(self):
        # Test cases with large coordinates
        self.assertTrue(check_overlap(1000, 2000, 1500, 2500))
        self.assertFalse(check_overlap(500, 1000, 2000, 3000))
        self.assertTrue(check_overlap(50000, 60000, 55000, 65000))

    def test_same_segments(self):
        # Test cases where both line segments are the same
        self.assertTrue(check_overlap(1, 5, 1, 5))
        self.assertTrue(check_overlap(-2, 2, -2, 2))
        self.assertTrue(check_overlap(0, 10, 0, 10))
        self.assertTrue(check_overlap(-10, 0, -10, 0))

    def test_invalid_input(self):
        # Test cases with invalid input (non-numeric)
        with self.assertRaises(ValueError):
            check_overlap('a', 5, 3, 7)
        with self.assertRaises(ValueError):
            check_overlap(1, 'b', 3, 7)
        with self.assertRaises(ValueError):
            check_overlap(1, 5, 'c', 7)
        with self.assertRaises(ValueError):
            check_overlap(1, 5, 3, 'd')

if __name__ == '__main__':
    unittest.main()
