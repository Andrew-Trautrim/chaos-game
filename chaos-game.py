from graphics import *
import random
import time

WIDTH = 1500
HEIGHT = 900

DELAY = 0
NUM_POINTS = 3

def main():
    win = GraphWin("Chaos Game", WIDTH, HEIGHT)
    win.setBackground('black')

    text = Text(Point(75, 25), "")
    text.setTextColor('white')
    text.draw(win)

    points = []
    for i in range(NUM_POINTS):
        text.setText("Set end point " + str(i + 1) + "/" + str(NUM_POINTS))
        pt = win.getMouse()
        pt.setFill('white')
        pt.draw(win)
        points.append(pt)

    text.setText("Set starting point")
    iter = win.getMouse()
    iter.setFill('white')
    iter.draw(win)

    text.setText("")
    while True:
        try: 
            pt = points[random.choice(range(NUM_POINTS))]
            iter = getMidPoint(iter, pt)
            iter.setFill('white')
            iter.draw(win)
            time.sleep(DELAY)
        except KeyboardInterrupt:
            break

    win.close()

def getMidPoint(p1, p2):
    return Point((p1.getX() + p2.getX())/2, (p1.getY() + p2.getY())/2)

main()