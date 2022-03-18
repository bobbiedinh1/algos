#1. how to find sum of digits of a positive integer number using recursion?

def sumOfDigits(n):
    assert n>=0 and int(n)==n, 'must be positive and whole number'
    print(n)
    if (n==0):
        return n
    return ((n%10)+sumOfDigits(n//10)) 

#2. how to calculate power of a number using recursion?

def power(num, exp):
    assert int(exp)==exp and exp>=0, ""
    if exp in [0,1]:
        return 1
    return num*power(num, exp-1)

print(power(2.5,3))