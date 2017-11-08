#!/usr/bin/env python
import os
import sys


scanned_files = {}


def has_duplicate(name, size):
    if [name, size] in scanned_files.values():
        return True
    return False


def seek_duplicates_in_dir(scanning_dir):
    list_of_dirs = []
    with os.scandir(scanning_dir) as file_or_dir:
        for entry in file_or_dir:
            if not entry.name.startswith('.') and entry.is_file():
                if has_duplicate(entry.name, entry.stat().st_size):
                    print('Found the duplicate: ', entry.path)
                else:
                    scanned_files[entry.path] = [entry.name, entry.stat().st_size]
            elif not entry.name.startswith('.') and entry.is_dir():
                list_of_dirs.append(entry.path)
    return list_of_dirs


def main():
    if len(sys.argv) != 2:
        print("Usage: python duplicates.py path_to_scanning_dir.")
    else:
        scanning_dir = [sys.argv[1],]
        while True:
            new_dirs = []
            if not scanning_dir:
                break
            for directory in scanning_dir:
                new_dir = seek_duplicates_in_dir(directory)
                if new_dir:
                    new_dirs.extend(new_dir)
            scanning_dir = new_dirs


if __name__ == '__main__':
    main()
