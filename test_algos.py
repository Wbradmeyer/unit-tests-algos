import unittest
import algos

class TestAlgos(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(algos.reverse_string('hello'), 'olleh')

    def test_alterate_cases(self):
        self.assertEqual(algos.alternate_cases('hello'), 'hElLo')
        self.assertEqual(algos.alternate_cases('sUPERcaliFrag'), 'sUpErCaLiFrAg')

    def test_starts_with_a_vowel(self):
        self.assertFalse(algos.starts_with_a_vowel('beaver'))
        self.assertTrue(algos.starts_with_a_vowel('otter'))
        self.assertTrue(algos.starts_with_a_vowel('emu'))

if __name__ == 'main':
    unittest.main()