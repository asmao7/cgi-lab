#!/usr/bin/env python3

import os
import json

#step 1
#print("content-Type: text/plain")
#print()
#print(os.environ)

#Q2
print("content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))

# if we add query parameters
# add a ? after .py
# changes: query string gets added at the bottom
# anything after ? gets put to the query string

#next
print("content-Type: text/html")
print()
print(f"<p>QUERY_sTRING={os.environ['QUERY_STRING']}</p>")


#question 3 do by yourself
# go over json stuff and 
# replace query string with var name
#


#question 4

#login form


#print(json.dumps(dict(os.environ), indent=2))

#print('Content-Type: text/html)
#print('Content-Type: application/octet-st..)
#print('Content TypeL text/plain')
#print()
#print("HELLO, BROWSER!!!!!")

