
#you have a stack of hundreds and you need to know how much money you have

from random import randrange

def recursion(stack, totalAmount=0):
    if (stack==0):
        return totalAmount
    totalAmount+=100
    return recursion(stack-1, totalAmount)

stack = randrange(1, 100)
print(stack)

print(recursion(stack))

