import os
import sys
import re
from collections import Counter
import argparse


def load_data(filepath):

    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as data_file:
        return data_file.read()


def get_most_frequent_words(text, first_n_words):

    # to count non-ASCII letters as well
    words = re.findall(r'\b[^\W\d_]+\b', text, re.I)
    return Counter(words).most_common(first_n_words)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    args = parser.parse_args()
    your_text = load_data(args.filepath)
    if not your_text:
        sys.exit('Error: the file %s was not found!' % args.filepath)
    else:
        first_n_words = 10
        for a_word in get_most_frequent_words(
                your_text.lower(), first_n_words):
            print(a_word[0])
