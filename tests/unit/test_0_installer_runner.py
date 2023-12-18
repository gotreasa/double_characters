import pytest
from modules import double_characters


def describe_double_char():
    def should_error_when_not_a_string():
        """🧪 should give an error message when the input is not a string"""
        with pytest.raises(ValueError, match="❗️ Input should be a string"):
            double_characters.double_chars(72)
