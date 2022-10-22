ERROR = 0.01

def getCoordinates():
    coords = input().split()
    return [int(coords[0]), int(coords[1])]

def absDiff(c1, c2):
    return c1 - c2 if c1 >= c2 else c2 - c1

testsNumber = int(input())


for currentTest in range(testsNumber):
    
    ballsNumber = int(input())

    xWhiteBall, yWhiteBall = getCoordinates()

    minDistance = 100000
    closestBall = 0

    for currentBall in range(ballsNumber):

        xBall, yball = getCoordinates()

        xdiff = xWhiteBall - xBall
        ydiff = yWhiteBall - yball

        ballDistance = (xdiff**2 + ydiff**2)**0.5
    
        if(ballDistance < minDistance and absDiff(ballDistance, minDistance) > ERROR):
            minDistance = ballDistance
            closestBall = currentBall + 1

    print(closestBall)
