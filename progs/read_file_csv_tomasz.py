import sys
import csv

with open(sys.argv[1]) as f:
   rows = list(csv.reader(f, "excel-tab"))
   print ",".join(rows[1])
