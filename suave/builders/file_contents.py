#!/usr/bin/env python

import argparse


def file_contents(file_path):
    """
    Returns the contents of the file at `file_path`.
    """
    with open(file_path, 'r') as f:
        contents = f.read()

    return contents


if __name__ == "__main__":
    # Accept the file name as the first positional argument.
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    # Print the file's contents.
    print file_contents(args.file)
