from graphics import *
import sys
import random
import time

WIDTH = 1500
HEIGHT = 900

# Restriction 1: the current vertex cannot be chosen in the next iteration
# Restriction 2: the current vertex cannot be one place away (counter-clockwise) from the previously chosen vertex
# Restriction 3: the currently chosen vertex cannot neighbor the previously chosen vertex if the two previously chosen vertices are the same
RESTRICTION = 3
JUMP = 1/2
NUM_POINTS = 4

DELAY = 0

def main():
    win = GraphWin("Chaos Game", WIDTH, HEIGHT)
    win.setBackground('black')

    text = Text(Point(75, 25), "")
    text.setTextColor('white')
    text.draw(win)

    vertices = []
    for i in range(NUM_POINTS):
        text.setText("Set end point " + str(i + 1) + "/" + str(NUM_POINTS))
        pt = win.getMouse()
        pt.setFill('white')
        pt.draw(win)
        vertices.append(pt)

    text.setText("Set starting point")
    iter = win.getMouse()
    iter.setFill('white')
    iter.draw(win)

    text.setText("")
    current = -1
    previous = -1
    while True:
        try: 
            (current, previous, pt) = getNextVertex(current, previous, vertices)
            iter = getNextPoint(iter, pt)
            iter.setFill('white')
            iter.draw(win)
            time.sleep(DELAY)
        except KeyboardInterrupt:
            break

    win.close()

def getNextVertex(current, previous, vertices):
    next = -1
    if RESTRICTION == 1:
        next = random.choice([x for x in range(NUM_POINTS) if x != current])
    elif RESTRICTION == 2:
        next = random.choice([x for x in range(NUM_POINTS) if x != (current - 1) % NUM_POINTS])
    elif RESTRICTION == 3:
        if current == previous:
            next = random.choice([x for x in range(NUM_POINTS) if x != (current - 1) % NUM_POINTS and x != (current + 1) % NUM_POINTS])
        else:
            next = random.choice(range(NUM_POINTS))
    else:
        next = random.choice(range(NUM_POINTS))
    return (next, current, vertices[next])

def getNextPoint(p1, p2):
    return Point(p1.getX() + (p2.getX() - p1.getX()) * JUMP, p1.getY() + (p2.getY() - p1.getY()) * JUMP)

main()