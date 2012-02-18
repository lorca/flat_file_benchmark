#!/usr/bin/env python
import pickle
import numpy as np
import matplotlib
matplotlib.use('Cairo')
import matplotlib.pyplot as plt
import os
import json

fig = plt.figure()

def plot(label, filename):
    stat = pickle.load(open(filename))["mem"]["Active"]
    stat = [int((int(number) - int(stat[0]))/1024.0) for number in stat]
    print "<tr><td>", label, "</td><td>", str(len(stat)), "</td><td>", str(stat[-1]), "</td></tr>"
    return (stat[-1],label)

filenames = []
for root, dirs, files in os.walk("output"):
    for name in files: filenames.append((root,name))

filenames.sort()

stats=[]
labels=[]
for filename in filenames:
    path = filename[0]
    name = filename[1]
    label = name.replace(".benchmark","")
    stat = plot(label, path + "/" + name)
    stats.append(stat)

from pylab import *
pos = arange(len(stats))+.25    # the bar centers on the y axis

figure(1)
barh(pos, map(lambda x: x[0], stats), align='center')
yticks(pos, map(lambda x: x[1], stats))
xlabel('Memory Usage (M)')
title('Reading a 135M TSV File into a List of Lists')
grid(True)
plt.savefig("pics/benchmark.png")


#figure(2)
#barh(pos,val, xerr=rand(5), ecolor='r', align='center')
#yticks(pos, ('Tom', 'Dick', 'Harry', 'Slim', 'Jim'))
#xlabel('Performance')
