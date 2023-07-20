# import sys

# print("Hello, " + sys.argv[1])

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
