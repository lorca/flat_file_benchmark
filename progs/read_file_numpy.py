import sys
from numpy import genfromtxt

rows = genfromtxt(sys.argv[1], delimiter="\t", dtype=None)
print ",".join(map(lambda x: str(x), rows[1]))

