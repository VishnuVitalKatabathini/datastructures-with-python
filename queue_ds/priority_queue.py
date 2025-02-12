#here we are going to implement the priorityqueue
#priority queue can be implemented in two ways
#1 using list by sorting according to the priority or by taking the
# list values as tuple with the priority ad the actual value
#2 using the priorityqueue class of queue module

#here we are going to implement the queue using the priority queue  class
from queue import PriorityQueue


q=PriorityQueue()
#bydefault priorityqueue will consider the lowest values as highest priority
def enqueue(element):
    q.put(element)

def dequeue():
   print('popped element ', q.get())

while True:
    print('enter choide \n1.enqueue\n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        enqueue(int(input('enter element')))
    elif choice==2:
        dequeue()
    elif choice==3:
        print(q.queue)
    elif choice==4:
        exit()
    else:
        print('invalid input...!')


