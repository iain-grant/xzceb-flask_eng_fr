"""Function to test translator"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Class TestTranslator"""
    def test_english_to_french(self):
        """Test English to French translations"""
        self.assertNotEqual(english_to_french('None'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        """Test French to English translations"""
        self.assertNotEqual(french_to_english('None'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
