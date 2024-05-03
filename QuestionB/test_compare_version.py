import unittest
from compare_versions import compare_versions

class TestVersionComparison(unittest.TestCase):
    def test_equal_versions(self):
        self.assertEqual(compare_versions("1.0", "1.0"), 0)
        self.assertEqual(compare_versions("1", "1"), 0)
        self.assertEqual(compare_versions("2.1", "2.1"), 0)
        self.assertEqual(compare_versions("3.0.0", "3.0.0"), 0)

    def test_greater_versions(self):
        self.assertEqual(compare_versions("1.2", "1.1"), 1)
        self.assertEqual(compare_versions("3", "1"), 1)
        self.assertEqual(compare_versions("2.0", "1.9"), 1)
        self.assertEqual(compare_versions("3.5.2", "3.5.1"), 1)

    def test_lesser_versions(self):
        self.assertEqual(compare_versions("1.1", "1.2"), -1)
        self.assertEqual(compare_versions("1", "2"), -1)
        self.assertEqual(compare_versions("1.9", "2.0"), -1)
        self.assertEqual(compare_versions("3.5.1", "3.5.2"), -1)

    def test_complex_versions(self):
        self.assertEqual(compare_versions("1.10", "1.2"), 1)
        self.assertEqual(compare_versions("2.1", "2.1.0"), 0)
        self.assertEqual(compare_versions("3.0.1", "3.0"), 1)
    
    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            compare_versions(1, "1")
        with self.assertRaises(TypeError):
            compare_versions("1", 1)
        with self.assertRaises(TypeError):
            compare_versions(2.0, "2.0")
        with self.assertRaises(TypeError):
            compare_versions("2.0", 2.0)
        with self.assertRaises(TypeError):
            compare_versions([], "1.0")
        with self.assertRaises(TypeError):
            compare_versions("1.0", {})
        with self.assertRaises(TypeError):
            compare_versions(None, "1.0")
        with self.assertRaises(TypeError):
            compare_versions("1.0", True)
    
    def test_invalid_version_format(self):
        # Test with version string missing version number
        with self.assertRaises(ValueError):
            compare_versions("1..0", "1.0")
        with self.assertRaises(ValueError):
            compare_versions("2.0", "2..1")
        with self.assertRaises(ValueError):
            compare_versions("3.0.1", "3.")

if __name__ == '__main__':
    unittest.main()
