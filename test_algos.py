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
    
    def test_add_alternating_indices(self):
        self.assertEqual(algos.add_alternating_indices([1,2,3,4,5,6,7,8], 1), 20)
        self.assertEqual(algos.add_alternating_indices([1,2,3,4,5,6,7,8], 0), 16)
        self.assertFalse(algos.add_alternating_indices([1,2,3,4,5,6,7,8], 8))
        self.assertFalse(algos.add_alternating_indices([1,2,3,4,5,6,7,8], -2))
        self.assertFalse(algos.add_alternating_indices([1,2,3,4,5,6,7,8], "five"))

# if __name__ == 'main':
if __name__ == '__main__':
    unittest.main()