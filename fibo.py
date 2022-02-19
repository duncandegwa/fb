
# python program to check if x is a perfect square
import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):
 
 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
   
i=int(input("Enter any number"))
     if (isFibonacci(i) == True):
         print (i,"is a Fibonacci Number")
     else:
         print (i,"is a not Fibonacci Number ")
