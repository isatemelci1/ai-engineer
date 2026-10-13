import sys
from sayings import hello, goodbye

if len(sys.argv) != 2:
    sys.exit("Usage: python3 sayingsimport.py Name")

hello(sys.argv[1])
goodbye(sys.argv[1])