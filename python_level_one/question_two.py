"""
Write a program which can compute the factorial of given numbers.
RETURN:
    result should be printed in a comma-separated sequence on a single line
Example result for input 8 output is 40320
8!  = 1*2*3*4*5*6*7*8 = 40320
"""
n = int(input("write the number"))


def compute_the_factorial(n):

    if n == 0:
        return 1
    elif n != 0:
        return n * compute_the_factorial(n - 1)


print(compute_the_factorial(n))
