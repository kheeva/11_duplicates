#!/usr/bin/env python
import os
import sys


def find_files_and_dirs(scanning_dir):
    found_dirs_list = []
    found_files_dict = {}
    with os.scandir(scanning_dir) as file_or_dir:
        for entry in file_or_dir:
            if not entry.name.startswith('.') and entry.is_file():
                found_files_dict[entry.path] = [entry.name,
                                                entry.stat().st_size]
            elif not entry.name.startswith('.') and entry.is_dir():
                found_dirs_list.append(entry.path)
    return found_dirs_list, found_files_dict


def main():
    scanned_files_dict = {}
    found_duplicates = []

    if len(sys.argv) != 2:
        exit("Usage: python duplicates.py path_to_scanning_dir.")

    scanning_dir = [sys.argv[1], ]
    while True:
        subdirectories = []

        if not scanning_dir:
            break

        for directory in scanning_dir:
            found_dirs, found_files = find_files_and_dirs(directory)
            if found_files:
                for file_path, file_attributes in found_files.items():
                    if file_attributes in scanned_files_dict.values():
                        found_duplicates.append(file_path)
                    else:
                        scanned_files_dict[file_path] = file_attributes

            if found_dirs:
                subdirectories.extend(found_dirs)

        scanning_dir = subdirectories

    for duplicate in found_duplicates:
        print('Found a duplicate {}!\n'.format(duplicate))


if __name__ == '__main__':
    main()
