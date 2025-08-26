#here we are going to  implement the 2d array in python from scratch

arr=[[1,2,3],
     [4,5,6]] #this is a basic representation of the two array it is 2*3 array
print(arr)

#accessing the elements from the 2d array
print(arr[0][0])#element at 0th row and 0th column
print(arr[1][2])#element at 1st row and 2nd column
#total no.of row in the array
row_count=len(arr)#basically it is the length of the array
print('total rows',row_count)
#total no.of col in the array
col_count=len(arr[0])#it is the length of the first row
print('total columns in each row',col_count)

for rows in range(row_count):
    for cols in range(col_count):
        print('arr[{}][{}]='.format(rows,cols),arr[rows][cols],end=' ')

    print()

#transposing the array
print('transpose of a matrix')
for cols in range(col_count):
    for rows in range(row_count):
        print('arr[{}][{}]'.format(rows,cols),arr[rows][cols],end=' ')
    print()







