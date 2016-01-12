#!/usr/bin/env python

import argparse
import random
import yaml


def random_line(file_path):
    """
    Returns a randomly-chosen list item from the YAML file at `file_path`.
    """
    try:
        with open(file_path, 'r') as f:
            contents = yaml.load(f.read())
        item_no = random.randint(0, (len(contents) - 1))
        line = contents[item_no]
    except IOError as e:
        line = '\n  %s' % e

    return line


if __name__ == "__main__":
    # Accept the file name as the first positional argument.
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    # Print a random line from the file.
    print '\n  %s' % random_line(args.file)
