#l->left,r->right,q->middle
def merge(Arr,l,q,r):
    n1=q-l+1
    n2=r-q
    arr1=[]
    arr2=[]
    arr=[]
    for i in range(n1):
        arr1[i]=Arr[l+1]

    for i in range(n2):
        arr2[i]=Arr[q+i]

    i=1
    j=1
    while l<r:
        if arr1[i]<=arr2[i]:
            arr[l]=arr1[i]
            i+=1
        else:
            arr[l]=arr2[j]
            j+=1
    print(arr)



def merge_sort(Arr,l,r):
    if l<r:
        q=(l+r)/2
        merge_sort(Arr,l,q)
        merge_sort(Arr,l+1,r)
        merge(Arr,l,q,r)



arr=[1,2,3,1,2,9,5,23,4,6,2,4,2]
merge_sort(arr,0,len(arr)-1)