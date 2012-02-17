import sys

rows = []
f = open(sys.argv[1])
for line in f:
    rows.append(line[:-1].split("\t"))
print(",".join(rows[1]))

