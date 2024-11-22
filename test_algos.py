import unittest
import algos

class TestAlgos(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(algos.reverse_string('hello'), 'olleh')


if __name__ == 'main':
    unittest.main()