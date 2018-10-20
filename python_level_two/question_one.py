"""
Write a program that calculate and prints the value according to the given formula
Q = square root of [(2 * C * D)/ H]

"""
import math


def get_square_root_from_numbers():
    c = 50
    h = 30
    your_result = []
    value = [x for x in input().split(",")]

    for d in value:
        your_result.append(str(int(round(math.sqrt((2 * c * float(d)/h))))))

    print(",".join(your_result))


get_square_root_from_numbers()
