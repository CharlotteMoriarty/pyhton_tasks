"""
Write a program which will find all numbers which are divisible by 7 but not multiple of 5, between 2000 and 3200
RETURN :
numbers obtained should be printed in a comma-separated sequence on a single line
"""


def find_number_divisible_and_not_multiply():

    list_of_found_numbers = []

    for i in range(2000, 3200):
        if (i % 7 == 0) and (i % 5 != 0):
            list_of_found_numbers.append(str(i))

    print(','.join(list_of_found_numbers))


find_number_divisible_and_not_multiply()


"""
USED METHOD :

RANGE: function witch two parameters (starting and ending sequence)
APPEND: add the  element to the end of the list 
JOIN: returning a str separator in sequence 

"""