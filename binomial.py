#!/usr/bin/env python
"""Calculate the binomial coefficent using functions logfactorial and choose

    notes:
    - imports argparse, math

"""
import math
import argparse
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("--log", action="store_true", help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfactorial(n, k=0):
   """Calculate the log factorial of n: log(n!) for any integer n>0

    notes:
    - import math

    Examples:

    >>> logfactorial(4)
    3.1780538303479453
    >>> logfactorial(5,3)
    2.995732273553991
    >>> logfactorial(5,5)
    0
    >>> logfactorial(5,6)
    0.0
    """
   
   total=0 
   assert n > 0
   assert type(n) == int
   assert k >= 0
   assert type(k) == int
   if k > n:
       total = math.log(1)
       return total
   else: 
       for i in range(k+1,n+1):
         total = total + math.log(i)
       return total  

def choose(n,k,l=False):
    """Calculate the log of the binomial log(choose(n,k)) for any integers n>=0 and 0<=k<=n

    notes:
    - import math
    - uses function logfactorial

    Examples:

    >>> choose(3,1)
    3
    >>> choose(3,1,True)
    1.0986122886681096
    >>> choose(6,5,True)
    1.791759469228055
    >>> choose(4,2,False)
    6
    """
    
    total=0 
    assert n > 0
    assert type(n) == int
    assert k >= 0 & k<= n 
    assert type(k) == int
    assert l == True or l==False

    total = logfactorial(n,k) - logfactorial(n-k,0)
    if l==False:
        total = round(math.exp(total))
    
    return total 

if __name__ == '__main__':
    if args.test:
        import doctest
        doctest.testmod()
    else:
        print(choose(args.n,args.k,args.log))



