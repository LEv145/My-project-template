from os import system
from sys import argv


system(f"mkinit {argv[1]} -w --black --nomods --relative --recursive")
