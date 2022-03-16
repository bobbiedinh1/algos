#example of how recursion works
def firstMethod():
    secondMethod()
    print("first method")

def secondMethod():
    thirdMethod()
    print("second method")

def thirdMethod():
    fourthMethod()
    print("third method")

def fourthMethod():
    print("fourth method")

firstMethod()

#what happened in the above code? well firstMethod called the secondMethod, but cannot be completed because secondMethod has not yet been completed.
#this requires firstMethod to be stored in memory, then proceeds to call secondMethod.
#Due to this, secondMethod is then placed on top of firstMethod creating the stack
#it continues until it reaches fourthMethod in which fourthMethod completes itself with the print statement.
#once fourthMethod is completed it then gets removed from memory(the stack) and continues back to thirdMethod.



#you have a stack of hundreds and you need to know how much money you have
from random import randrange

def recursion(stack, totalAmount=0):
    if (stack==0):
        return totalAmount
    totalAmount+=100
    print(totalAmount)
    return recursion(stack-1, totalAmount)

stack = randrange(1, 100)
