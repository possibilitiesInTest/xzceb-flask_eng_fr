"""
   Unit Tests for null and hello
"""
import unittest
import sys
import os
from translator import english_to_french, french_to_english
# sys.path.append('../machinetranslation') # setting path
# parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# sys.path.append(parent_directory)
# parent_directory = Path(__file__).resolve().parent.parent.parent
# directory = Path(__file__).resolve().parent.parent
# sys.path.append(directory)
# parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# sys.path.append(parent_directory)

class TestEnglishToFrench(unittest.TestCase):
    """
        This returns translations in French!
    """
    def test_english_to_french_translation(self):
        """
        This returns translations in French!
        """
        english_string = "Hello"
        english_to_french_translation = english_to_french(english_string)
        self.assertEqual(english_to_french(""), "") # Tests null
        self.assertEqual(english_to_french_translation, "Bonjour") # Tests translation

class TestFrenchToEnglish(unittest.TestCase):
    """
    This returns translations in Englich!
    """
    def test_french_to_english_translation(self):
        """
        This returns translations in Englich!
        """
        french_string = "Bonjour"
        french_to_english_translation = french_to_english(french_string)
        self.assertEqual(french_to_english(""), "") # Tests null
        self.assertEqual(french_to_english_translation, "Hello") # Tests translation

if __name__ == '__main__':
    unittest.main()
