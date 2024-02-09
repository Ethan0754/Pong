from graphics import *
import time


def upScreen(aDirection, bDirection, aLine, bLine, ball, bMoveX, bMoveY, bX, bY, paddleAY, paddleBY):
    time.sleep(.02)
    
    
    if(aDirection == "w"):
        aLine.move(0,-8)
        paddleAY += -8
    if(aDirection == "s"):
        aLine.move(0, 8)
        paddleAY += 8
    if(bDirection == "i"):
        bLine.move(0,-8)
        paddleBY += -8
    if(bDirection == "k"):
        bLine.move(0, 8)
        paddleBY += 8
        
    if(paddleAY < 50 or paddleAY > 650):
        aDirection = ""
    if(paddleBY < 50 or paddleBY > 650):
        bDirection = ""
    
        
        
    #Ball
    ball.move(bMoveX, bMoveY)
    bX += bMoveX
    bY += bMoveY
    if(detectPaddle(bX, bY, paddleAY, paddleBY) == "Left"):
        bMoveX, bMoveY = ballDirection(bMoveX, bMoveY, "Left", paddleAY, paddleBY, bX, bY)
    if(detectPaddle(bX, bY, paddleAY, paddleBY) == "Right"):
        bMoveX, bMoveY = ballDirection(bMoveX, bMoveY, "Right", paddleAY, paddleBY, bX, bY)
    if(detectEdge(bY) == True):
        bMoveX, bMoveY = ballDirection(bMoveX, bMoveY, "NULL", paddleAY, paddleBY, bX, bY)
    return bMoveX, bMoveY, bX, bY, paddleAY, paddleBY, aDirection, bDirection

    
def ballDirection(bMoveX, bMoveY, side, paddleAY, paddleBY, bX, bY):
    if(side == "Left"):
        bMoveX = -bMoveX
        if(bY > paddleAY-10 and bY < paddleAY+10):
            bMoveY = bMoveY
        elif(bY > paddleAY+10 and bY < paddleAY+20):
            bMoveY = 2
        elif(bY > paddleAY+20 and bY < paddleAY+30):
            bMoveY = 4
        elif(bY > paddleAY+30 and bY < paddleAY+40):
            bMoveY = 6
        elif(bY > paddleAY+40 and bY < paddleAY+50):
            bMoveY = 8
        elif(bY > paddleAY-10 and bY < paddleAY-20):
            bMoveY = -2
        elif(bY > paddleAY-20 and bY < paddleAY-30):
            bMoveY = -4
        elif(bY > paddleAY-30 and bY < paddleAY-40):
            bMoveY = -6
        elif(bY > paddleAY-40 and bY < paddleAY-50):
            bMoveY = -8
    if(side == "Right"):
        bMoveX = -bMoveX
        if(bY > paddleBY-10 and bY < paddleBY+10):
            bMoveY = bMoveY
        elif(bY > paddleBY+10 and bY < paddleBY+20):
            bMoveY = 2
        elif(bY > paddleBY+20 and bY < paddleBY+30):
            bMoveY = 4
        elif(bY > paddleBY+30 and bY < paddleBY+40):
            bMoveY = 6
        elif(bY > paddleAY+40 and bY < paddleBY+50):
            bMoveY = 8
        elif(bY > paddleBY-10 and bY < paddleBY-20):
            bMoveY = -2
        elif(bY > paddleBY-20 and bY < paddleBY-30):
            bMoveY = -4
        elif(bY > paddleBY-30 and bY < paddleBY-40):
            bMoveY = -6
        elif(bY > paddleBY-40 and bY < paddleBY-50):
            bMoveY = -8
    if(bY < 10 or bY > 690):
        bMoveY = -bMoveY
    

    return bMoveX,bMoveY

def loseCondition(bX):
    if(bX == 20 or bX == 990):
        return True
    return False

def detectEdge(bY):
    if(bY < 10 or bY > 690):    
        return True
    

        
def detectPaddle(bX, bY, paddleAY, paddleBY):
    if((bY > paddleAY-50 and bY < paddleAY+50) and (bX == 120)):
        return "Left"
    if((bY > paddleBY-50 and bY < paddleBY+50) and (bX == 880)):
        return "Right"
    
        
def play(win, aDirection, bDirection):
    press = win.checkKey()
    if press == "w" or press == "s":
        aDirection = press
    if press == "i" or press == "k":
        bDirection = press

    return aDirection, bDirection

def draw(win):
    
    aLine = Line(Point(100,300), Point(100,400))
    bLine = Line(Point(900,300), Point(900,400))
    aLine.draw(win)
    bLine.draw(win)
    ball = Circle(Point(500,350), 15)
    ball.draw(win)
    return aLine, bLine, ball


    


def main():
    win=GraphWin("Circle", 1000, 700)

    aLine, bLine, ball = draw(win)

    aDirection = "w"
    bDirection = "i"
    bMoveX, bMoveY = 10, 0
    bX, bY = 500, 350
    paddleAY, paddleBY = 350, 350

    win.getMouse()
    while(loseCondition(bX)==False):
        
        aDirection, bDirection = play(win, aDirection, bDirection)
        bMoveX, bMoveY, bX, bY, paddleAY, paddleBY, aDirection, bDirection = upScreen(aDirection, bDirection, aLine, bLine, ball, bMoveX, bMoveY, bX, bY, paddleAY, paddleBY)
        
    win.getMouse()
    win.close()

main()



  