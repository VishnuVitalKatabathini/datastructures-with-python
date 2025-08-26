#creating an empty matrix or another way of declaring or representing the matrix


#declaring the no.of rows and no.of columns
no_of_rows=3
no_of_cols=2
arr=[[0]*no_of_cols]*no_of_rows

for rows in range(no_of_rows):
    for cols in range(no_of_cols):
        arr[rows][cols] = int(input())


for rows in range(no_of_rows):
    for cols in range(no_of_cols):
        print(arr[rows][cols],end=' ')
    print()


#accessing the elements from this row
print(arr[0][0])#elment at 0th row and 0th column
print(arr[0])
#you have seen that elements of the are override at each time when loop runs
#this is because we are creating the multiple copies of the same row multiple times
#i.e. we are done at the starting of the program
#arr=[[0]*no_of_cols]*no_of_rows  this in the sense making copies of no_of_rows i.e.=3
# all these rows are identical or same
#this is acts as
#arr=[[0,0],[0,0],[0,0]] if we update one column let's say arr[0][1]
#it will be like
#arr=[[0,1],[0,1],[0,1]

#so this is not a good declaration the 2d_array