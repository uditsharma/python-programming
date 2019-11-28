"""
This is a journal Module
"""
import os


def load(name):
    """
    This method load and create the new journal.
    :param name: This is the base name of Journal.
    :return: return the Journal Data Structure loaded data from file.

    """
    path = get_full_path(name)
    journal_data = [];
    print("Loading from {}".format(path))
    if os.path.exists(path):
        with open(path, 'r') as fin:
            for entry in fin.readlines():
                journal_data.append(entry.rstrip())
    return journal_data


def save(name, journal):
    path = get_full_path(name)
    print("Saving to {}".format(path))
    with open(path, 'w') as fout:
        for entry in journal:
            fout.write(entry + "\n")


def add_entry(journal, data):
    journal.append(data)


def get_full_path(name):
    file_name = os.path.abspath(os.path.join('.', 'journals', name))
    return file_name
