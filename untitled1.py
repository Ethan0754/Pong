from graphics import *
import time


def upScreen(aDirection, bDirection, aLine, bLine, ball, bMoveX, bMoveY, bX, bY, paddleAY, paddleBY):
    time.sleep(.05)
    
    
    #Paddles
    if(aDirection == "w"):
        aLine.move(0,-5)
        paddleAY += -5
    if(aDirection == "s"):
        aLine.move(0, 5)
        paddleAY += 5

    if(bDirection == "i"):
        bLine.move(0,-5)
        paddleBY += -5

    if(bDirection == "k"):
        bLine.move(0, 5)
        paddleBY += 5

    
        
        
    #Ball
    ball.move(bMoveX, bMoveY)
    bX += bMoveX
    bY += bMoveY
    if(detectPaddle(bX, bY, paddleAY, paddleBY) == "Left"):
        bMoveX, bMoveY = ballDirection(bMoveX, bMoveY, "Left")
    if(detectPaddle(bX, bY, paddleAY, paddleBY) == "Right"):
        bMoveX, bMoveY = ballDirection(bMoveX, bMoveY, "Right")
    return bMoveX, bMoveY, bX, bY, paddleAY, paddleBY

    
def ballDirection(bMoveX, bMoveY, side):
    bMoveX = -bMoveX
    bMoveY = bMoveY
    return bMoveX,bMoveY
        
def detectPaddle(bX, bY, paddleAY, paddleBY):
    print(bX)
    print(paddleBY)
    if(bX == 800):
        print("hi")
    if((bY > paddleAY-50 and bY < paddleAY+50) and (bX == 65)):
        return "Left"
    if((bY > paddleBY-50 and bY < paddleBY+50) and (bX == 935)):
        return "Right"
    
        
def play(win, aDirection, bDirection):
    press = win.checkKey()
    if press == "w" or press == "s":
        aDirection = press
    if press == "i" or press == "k":
        bDirection = press

    return aDirection, bDirection

def draw(win):
    
    aLine = Line(Point(50,450), Point(50,550))
    bLine = Line(Point(950,450), Point(950,550))
    aLine.draw(win)
    bLine.draw(win)
    ball = Circle(Point(500,500), 15)
    ball.draw(win)
    return aLine, bLine, ball


    


def main():
    win=GraphWin("Circle", 1000, 1000)

    aLine, bLine, ball = draw(win)

    aDirection = "w"
    bDirection = "i"
    bMoveX, bMoveY = 5, 0
    bX, bY = 500, 500
    paddleAY, paddleBY = 500, 500

    
    for i in range(1000):
        aDirection, bDirection = play(win, aDirection, bDirection)
        bMoveX, bMoveY, bX, bY, paddleAY, paddleBY = upScreen(aDirection, bDirection, aLine, bLine, ball, bMoveX, bMoveY, bX, bY, paddleAY, paddleBY)
        
    win.getMouse()
    win.close()

main()



  