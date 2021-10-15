# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

from PIL import Image
import random
import math

SIZE = 256
POINTS = 32

def get_height(points,x,y):
    sum = 0
    weights = 0
    for p in points:
        w = (1/(math.sqrt((p[0]-x)**2+(p[1]-y)**2))**32)
        weights += w
        sum += p[2]*w
    return sum/weights

points = [(random.uniform(-0.1,1.1),random.uniform(-0.1,1.1),i/(POINTS-1)) for i in range(POINTS)]
red = [[get_height(points,x/SIZE,y/SIZE) for x in range(SIZE)] for y in range(SIZE)]

points = [(random.uniform(-0.1,1.1),random.uniform(-0.1,1.1),i/(POINTS-1)) for i in range(POINTS)]
blue = [[get_height(points,x/SIZE,y/SIZE) for x in range(SIZE)] for y in range(SIZE)]

points = [(random.uniform(-0.1,1.1),random.uniform(-0.1,1.1),i/(POINTS-1)) for i in range(POINTS)]
green = [[get_height(points,x/SIZE,y/SIZE) for x in range(SIZE)] for y in range(SIZE)]

im = Image.new("RGB",(SIZE,SIZE))

pix = im.load()

for x in range(SIZE):
    for y in range(SIZE):
        pix[x,y] = (int(red[x][y]*255),int(blue[x][y]*255),int(green[x][y]*255))

im.save("output.png")