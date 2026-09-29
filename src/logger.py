# logger.py
# Keeps a record of what the user did in this session.
# Each record is a tuple stored in a list (Unit 5: Lists, Tuples).

session_log = []


def add_entry(action, status, detail):
    """Add one record: (action, status, detail)."""
    session_log.append((len(session_log) + 1, action, status, detail))


def show_log():
    """Print all records of the current session."""
    if len(session_log) == 0:
        print("Log is empty.")
        return
    for entry in session_log:
        number, action, status, detail = entry
        print(str(number) + ". " + action + " | " + status + " | " + detail)


def count_status(status):
    """Count how many records have the given status (Counting)."""
    count = 0
    for entry in session_log:
        if entry[2] == status:
            count = count + 1
    return count
