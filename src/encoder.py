# encoder.py
# Module 1: converts text to Morse code.
# Algorithm: look up every character in the dictionary (Unit 3: Iteration).

from morse_map import morse_code, word_separator
from validator import check_text


def encode(text):
    """Convert text to Morse code. Returns (True, morse) or (False, error)."""
    valid, message = check_text(text)          # tuple assignment (Unit 2)
    if not valid:
        return (False, message)

    result = ""
    words = text.lower().split()
    for w in range(len(words)):
        if w > 0:
            result = result + " " + word_separator + " "
        first = True
        for ch in words[w]:
            if first:
                result = result + morse_code[ch]
                first = False
            else:
                result = result + " " + morse_code[ch]
    return (True, result)
