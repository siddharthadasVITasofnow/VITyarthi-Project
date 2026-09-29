# test_encoder.py - run from the project folder:  python tests/test_encoder.py
import sys
sys.path.insert(0, "src")

from encoder import encode


def test_letters():
    assert encode("sos") == (True, "... --- ...")


def test_uppercase_same_as_lowercase():
    assert encode("HeLLo") == encode("hello")


def test_numbers_and_words():
    assert encode("Hello 123") == (True, ".... . .-.. .-.. --- / .---- ..--- ...--")


def test_extra_spaces():
    assert encode("  a   b ") == (True, ".- / -...")


def test_unsupported_character():
    ok, message = encode("hi #")
    assert ok == False
    assert "#" in message


def test_empty_input():
    assert encode("   ")[0] == False


tests = [test_letters, test_uppercase_same_as_lowercase, test_numbers_and_words,
         test_extra_spaces, test_unsupported_character, test_empty_input]
for t in tests:
    t()
    print("PASS:", t.__name__)
print("All", len(tests), "encoder tests passed.")
