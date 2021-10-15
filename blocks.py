# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

from PIL import Image
import random
import math

SIZE = 256
PASSES = 10

xv = [random.random() for _ in range(SIZE)]
yv = [random.random() for _ in range(SIZE)]

def get_value(x,y):
    return int((xv[x]+yv[y])/2+0.3)

vals = [[get_value(x,y) for x in range(SIZE)] for y in range(SIZE)]

def celluar(grid):
    def cell_pass(x,y):
        total = 0
        count = 0
        if x>0:
            total += grid[x-1][y]
            count += 1
        if x<SIZE-2:
            total += grid[x+1][y]
            count += 1
        if y>0:
            total += grid[x][y-1]
            count += 1
        if y<SIZE-2:
            total += grid[x][y+1]
            count += 1
        return int(total/count+0.5)
    return [[cell_pass(x,y) for x in range(SIZE)] for y in range(SIZE)]

for _ in range(PASSES):
    vals = celluar(vals)

im = Image.new("RGB",(SIZE,SIZE))

pix = im.load()

for x in range(SIZE):
    for y in range(SIZE):
        pix[x,y] = (int(vals[x][y]*255),int(vals[x][y]*255),int(vals[x][y]*255))

im.save("output.png")