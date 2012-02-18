#!/usr/bin/env python
import pickle
import os
import json

def plot(label, filename):
    stat = pickle.load(open(filename))["mem"]["Active"]
    stat = [int((int(number) - int(stat[0]))/1024.0) for number in stat]
    return {"mem":max(stat),"program":label,"cpu":len(stat)}

filenames = []
for root, dirs, files in os.walk("output"):
    for name in files: filenames.append((root,name))

filenames.sort()

stats=[]
for filename in filenames:
    path = filename[0]
    name = filename[1]
    label = name.replace(".benchmark","")
    stat = plot(label, path + "/" + name)
    stats.append(stat)

print json.dumps(stats)
