#here we are going to represent another form of 2-d array
#by using the list comprehension to create the 2d array
# it is same as what we did it in the 2d_array.py
#but here we are going to implement the list comprehension

import random
#that is we are appling the list comprehension inside the list itself

rows,cols=(3,4) #3 rows 4 cols
arr=[[0 for i in range(cols)] for j in range(rows)]
print(arr)
#initializing the array with random numbers

for row in range(rows):
    for col in range(cols):
        arr[row][col]=random.randint(0,10)

print(arr)
print('\n')
for row in range(rows):
    for col in range(cols):
        print('arr[{}][{}]'.format(row,col),arr[row][col],end=' ')
    print()

print(arr[0][1]) #element at 0th row and 1st column
