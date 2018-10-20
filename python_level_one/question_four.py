"""
Write a program which accepts a sequence pf comma-separated numbers from console and generate a list and a tuple which
contains every number.
Return:
    list
    tuple
"""


def convert_for_list_and_tuple():

    user_input = input("Write a sequence of number: ")
    your_list = list(user_input.split(","))
    print(your_list)

    # your_tuple = tuple(user_input.split(","))
    # or
    your_tuple = tuple(your_list)
    print(your_tuple)


convert_for_list_and_tuple()

"""
USED METHOD :
SPLIT  add the  element to the end of the list

* WHAT IS GOING ON : *
crate a function
create variable for user numbers input
create a list from the split user numbers
print list
crate a tuple from the split user numbers
print a tuple

"""