#!/bin/python3

import collections
import re
import sys
import time
import string
import fileinput
import argparse

def clean_input(line):

    # Format strings ignore punctuation, lower casing, squashing contractions
    return re.findall(r'\w+', line.lower().translate(str.maketrans('','',string.punctuation)))

def get_ngrams(lines, sequence_count=3):
    # Generate ngram frequencies and store them into a dictionary
    #  containing the sequence count mapped to a Counter object tuple
    #  that contains said ngram and frequency

    # Initialize dictionary and queue
    ngrams = {sequence_count: collections.Counter()}
    queue = collections.deque(maxlen=sequence_count)

    # Adds ngram for queue to dictionary
    def add_to_queue():
        current = tuple(queue)
        if len(current) >= sequence_count:
            ngrams[sequence_count][current[:sequence_count]] += 1

    # Find and add ngrams to dictionary
    for line in lines:
        for word in clean_input(line):
            queue.append(word)
            if len(queue) >= sequence_count:
                add_to_queue()

    # Gets last ngram in queue
    while len(queue) > sequence_count:
        queue.popleft()
        add_to_queue()

    return ngrams


def rank_occurrences(ngrams, rankings=100):
    for n in sorted(ngrams):
        print('Ranked {} ocurring {}-grams:'.format(rankings, n))
        for sequence, frequency in ngrams[n].most_common(rankings):
            print('{0} - {1}'.format(' '.join(sequence), frequency))
        print()

def main():

    #Parse input
    parser = argparse.ArgumentParser()
    parser.add_argument('input_files', metavar='FILE1 FILE2 ...', nargs='*', help='one or more files to use as input, otherwise stdin will be used')
    args = parser.parse_args()

    # Ensure we have _something_ to work with
    if not args.input_files:
        if sys.stdin.isatty():
            sys.exit("No input detected from stdin, try using the format: \n input_file.txt | python ngrams.py \n or \n python ngrams.py FILE ")

    # Execute core functions
    ngrams = get_ngrams(fileinput.input(files=args.input_files))
    rank_occurrences(ngrams)

if __name__ == '__main__':

    # Start timing after parsing input
    start_time = time.time()

    # Run core functions
    main()

    # Output execution time
    elapsed_time = time.time() - start_time
    print('Executed in {:.03f} seconds'.format(elapsed_time))
