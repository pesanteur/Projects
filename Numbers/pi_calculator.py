"""Description from karan/Projects:
    Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
    This module gets pi up to 100,000 digits. Returns a string.
"""
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html')
content = r.text

soup = bs(content, 'html.parser')

def get_pi(i):
    #TODO: get this to ignore \n
    if i == 0:
        places = 25
    else:
        places = 26 + i
    pi_string = soup.body.text[24:places]
    pi = ''.join(pi_string.splitlines())
    return pi

