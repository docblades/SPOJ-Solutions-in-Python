#!/usr/bin/python
# created by Christian Blades (christian.blades@gmail.com) - Sun Oct 03, 2010

# Solution to http://www.spoj.pl/problems/CMPLS/

# Requires numpy

from numpy import array
from numpy.linalg import solve

class DepthError(Exception):
    """ Raised when len(sequence) < depth + 1 """
    pass

def getInput():
    seqList = []
    
    while True:
        numSeq = raw_input('> ')
        try:
            numSeq = int(numSeq)
        except ValueError:
            print "Input: 1 integer"
        else:
            break
        
    for i in range(0, numSeq):
        while True:
            seqInfo = raw_input('> ')
            numInSeq, numOutput = seqInfo.split(' ', 1)
            try:
                numOutput = int(numOutput)
            except ValueError:
                print "Input: 2 integers separated by a space"
            else:
                break
        
        while True:
            seqInput = raw_input('> ')
            seqInput = seqInput.split()

            try:
                sequence = []
                for i in seqInput:
                    sequence.append(int(i))
            except ValueError:
                print "Input: N integers separated by a space"
            else:
                break

        seqDict = {'sequence': sequence, 'numOutput': numOutput}
        seqList.append(seqDict)

    return seqList

def findDepth(sequence):
    """ Here, we find the difference between each number in the sequence, then difference between each of those differences, and so on until we find a distance of 0. How many steps we had to go through gives us our depth, and the maximum exponent in our polynumeral. """
    differences = [list(sequence)]

    maxDist = -1
    while maxDist != 0:
        maxDist = -1
        currentList = differences[len(differences) - 1]
        # If we've run out of number to compare, but haven't found the max depth, our sample sequence wasn't large enough. Basically, our sample size needs to be depth + 1.
        if len(currentList) == 1: raise DepthError
        differences.append([])
        currentDiffs = differences[len(differences) - 1]
        for i in range(0, len(currentList) - 1):
            diff = abs(currentList[i] - currentList[i+1])
            currentDiffs.append(diff)
            if diff > maxDist: maxDist = diff

    return len(differences) - 1

def makeMatrix(sequence):
    depth = findDepth(sequence)

    matrix = []
    y = []
    # P(n) = sub(a,d) * n**d-n + sub(a,d) * n**d-n + ... + sub(a,d) * n**0
    for n in range(1, depth+1):
        matrixLine = []
        for d in range(0,depth)[::-1]:
            matrixLine.append(n ** d)
        y.append(sequence[n-1])
        matrix.append(matrixLine)

    a = array(matrix)
    y = array(y)

    return a, y

def doOutput(sequence, outputNum):
    """ Here we:
    * solve our matrix, which gives us the A,B,C in P(n) = A * n^D + B * n^D...
    * round up to the nearest integer in the solution
    * generate and calculate our polynomial
    """
    a, y = makeMatrix(sequence)
    solution = solve(a,y)
    outputList = []

    for n in xrange(len(sequence) + 1, len(sequence) + outputNum + 1):
        ans = 0
        print "n: %d" % n
        for x in xrange(0, len(solution)):
            ans += round(solution[x]) * n ** (len(solution) - 1 - x)
        outputList.append(ans)

    return outputList
        
if __name__ == '__main__':
    seqList = getInput()
    print findDepth(seqList[0]['sequence'])
    outList = doOutput(seqList[0]['sequence'], seqList[0]['numOutput'])
    print outList
    for x in outList: print "Out: %d" % x
