# test_validator.py - run from the project folder:  python tests/test_validator.py
# Also tests the signal module.
import sys
sys.path.insert(0, "src")

from validator import find_unsupported, check_text, check_morse
from morse_signal import build_units, draw_signal, total_duration, show_signal


def test_find_unsupported():
    assert find_unsupported("a#b$#") == ["#", "$"]


def test_check_text_valid():
    assert check_text("hello 1") == (True, "")


def test_check_text_empty():
    assert check_text("")[0] == False


def test_check_morse_valid():
    assert check_morse(".- / -...") == (True, "")


def test_check_morse_invalid_symbol():
    assert check_morse("a.-")[0] == False


def test_units_for_letter_a():
    # A = .-  ->  dot(1) gap(0) dash(1 1 1)
    assert build_units(".-") == [1, 0, 1, 1, 1]


def test_word_gap_is_seven_units():
    assert build_units(". / .") == [1] + [0] * 7 + [1]


def test_draw_signal():
    assert draw_signal([1, 0, 1, 1, 1]) == "#_###"


def test_total_duration():
    assert total_duration(build_units("... --- ...")) == 27


def test_show_signal():
    ok, result = show_signal(".-")
    assert ok == True
    assert result == ("#_###", 4, 5)


tests = [test_find_unsupported, test_check_text_valid, test_check_text_empty,
         test_check_morse_valid, test_check_morse_invalid_symbol,
         test_units_for_letter_a, test_word_gap_is_seven_units,
         test_draw_signal, test_total_duration, test_show_signal]
for t in tests:
    t()
    print("PASS:", t.__name__)
print("All", len(tests), "validator and signal tests passed.")
