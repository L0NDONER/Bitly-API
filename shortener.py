#!user/bin/env python

import bitly_api
import sys

# Define Bitly Api Details

API_USER = "*****"  # USERNAME
API_KEY = "****************"  # API KEY
b = bitly_api.Connection(access_token=API_KEY)

usage = """ Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com """

if len(sys.argv) != 2:
    print usage
    sys.exit(0)

longurl = sys.argv[1]

response = b.shorten(uri=longurl)

print response["url"]
