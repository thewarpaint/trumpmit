#!/usr/bin/env python3

from random import choice
import requests

request = requests.get(url='https://raw.githubusercontent.com/thewarpaint/trumpmit/master/data.json')
data = request.json()

print(choice(data)['text'])