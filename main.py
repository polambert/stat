#!/usr/bin/python3

import libstat as stat
import libcalc as calc

import math
import datetime
import time
import requests
import socket

# STAT is a program for doing hard things the easy way.
# Certain parts of STAT may be written in much more complicated languages.

# On load, print out vital information.

# Starting things.
print()
print(" --- STAT ---")

## BATTERY
def print_battery_usage():
    percent = stat.Battery.battery_percent()
    time = stat.Battery.battery_time() / 60000

    vector = str(math.floor(time // 60)) + "h " + str(math.floor(time % 60)) + "m"
    if stat.Battery.is_charging:
        vector = "Charging"

    string = "Battery: " + str(stat.Battery.battery_percent()) + " (" + vector +  ")"

    color = ""

    # Determine the color of the text for the battery
    if percent > 50:
        color = stat.Colors.green
    elif percent > 25:
        color = stat.Colors.warning
    else:
        color = stat.Colors.fail

    print("  " + color + string + stat.Colors.end)

## MEMORY

def print_memory_usage():
    percent = stat.Memory.percent()

    used = stat.Memory.used() / 1000000000
    total = stat.Memory.total() / 1000000000

    color = ""
    
    if percent < 75:
        color = stat.Colors.green
    elif percent < 90:
        color = stat.Colors.warning
    else:
        color = stat.Colors.fail

    print(color + "  Memory: " + str(percent) + "% (" + str(round(used, 2)) + "/" + str(round(total, 2)) + ")" + stat.Colors.end)

## PROCESSOR
def print_cpu_usage(interval=0.1):
    percent = stat.CPU.percent(interval=interval)

    percent_per_cpu = stat.CPU.percent_per_cpu(interval=interval)

    ppc_str = ""

    for i in percent_per_cpu:
        ppc_str += str(round(i, 0))[:-2] + " "

    ppc_str = ppc_str[:-1]

    color = ""

    if percent < 40:
        color = stat.Colors.green
    elif percent < 85:
        color = stat.Colors.warning
    else:
        color = stat.Colors.fail

    print(color + "  CPU: " + str(percent) + " (" + ppc_str + ")" + stat.Colors.end)

## HARD DRIVES
def print_disk_usage():
    percent = stat.Disk.percent("/")

    used = str(round(stat.Disk.used("/") / 1000000000, 2))
    total = str(round(stat.Disk.total("/") / 1000000000, 2))

    color = ""

    if percent < 80:
        color = stat.Colors.green
    elif percent < 95:
        color = stat.Colors.warning
    else:
        color = stat.Colors.fail

    print(color + "  Disk: " + str(percent) + "% (" + used + " G/" + total + " G)" + stat.Colors.end)

def get_time_readout():
    dtime = str(datetime.datetime.now()).split(" ")

    string = "   " + stat.Colors.green + dtime[0] + " " + stat.Colors.warning + dtime[1].split(".")[0]
    string += " UTS " + stat.Colors.blue + str(round(time.time(), 0))[:-2] + stat.Colors.end

    return string


print_battery_usage()
print_memory_usage()
print_disk_usage()

_time = datetime.datetime.now().strftime("%I:%M:%S")
print("  Time: " + _time)

print()

## The Main Loop.
while True:
    cmd = input(":> ")

    split = cmd.split(" ")

    prog = split[0]

    if cmd == "q" or cmd == "quit":
        break
    elif prog == "cpu":
        if cmd == prog:
            print_cpu_usage()
        else:
            time = " ".join(split[1:])
            time = stat.interpret_time(time)

            print_cpu_usage(interval=time / 2)
    elif prog == "time" or prog == "t":
        dtime = str(datetime.datetime.now()).split(" ")

        print(" " + stat.Colors.green + dtime[0] + " " + stat.Colors.warning + dtime[1].split(".")[0] + stat.Colors.end)
        print(" UTS " + stat.Colors.blue + str(round(time.time(), 0))[:-2] + stat.Colors.end)
    elif prog == "livetime" or prog == "lt":
        ## Live Time: A clock that re-prints itself over and over.
        while True:
            t = get_time_readout()
            l = len(t)

            print(t, end="")
            print('\r', end="")

            time.sleep(1)
    elif prog == "calc" or prog == "c":
        ## Launch the calculator
        calc.run()
    elif prog == "ip":
        ## Get their Public IP
        pubip = requests.get("https://ipapi.co/ip/").text
        print(stat.Colors.green + "  Public: " + pubip)

        ## Get their Private IP
        prvip = socket.gethostbyname(socket.gethostname())
        print(stat.Colors.warning + "  Private: " + prvip)
    else:
        if prog != "":
            print(" " + prog + ": not a known command.")

