# main.py
# Menu-driven program. Run it with:  python src/main.py
# Workflow: show menu -> take choice -> call the module -> show result -> repeat.

from encoder import encode
from decoder import decode
from morse_signal import show_signal
from logger import add_entry, show_log, count_status


def show_menu():
    print()
    print("========== Morse Code Converter ==========")
    print("1. Text  -> Morse code")
    print("2. Morse code -> Text")
    print("3. Show Morse signal pattern")
    print("4. View session log")
    print("5. Exit")


def do_encode():
    text = input("Type your text: ")
    ok, result = encode(text)
    if ok:
        print("Morse code:", result)
        add_entry("ENCODE", "OK", text)
    else:
        print("Error:", result)
        add_entry("ENCODE", "ERROR", result)


def do_decode():
    morse = input("Enter Morse code (use / between words): ")
    ok, result = decode(morse)
    if ok:
        print("Text:", result)
        add_entry("DECODE", "OK", morse)
    else:
        print("Error:", result)
        add_entry("DECODE", "ERROR", result)


def do_signal():
    text = input("Type your text: ")
    ok, morse = encode(text)
    if not ok:
        print("Error:", morse)
        add_entry("SIGNAL", "ERROR", morse)
        return
    ok, result = show_signal(morse)
    if ok:
        picture, on_units, total_units = result
        print("Morse code:", morse)
        print("Signal (# = ON, _ = OFF):")
        print(picture)
        print("ON units:", on_units, "| Total units:", total_units)
        add_entry("SIGNAL", "OK", text)
    else:
        print("Error:", result)
        add_entry("SIGNAL", "ERROR", result)


def main():
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            do_encode()
        elif choice == "2":
            do_decode()
        elif choice == "3":
            do_signal()
        elif choice == "4":
            show_log()
            print("Successful:", count_status("OK"), "| Errors:", count_status("ERROR"))
        elif choice == "5":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
