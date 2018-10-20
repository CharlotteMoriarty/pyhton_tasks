"""
With a given integral number n, write a program to generate dictionary that contain (i , i* i )
Return example :
for input 8 output should be:
{1:1, 2:4,3:9, 4:16, 5:25, 6:36, 7:49, 8:64}
"""
n = int(input("How long dictionary do you want to generate? : "))


def find_dictionary(n):
    numbers = {}

    for i in range(1,n+1):
        numbers[i] = i * i
    print(numbers)


find_dictionary(n)

"""
USED METHOD :
RANGE: function witch two parameters (starting and ending sequence)


*dictionary doesn't have a append method !! *

* WHAT IS GOING ON : *
input "n"  = > how many keys dictionary will get
create a function with n argument
create a empty dictionary
for loop in range from 1 to n + 1
    number[key] = value
    
"""