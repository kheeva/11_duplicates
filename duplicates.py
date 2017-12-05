#!/usr/bin/env python
import os
import sys


def find_files_and_dirs(scanning_dir, files_dictionary):
    """Takes a dir and search files and directories inside it, returns
    dictionary of found files like this one: {(file_name, size):[file_path1,
    file_path2]}, and list of found sub-directories.
    """
    found_dirs_list = []
    with os.scandir(scanning_dir) as file_or_dir:
        for entry in file_or_dir:
            if not entry.name.startswith('.') and entry.is_file():
                file_attributes = (entry.name, entry.stat().st_size)
                if file_attributes not in files_dictionary.keys():
                    files_dictionary[file_attributes] = [entry.path]
                else:
                    files_dictionary[file_attributes].append(entry.path)
            elif not entry.name.startswith('.') and entry.is_dir():
                found_dirs_list.append(entry.path)
    return found_dirs_list, files_dictionary


def output_duplicates(found_files):
    groups_of_duplicates = filter(lambda x: len(x) > 1, found_files.values())
    print('\nThere is the list of found duplicates:')
    for duplicates_group in groups_of_duplicates:
        print('\r')
        for duplicate in duplicates_group:
            print(duplicate)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit("Usage: python duplicates.py path_to_scanning_dir")

    files_dict = {}
    scanning_dirs = [sys.argv[1]]
    while scanning_dirs:
        subdirectories = []
        for directory in scanning_dirs:
            found_dirs, files_dict = find_files_and_dirs(directory, files_dict)
            if found_dirs:
                subdirectories.extend(found_dirs)

        scanning_dirs = subdirectories

    output_duplicates(files_dict)
