#!user/bin/env python

import bitly_api
import sys

#Define Bitly Api Details

API_USER = "l0ndoner"
API_KEY = "6fd9798ab922047be169b516c52681468379013e"
b = bitly_api.Connection(access_token=API_KEY)

usage = """ Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com """

if len(sys.argv) != 2:
	print usage
	sys.exit(0)

longurl	= sys.argv[1]

response = b.shorten(uri=longurl)

print response["url"]
