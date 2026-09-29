# test_decoder.py - run from the project folder:  python tests/test_decoder.py
import sys
sys.path.insert(0, "src")

from decoder import decode
from encoder import encode


def test_basic():
    assert decode("... --- ...") == (True, "SOS")


def test_words_with_slash():
    assert decode(".... .. / - .... . .-. .") == (True, "HI THERE")


def test_words_with_three_spaces():
    assert decode(".-   -...") == (True, "A B")


def test_round_trip():
    ok, morse = encode("Hello World 2026")
    assert decode(morse) == (True, "HELLO WORLD 2026")


def test_unknown_sequence():
    assert decode("......-.-.")[0] == False


def test_wrong_characters():
    assert decode("abc")[0] == False


def test_empty_input():
    assert decode("")[0] == False


tests = [test_basic, test_words_with_slash, test_words_with_three_spaces,
         test_round_trip, test_unknown_sequence, test_wrong_characters,
         test_empty_input]
for t in tests:
    t()
    print("PASS:", t.__name__)
print("All", len(tests), "decoder tests passed.")
