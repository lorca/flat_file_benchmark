import time
import pickle
import os
import subprocess
import sys
import signal

def gather_stats(filename):
    try:
        stats = {}
        _gather_stats(stats)
    except:
        f = open(filename,"w")
        pickle.dump(stats, f)
        f.close()

def _gather_stats(stats):
    mem_stat={}
    stats["mem"] = mem_stat
    mem_infos = [line.split() for line in open("/proc/meminfo").read().replace(":","").split("\n") if line]
    for mem_info in mem_infos: mem_stat[mem_info[0]] = []

    cpu_stat={}
    stats["cpu"] = cpu_stat
    cpu_infos = [line.split() for line in open("/proc/stat").read().split("\n") if line]
    for cpu_info in cpu_infos:
        i = 1
        for info in cpu_info[1:]:
            cpu_stat[cpu_info[0] + "_" + str(i)] = []
            i = i + 1

    while 1:
        mem_infos = [line.split() for line in open("/proc/meminfo").read().replace(":","").split("\n") if line]
        for mem_info in mem_infos: mem_stat[mem_info[0]].append(mem_info[1])

        cpu_infos = [line.split() for line in open("/proc/stat").read().split("\n") if line]
        for cpu_info in cpu_infos:
            i = 1
            for info in cpu_info[1:]:
                cpu_stat[cpu_info[0] + "_" + str(i)].append(info)
                i = i + 1
 
        time.sleep(1)

def benchmark(filename, cmd, margin, delay):
    time.sleep(delay)
    collector_pid = os.fork()
    if not collector_pid:
        gather_stats(filename)
        sys.exit(0)
    time.sleep(margin)
    exec_pid = os.fork()
    if not exec_pid:
        os.execvp(cmd[0], cmd)
        sys.exit(0)
    os.waitpid(exec_pid, 0)
    time.sleep(margin)
    os.kill(collector_pid, signal.SIGINT)
    os.waitpid(collector_pid, 0)

