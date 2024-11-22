import unittest
import algos

class TestAlgos(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(algos.reverse_string('hello'), 'olleh')

    def test_alterate_cases(self):
        self.assertEqual(algos.alternate_cases('hello'), 'hElLo')
        self.assertEqual(algos.alternate_cases('sUPERcaliFrag'), 'sUpErCaLiFrAg')

if __name__ == 'main':
    unittest.main()