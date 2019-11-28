import os
import platform
import subprocess

import cat_service


def print_header():
    print("--------------------------------")
    print("         LOL CAT FACTORY")
    print("--------------------------------")


def get_or_create_folder():
    abspath = os.path.abspath(os.path.dirname(__file__))
    folder_name = "cat_pictures"
    full_path = os.path.join(abspath, folder_name)

    if not os.path.exists(full_path) and not os.path.isdir(full_path):
        print("Creating the folder  + " + full_path)
        os.mkdir(full_path)
    return full_path


def downloads_cats(folder):
    cat_count = 1
    for i in range(cat_count):
        cat_name = "lol_cat.{}".format(i)
        print("Downloading cat " + cat_name)
        cat_service.get_cat(folder, cat_name)


def display_cats(folder):
    if platform.system() == "Darwin":
        subprocess.call(["open", folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


def main():
    print_header()
    folder = get_or_create_folder()
    downloads_cats(folder)
    display_cats(folder)


if __name__ == '__main__':
    main()
