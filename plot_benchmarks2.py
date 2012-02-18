#!/usr/bin/env python
import pickle
import numpy as np
import matplotlib
matplotlib.use('Cairo')
import matplotlib.pyplot as plt
import os

fig = plt.figure()

def plot(label, filename):
    global fig
    stat = pickle.load(open(filename))["mem"]["Active"]
    stat = [int((int(number) - int(stat[0]))/1024.0) for number in stat]
    ax = fig.add_subplot(111)
    ax.plot(stat, label=label)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Memory Usage (M)")
    leg = ax.legend(loc="lower right")

   # print ",".join([label,str(len(stat)),str(stat[-1])])
    
    print "<tr><td>", label, "</td><td>", str(len(stat)), "</td><td>", str(stat[-1]), "</td></tr>"

filenames = []
for root, dirs, files in os.walk("output2"):
    for name in files: filenames.append((root,name))

filenames.sort()

for filename in filenames:
    path = filename[0]
    name = filename[1]
    label = name.replace(".benchmark","")
    plot(label, path + "/" + name)

fig.suptitle("Reading a 135M TSV File into Memory")

plt.savefig("pics/benchmark2.png")

