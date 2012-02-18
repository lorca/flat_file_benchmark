import sys

rows = []
f = open(sys.argv[1])
for line in f:
    rows.append(tuple(line[:-1].split("\t")))
rows = tuple(rows)
print ",".join(rows[1])

