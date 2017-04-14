#!/usr/bin/env python3

from random import randint
import requests

request = requests.get(url='https://raw.githubusercontent.com/thewarpaint/trumpmit/master/data.json')
data = request.json()
quote = data[randint(0, len(data) - 1)]

print(quote['text'])