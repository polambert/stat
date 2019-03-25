#!/usr/bin/python3

import os
import subprocess

import psutil

# This is the main library file for Stat.

# Colors
class Colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

# Battery
class Battery:
    def get(file):
        f = os.path.join("/sys/class/power_supply/BAT0", file)
    
        cmd = "cat {}".format(f)

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        result = proc.stdout.read().decode().split("\n")[0]
        proc.stdout.close()

        return result

    def battery_percent():
        return int(Battery.get("capacity"))

    def battery_time():
        return int(Battery.get("power_now"))

# Memory
class Memory:
    def percent():
        return psutil.virtual_memory().percent

    def used():
        return psutil.virtual_memory().used

    def total():
        return psutil.virtual_memory().total

# CPU
class CPU:
    def percent(interval):
        return psutil.cpu_percent(interval=interval)

    def percent_per_cpu(interval):
        return psutil.cpu_percent(interval=interval, percpu=True)

# Disk
class Disk:
    def percent(path):
        return psutil.disk_usage(path).percent

    def used(path):
        return psutil.disk_usage(path).used

    def total(path):
        return psutil.disk_usage(path).total

