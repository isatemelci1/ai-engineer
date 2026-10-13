import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 trex.py NAME")

cowsay.trex(f"Hello {sys.argv[1]}")