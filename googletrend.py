import requests
from xml.etree.ElementTree import *

namespace = '{http://www.w3.org/2005/Atom}'

def trend():
    res = requests.get('http://www.google.co.jp/trends/hottrends/atom/hourly')
    root = fromstring(res.text)
    entry = root.find(namespace+'entry')
    title = entry.find(namespace+'title')
    result = title.text.split(', ')
    return result[:-1]
