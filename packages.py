# a package is a third party library that is downloaded for use in your machine
# sys  package gives access to commandline arguments
"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
"""

# the requests package is used when calling http requests
# the json package is used to format json documents
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()
# print(json.dumps(o, indent=2)) # This prints out the json document
for result in o["results"]:
    print(result["trackName"])



