# decoder.py
# Module 2: converts Morse code to text.
# Algorithm: look up every Morse symbol in the reverse dictionary.

from morse_map import reverse_morse_code, word_separator
from validator import check_morse


def decode(morse):
    """Convert Morse code to text. Returns (True, text) or (False, error)."""
    valid, message = check_morse(morse)
    if not valid:
        return (False, message)

    # three spaces also mean a gap between words
    morse = morse.strip().replace("   ", " " + word_separator + " ")

    result = ""
    for word in morse.split(word_separator):
        symbols = word.split()
        if len(symbols) > 0:
            if result != "":
                result = result + " "
            for symbol in symbols:
                result = result + reverse_morse_code[symbol]
    return (True, result.upper())
