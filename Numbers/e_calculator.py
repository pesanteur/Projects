"""
"""
import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.math.utah.edu/~pa/math/e.html')
content = r.text

soup = bs(content, 'html.parser')

def get_e(i):
    #TODO: Get rid of erroneous spacings
    if i == 0:
        places = 5
    else:
        places = 6 + i
    e_string = soup.body.p.text[5:places]
    e = ''.join(e_string.splitlines())
    return e
