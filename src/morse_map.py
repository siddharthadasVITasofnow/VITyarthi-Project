# morse_map.py
morse_code = {
    "a": ".-",   "b": "-...", "c": "-.-.", "d": "-..",  "e": ".",
    "f": "..-.", "g": "--.",  "h": "....", "i": "..",   "j": ".---",
    "k": "-.-",  "l": ".-..", "m": "--",   "n": "-.",   "o": "---",
    "p": ".--.", "q": "--.-", "r": ".-.",  "s": "...",  "t": "-",
    "u": "..-",  "v": "...-", "w": ".--",  "x": "-..-", "y": "-.--",
    "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}
# Word separator used in the Morse output
word_separator = "/"

# Reverse dictionary: ".-" -> "a"
reverse_morse_code = {}
for letter in morse_code:
    reverse_morse_code[morse_code[letter]] = letter
