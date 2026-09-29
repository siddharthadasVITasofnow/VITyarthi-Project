# validator.py
# Input checks and error messages (Unit 3: Conditionals, Unit 5: Sets, Tuples).
# Every check returns a tuple (is_valid, message).

from morse_map import morse_code, reverse_morse_code
def find_unsupported(text):
    """Return a sorted list of characters that have no Morse code."""
    bad = set()                      # a set stores each bad character only once
    for ch in text.lower():
        if ch != " " and ch not in morse_code:
            bad.add(ch)
    return sorted(bad)
def check_text(text):
    """Check the text entered for encoding."""
    if text.strip() == "":
        return (False, "Input is empty. Please type some text.")
    bad = find_unsupported(text)
    if len(bad) > 0:
        return (False, "Unsupported character(s): " + " ".join(bad))
    return (True, "")
def check_morse(morse):
    """Check the Morse code entered for decoding."""
    if morse.strip() == "":
        return (False, "Input is empty. Please enter Morse code.")
    for ch in morse:
        if ch != "." and ch != "-" and ch != " " and ch != "/":
            return (False, "Morse code can only contain '.', '-', spaces and '/'.")
    for token in morse.replace("/", " ").split():
        if token not in reverse_morse_code:
            return (False, "Unknown Morse sequence: " + token)
    return (True, "")
