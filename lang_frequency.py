import os
import sys
import re
from collections import Counter


def load_data(filepath):

    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as data_file:
        return data_file.read().lower()


def get_most_frequent_words(text):
    ''' Finds 10 most common words '''

    # to count non-ASCII letters as well
    words = re.findall(r'\b[^\W\d_]+\b', text, re.I)
    return Counter(words).most_common(10)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('Usage: python lang_frequency.py < filepath >')
    else:
        your_text = load_data(sys.argv[1])

    if not your_text:
        sys.exit('Error: the file %s was not found!' % sys.argv[1])
    else:
        for a_word in get_most_frequent_words(your_text):
            print(a_word[0])
