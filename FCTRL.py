#!/usr/bin/python

# created by Christian Blades (christian.blades@gmail.com) - Tue Oct 12, 2010

def getInput():
    numOfLines = raw_input("> ")
    numOfLines = int(numOfLines)

    inNums = []
    for n in range(0, numOfLines):
        num = raw_input("> ")
        inNums.append(int(num))

    return inNums

def doCalc(inNums):
    trailingZeros = []

    for x in inNums:
        num = 0
        exp = 1
        while (5 ** exp <= x):
            num += x / 5 ** exp
            exp += 1
            
        trailingZeros.append(num)

    return trailingZeros
        
if __name__ == "__main__":
    while True:
        try:
            inNums = getInput()
        except ValueError:
            print "Integers only"
        else:
            trailingZeros = doCalc(inNums)
            for x in trailingZeros:
                print x
            break
