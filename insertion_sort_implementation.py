class Insertionsort:
    @staticmethod
    def ins_sort(arr,n):

        for i in range(1,n):
            j=i-1
            key=arr[i]
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=key
        return arr

ins=Insertionsort()
n=int(input('enter array elements'))
lst=[]
for i in range(n):
    lst.append(int(input('enter element')))
print(lst)
lst=ins.ins_sort(lst,n)
print(lst)


