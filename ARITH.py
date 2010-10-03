#!/usr/bin/python
# created by Christian Blades (christian.blades@gmail.com) - Sun Oct 03, 2010

# Solution for http://www.spoj.pl/problems/ARITH/

class InvalidFormat(Exception):
    pass

def getInput():
    rawInput = raw_input('> ')

    # find the operator
    opIndex = -1
    for x in '+-*':
        opIndex = rawInput.find(x)
        if opIndex != -1: break
    if opIndex == -1: raise InvalidFormat

    operator = rawInput[opIndex]
    left = rawInput[0:opIndex]
    right = rawInput[opIndex + 1:]

    left = int(left)
    right = int(right)

    return left, right, operator

def doSimpleFormat(left, right, operator, result):
    leftStr = str(left)
    rightStr = operator + str(right)
    lineStr = '-'
    resultStr = str(result)

    # find the length of the longest line
    width = 0
    for x in [leftStr, rightStr, resultStr]:
        if len(x) > width: width = len(x)

    # right justify all of the lines
    tempStrList = []
    for x in [leftStr, rightStr, resultStr]:
        tempStrList.append(x.rjust(width))

    lineStr *= width
    leftStr, rightStr, resultStr = tempStrList

    return leftStr, rightStr, lineStr, resultStr
    

def doAddition(left, right):
    sumStr = str(left + right)
    return doSimpleFormat(left, right, '+', sumStr)

def doSubtraction(left, right):
    difStr = str(left - right)
    return doSimpleFormat(left, right, '-', difStr)

def doMultiplication(left, right):
    leftStr = str(left)
    rightStr = '*' + str(right)
    # firstLineStr is the line under left, right and operator
    firstLineStr = '-'
    # lineStr is the line under all of the operations
    lineStr = '-'
    resultStr = str(left * right)
    # each of the operations
    resultLines = []

    # here we make a line for each of the operations
    # reversed string of the right number
    workingRight = str(right)[::-1]
    i = 0
    for x in workingRight:
        thisResult = str(int(x) * left)
        rightSpacing = ' ' * i
        resultLines.append(thisResult + rightSpacing)
        i += 1
        
    # width of the first line
    width = 0
    for x in [leftStr, rightStr]:
        if width < len(x): width = len(x)
    firstLineStr = firstLineStr * width

    # find the length of the longest line
    width = 0
    for x in [leftStr, rightStr, resultStr] + resultLines:
        if width < len(x): width = len(x)

    lineStr = lineStr * width

    # combine the lines, right justified
    lines = []
    for x in [leftStr, rightStr, firstLineStr] + resultLines + [lineStr, resultStr]:
        lines.append(x.rjust(width))

    # if there's only one operation line, then we don't need the second line and result
    if len(str(right)) == 1:
        return lines[:-2]
    else:
        return lines

if __name__ == '__main__':
    while True:
        try:
            left, right, operator = getInput()
        except InvalidFormat:
            print "FormAt: 1234+5678"
            print "Valid operators: +-*"
        except ValueError:
            print "Format: 1234+5678"
            print "Valid operators: +-*"
        else:
            if operator == '+':
                lines = doAddition(left, right)
            elif operator == '-':
                lines = doSubtraction(left, right)
            elif operator == '*':
                lines = doMultiplication(left, right)
            for x in lines:
                print x
