# vim: ft=python

import random as random_

BRANCH_SIZE = 25
BRANCH_POS_OFFS = 0.1
BRANCH_NEG_OFFS = 0.2
CLR_POS_OFFS = 5
CLR_NEG_OFFS = 10

def add_polar(x, y, th, r):
    return (x + r * cos(th),
            y + r * sin(th))

def shufflepop(l):
    i = random_.randrange(len(l))
    l[i], l[-1] = l[-1], l[i]
    return l.pop()

def make_branch(coltz):
    val, ori, c, (x, y) = shufflepop(coltz)
    nx, ny = add_polar(x, y, ori, BRANCH_SIZE)
    stroke(c % 255, 255, 255)
    line(x, y, nx, ny)
    coltz.append( (val * 2, ori + BRANCH_POS_OFFS, c + CLR_POS_OFFS, (nx, ny)) )
    
    if (val - 4) % 6 == 0:
        coltz.append( ( (val - 1) // 3, ori - BRANCH_NEG_OFFS, c - CLR_NEG_OFFS, (nx, ny) ) )

def setup():
    global coltz_locs
    size(1300, 900)
    colorMode(HSB, 255, 255, 255)
    background(0)
    strokeWeight(0.7)
    coltz_locs = [(1, 0, 0, (50, 50))]

def draw():
    make_branch(coltz_locs)

def keyPressed():
    if keyCode == ord("R"):
        setup()
