# morse_signal.py
# Module 3: shows the Morse signal as a pattern of ON/OFF time units.
# Standard Morse timing (links the project to communication systems):
#   dot = 1 unit ON,  dash = 3 units ON,  gap inside a letter = 1 unit OFF,
#   gap between letters = 3 units OFF,   gap between words = 7 units OFF.

from morse_map import word_separator
from validator import check_morse
def build_units(morse):
    """Convert Morse code to a list of 1 (ON) and 0 (OFF) units."""
    units = []
    words = morse.strip().split(word_separator)
    first_word = True
    for word in words:
        letters = word.split()
        if len(letters) == 0:
            continue
        if not first_word:
            units = units + [0] * 7            # word gap
        first_word = False
        first_letter = True
        for letter in letters:
            if not first_letter:
                units = units + [0] * 3        # letter gap
            first_letter = False
            first_symbol = True
            for symbol in letter:
                if not first_symbol:
                    units.append(0)            # gap inside a letter
                first_symbol = False
                if symbol == ".":
                    units = units + [1]
                else:
                    units = units + [1, 1, 1]
    return units
def draw_signal(units):
    """Turn the units list into a picture: # = ON, _ = OFF."""
    line = ""
    for u in units:
        if u == 1:
            line = line + "#"
        else:
            line = line + "_"
    return line
def total_duration(units):
    """Add up all the units (Summation)."""
    total = 0
    for u in units:
        total = total + 1
    return total
def show_signal(morse):
    """Returns (True, (picture, on_units, total_units)) or (False, error)."""
    valid, message = check_morse(morse)
    if not valid:
        return (False, message)
    units = build_units(morse)
    on_units = 0
    for u in units:
        if u == 1:
            on_units = on_units + 1
    return (True, (draw_signal(units), on_units, total_duration(units)))
