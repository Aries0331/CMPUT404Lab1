#!/usr/bin/env python

import requests

print requests.__version__

#sth like curl
response = requests.get("http://google.com/") #get script for google
#request is automatically following so instead we get google.ca

print response.text
print response.status_code
