#!/usr/bin/python
# created by Christian Blades (christian.blades@gmail.com) - Sat Oct 02, 2010

# Solution to http://www.spoj.pl/problems/PALIN/

def getInput():
    a = raw_input('number: ')
    return int(a)

def isPalindrome(num):
    numString = str(num)
    start = 0
    end = len(numString) - 1
    while(start < end):
        if numString[start] != numString[end]: return False
        start += 1
        end -= 1
    return True

def nextPalindrome(num):
    if len(str(num)) < 2:
        if num < 9:
            return num + 1
        else:
            return 11

    num += 1

    while(not isPalindrome(num)):
        num += 1

    return num

# main loop
if __name__ == '__main__':
    while True:
        try:
            num = getInput()
        except ValueError:
            print "Please only type integers"
        except EOFError:
            print "Goodbye"
            break
        except KeyboardInterrupt:
            print "Goodbye"
            break
        else:
            palResult = nextPalindrome(num)
            print "Next palindrome: %d" % palResult
    
        
