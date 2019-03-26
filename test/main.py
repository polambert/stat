#!/usr/bin/python3

import sys
import datetime
from math import sin, cos, pi, floor, ceil

## A graphical clock test. First, we need to create a display.
# Then, we'll just draw dots for the clock's minute hand.
# And finally, calculate the rotation of each clock as a percentage
#  of 360 degrees.

grid = []

def clear_grid():
    global grid
    grid = []
    for i in range(20):
        a = []
        for j in range(20):
            a.append(" ")
        grid.append(a)

def print_grid():
    for i in grid:
        a = ""
        for j in i:
            a += j + " "
        print(a)

# Draw a dot on the grid.
def draw(x, y):
    if x >= 0 and y >= 0:
        if x < 20 and y < 20:
            grid[y][x] = "."

def backspace():
    for i in range(20):
        sys.stdout.write("\033[F")

clear_grid()

while True:
    # Center point
    draw(10, 10)

    # Find the X/Y for the current second of the minute
    second = datetime.datetime.now().second
    
    degree = (second / 60) * 2 * pi - pi

    draw(int(round(10 - sin(degree) * 9)), int(round(10 + cos(degree) * 9)))

    # continue with graphical stuff
    print_grid()

    clear_grid()

    backspace()

