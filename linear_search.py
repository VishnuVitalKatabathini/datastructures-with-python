#linear search algorithm time complexity O(n)
from time import *
class Searching:
    @staticmethod
    def linear_search(arr,n,key):
        for i in range(n):
            if arr[i]==key:
                return i
            if i==n-1:
                return 'not found'

start_time=time()

ls=Searching()
#n=int(input('enter size of array'))
arr=[10,2,9,4,5,6,5,7,656,4,4,5,2,5,540,2,3,43,445,56,83,434,56,7,67,87,86,543,44,54,56,56,67,6,5,67,6,566]
#for i in range(n):
    #arr.append(int(input('enter a value')))

key=56
index_value=ls.linear_search(arr,len(arr),key)
print(index_value)
end_time=time()
print(end_time-start_time)
