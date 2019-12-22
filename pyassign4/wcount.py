#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.
__author__ = "Li Siyuan"
__pkuid__  = "1900011791"
__email__  = "tsd@pku.edu.cn"
"""

import sys
import string
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    newlines = lines.lower()
    for i in string.punctuation:
        newlines = newlines.replace(i, '')
    words = newlines.split()

    countdir = dict()
    for word in words:
        if word not in countdir:
            countdir[word] = 1
        else:
            countdir[word] += 1

    i = 0
    for word in sorted(countdir, key=lambda x: countdir[x], reverse=True):
        print('{0:9} {1:4d}'.format(word, countdir[word]))
        i += 1
        if i >= topn:
            break


def getfile(url):
    """get the content from the given URL, and returns the content in the
    type of string.
    """
    try:
        doc = urlopen(url)
    except:  # If something goes wrong when connecting
        print('Please check the URL and your Internet connection')
        sys.exit(1)
    else:
        pass
    docstr = doc.read()
    doc.close()
    try:
        content = docstr.decode('UTF-8')
    except:  # If the file can't be decoded as a textfile
        print("The given file can't be decoded with UTF-8. Please check it")
        sys.exit(1)
    else:
        pass
    return(content)


if __name__ == '__main__':
    if len(sys.argv) == 2:  # Analyze whether paras are right or not
        wcount(getfile(sys.argv[1]))
    elif len(sys.argv) == 3 and (sys.argv[2]).isnumeric():
        wcount(getfile(sys.argv[1]), int(sys.argv[2]))
    else:  # Run the program only when the paras are legal.
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print(
            '  topn: how many (words count) to output. ' +
            'If not given, will output top 10 words'
        )
        sys.exit(1)
