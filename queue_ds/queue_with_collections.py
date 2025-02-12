#here we are going to implement the queue data structure using the collection module
from collections import deque

queue =deque()
def enqueue(element):
    queue.append(element)

def dequeue():
    print('dequeued element is ',queue.popleft())

while True:
    print('enter the choice \n1.enqueue\n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        enqueue(input('enter element '))
    elif choice==2:
        dequeue()
    elif choice==3:
        print(queue)
    elif choice==4:
        exit()
    else:
        print('enter a valid input')


#here we have to types of append() appendleft() and append() and to types of pop() popleft and pop()
#appendleft() will simply append the element at left side of the deque or list
#append() will do append at right or general append() we can say
#here pop() will pop the last element
#popleft() will append the last element
# but the last element considered as left most element in the list
#example [1,2,3,4,5] the 1 at index 0 is considered as left most element
# and popleft will delete this left most element we should use the basic append() appending at right side
#if append() then -> popleft()
#if appendLeft() then -> pop() are to be implemented

