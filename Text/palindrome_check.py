""" Description from karan/Projects:
    Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
"""

from reverse_string import reverse_string

def palindrome_check(string):
    if reverse_string(string) == string:
        print('It\'s a palindrome!')
    else:
        print('It\'s not a palindrome!')
