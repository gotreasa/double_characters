import pytest
from modules import double_characters


def describe_double_char():
    def should_error_when_not_a_string():
        """🧪 should give an error message when the input is not a string"""
        with pytest.raises(ValueError, match="❗️ Input should be a string"):
            double_characters.double_chars(72)

    def should_double_a_single_lowercase_letter():
        """🧪 should give 'aa' for the input 'a'"""
        assert double_characters.double_chars("a") == "aa"

    def should_double_a_single_uppercase_letter():
        """🧪 should give 'AA' for the input 'A'"""
        assert double_characters.double_chars("A") == "AA"

    def should_double_the_letters_for_one_word():
        """🧪 should give 'SSttrriinngg' for the input 'String'"""
        assert double_characters.double_chars("String") == "SSttrriinngg"
        assert double_characters.double_chars("A") == "AA"

    def should_double_the_letters_for_two_words():
        """🧪 should give 'HHeelloo WWoorrlldd' for the input 'Hello World'"""
        assert double_characters.double_chars("Hello World") == "HHeelllloo  WWoorrlldd"
        assert double_characters.double_chars("A") == "AA"

    def should_double_the_letters_for_text_with_a_space_at_the_end():
        """🧪 should give '11223344!!__  ' for the input '1234!_ '"""
        assert double_characters.double_chars("1234!_ ") == "11223344!!__  "
