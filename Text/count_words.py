""" Description from karan/Projects:
    Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
"""
from sys import argv

def count_words(sentence):
    words = sentence.split(' ')
    count = 0
    for word in words:
        count += 1
    return count

if __name__ == "__main__":
    script, filename = argv
    f = open(filename, 'r')
    sentences = f.read()
    word_count = count_words(sentences)
    print('This file has %s words.' % word_count)
