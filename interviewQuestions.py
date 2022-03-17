#1. how to find sum of digits of a positive integer number using recursion?

def sumOfDigits(n):
    assert n>=0 and int(n)==n, 'must be positive and whole number'
    print(n)
    if (n==0):
        return n
    return ((n%10)+sumOfDigits(n//10))

print(sumOfDigits(1122))    