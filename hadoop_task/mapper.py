#!/usr/bin/env python3
import sys

punctuations = '''
_)(.;,!?"“”‘’[]:-—/
'''

def preprocess(word):

    # TODO

def extract_html(word):

    # TODO

# Where do these lines come from?
# This is done by Hadoop Streaming ...
for line in sys.stdin:

    # Remove whitespace and split up line
    # into words (whitespace as delimiter)
    line = line.strip()
    words = line.split()

    for word in words:

        # TODO

        # The output is written to 'stdout' and will
        # be used as input by the reducers. Hadoop
        # Streaming will split up the work and will
        # feed these new lines to the reducers!
        print('%s\t%s' % (word, 1))
