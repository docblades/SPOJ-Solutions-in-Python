#!/usr/bin/python
# Solution to http://www.spoj.pl/problems/PRIME1/
# created by Christian Blades (christian.blades@gmail.com) - Fri Oct 01, 2010

# Problem: Return a list of all primes from m -> n

import math
import time

# Wrapper that times how long the naive findPrimes takes
def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms ' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

class BadRange(Exception):
    pass

def isEvenDiv(a, b):
    # If a / b has a remainder, return False
    if math.modf(float(a) / float(b))[0] != 0.0:
        return False
    else:
        return True

def getInput():
    m = raw_input('m: ')
    n = raw_input('n: ')

    m = int(m)
    n = int(n)

    # Restrictions on input from the original problem
    if n > 1000000000 or n - m > 100000 or m < 1 or n - m < 1:
        raise BadRange()

    return m, n


def isPrime(num, primesIn):
    """Test if a number is prime using a naive primes algorithm
    
    Arguments:
         num -- Number to test for primality
         primesIn -- List of known primes. Include at least 1 and 2 in this list
    Returns a boolean
    """
    # Make a copy of the primes list so that we can remove '1' from it later
    primes = list(primesIn)
    
     #if it's in the list of primes, it must be prime, right?
    if num in primes: return True

    # if it's divisible by any primes(except 1), it's not prime
    primes.remove(1)
    for x in primes:
        if isEvenDiv(num, x): return False

    # Testing against all other odd numbers up to sqrt(num)
    # (assuming primes contains all primes sequentially, and it doesn't end in '2')
    for x in range(max(primes), int(math.sqrt(num)), 2):
        if isEvenDiv(num, x): return False

    # if it made it this far, it must be prime
    return True

# 1, 2, and 3 are primes
primes = range(1,4)

@print_timing
def findPrimes(start, finish):
    global primes
    returnablePrimes = []

    # if our range is within the range of found primes,
    # just return the intersection of the two sets
    if max(primes) >= finish:
        primesSet = set(primes)
        rangeSet = set(range(start, finish))
        returnablePrimes = list(rangeSet.intersection(primesSet))
        return returnablePrimes

    # find all the primes, from known up to m
    for x in range(max(primes), start):
        if isPrime(x, primes): primes += [x]

    # Test for primes from m to n
    for x in range(start, finish+1):
        if isPrime(x, primes):
            if x not in primes: primes += [x]
            returnablePrimes += [x]

    return returnablePrimes

# main loop
while True:
    try:
        m, n = getInput()
    except BadRange:
        print "Invalid range, try again"
    except ValueError:
        print "Please type numbers only"
    except EOFError:
        print "Goodbye"
        break
    except KeyboardInterrupt:
        print "Goodbye"
        break
    else:
        # reassuring message
        print 'working...'
        retPrimes = findPrimes(m,n)
        for x in retPrimes: print x
        print "Total primes returned: %d" % len(retPrimes)
