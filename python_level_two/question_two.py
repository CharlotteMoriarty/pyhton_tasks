"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

"""


def i_have_no_idea():
    user_input = input("X, Y")
    user_input = user_input.replace(",", "")

    dim = []
    for x in user_input:
        x = int(x)
        dim.append(x)
    print("Your X and Y ", dim)

    row_number = dim[0]
    column_number = dim[1]

    multi_list = []
    for i in range(row_number):
        row = []
        for j in range(column_number):
            row.append(0)
        multi_list.append(row)

    for row in range(row_number):
        for column in range(column_number):
            multi_list[row][column] = row * column
    print(multi_list)


i_have_no_idea()
