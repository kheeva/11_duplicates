#!/usr/bin/env python
import os
import sys


def find_files_and_dirs(scanning_dir):
    """Takes a dir and search files and directories inside it, returns
    dictionary of found files like this one: {file_path: [file_name, size]},
    and list of found sub-directories.
    """
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


def output_duplicates(found_duplicates_dict):
    for origin_file, duplicates in found_duplicates_dict.items():
        print('\nThere is the list of duplicates of the file {}:'
              .format(origin_file))
        for duplicate in duplicates:
            print(duplicate)


def main():
    scanned_files_dict = {}
    found_duplicates_dict = {}

    if len(sys.argv) != 2:
        exit("Usage: python duplicates.py path_to_scanning_dir")

    scanning_dirs = [sys.argv[1], ]
    while True:
        subdirectories = []

        if not scanning_dirs:
            break

        for directory in scanning_dirs:
            found_dirs, found_files = find_files_and_dirs(directory)
            if found_files:
                for file_path, file_attributes in found_files.items():
                    if file_attributes in scanned_files_dict.values():
                        origin_file = list(scanned_files_dict.keys())[list(
                            scanned_files_dict.values()).index(file_attributes)]
                        if found_duplicates_dict.get(origin_file) is None:
                            found_duplicates_dict[origin_file] = [file_path, ]
                        else:
                            found_duplicates_dict[origin_file].append(file_path)
                    else:
                        scanned_files_dict[file_path] = file_attributes

            if found_dirs:
                subdirectories.extend(found_dirs)

        scanning_dirs = subdirectories

    output_duplicates(found_duplicates_dict)


if __name__ == '__main__':
    main()
