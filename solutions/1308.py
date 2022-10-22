
def getLineCount(qty):
    return int((-1 + (1+8*qty)**0.5)/2)


inputCount = int(input())

for i in range(inputCount):

    warriors = int(input())
    
    print(getLineCount(warriors))
    