#!/usr/bin/env python

import requests

print requests.__version__

#sth like curl
response = requests.get("https://raw.githubusercontent.com/Aries0331/c404Lab/master/checkversion.py") 
#get script for google "http://google.com"
#request is automatically following so instead we get google.ca

print response.text
print response.status_code
