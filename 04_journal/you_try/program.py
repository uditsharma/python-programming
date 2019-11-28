import journal


def print_header():
    print('------------------------')
    print('    JOURNAL APP')
    print('------------------------')


def list_entries(journal):
    print("Your Journal Entries")
    for idx, entry in enumerate(journal):
        print("* [{}] {}".format(idx + 1, entry))


def add_entries(journal_data):
    print("Enter your Entry, Press <Enter> to exit")
    entry = input()
    journal_data.append(entry)


def run_event_loop():
    print("What do you want to do with your Journal app")
    cmd = "EMPTY"
    journal_name = 'placeholder.txt'
    journal_data = journal.load(journal_name)
    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("We do not understand {}".format(cmd))
    journal.save(journal_name, journal_data)
    print("Good bye !!")


def main():
    print_header()
    run_event_loop()


if __name__ == "__main__":
    main()
