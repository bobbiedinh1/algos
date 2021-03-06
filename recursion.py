from random import randrange

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

#RECURSION COMPARSION

#you have a stack of hundreds and you need to know how much money you have

def recursion(stack, totalAmount=0):
    if (stack==0):
        return totalAmount
    totalAmount+=100
    return recursion(stack-1, totalAmount)

stack = randrange(1, 100)

def iteration(stack, totalAmount=0):
    while stack>0:
        totalAmount+=100
        stack-=1
    return totalAmount

def factorial(n):
    assert n>=0 and int(n) == n, 'must be greater or = to 0 and positive'
    if n in [0,1]:
        return 1
    return (n * factorial(n-1))

print(factorial(4))


def fibonacci(n):
    assert n>=0 and int(n) == n, 'must be greater or = to 0 and positive'
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(-6))