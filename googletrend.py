import requests
from xml.etree.ElementTree import *
import re
import json

namespace = '{http://www.w3.org/2005/Atom}'

def currenttrend():
    res = requests.get('http://www.google.co.jp/trends/hottrends/atom/hourly')
    root = fromstring(res.text)
    entry = root.find(namespace+'entry')
    title = entry.find(namespace+'title')
    result = title.text.split(', ')
    return result[:-1]

r = requests.get('http://www.google.com/trends/fetchComponent?q=bitcoin&cid=TIMESERIES_GRAPH_0&export=3')
jsontext = re.search('\(.+\)',r.text).group()[1:-1]
jsontext = re.sub('new Date\(.+?\)','"..."',jsontext)
j = json.loads(jsontext)
