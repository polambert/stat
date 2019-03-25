#!/usr/bin/python3

# libstat.py

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

    def is_charging():
        return Battery.get("status") == "Charging"

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

## Common Functions
def interpret_time(text):
    # Interpret the text from left to right and add on to the total.
    # Time Texts are written as:
    # Xd Xh Xm Xs
    # With spaces in between.
    # The value returned is in seconds.
    total = 0

    cap = ""

    for i in text:
        if i in "0123456789":
            cap += i
        elif i == "d":
            total += int(cap) * 24 * 60 * 60
        elif i == "h":
            total += int(cap) * 60 * 60
        elif i == "m":
            total += int(cap) * 60
        else:
            total += int(cap)

    total += int(cap)

    return total

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
