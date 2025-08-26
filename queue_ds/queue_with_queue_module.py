#here we are going to implement the queue using the queue module Queue()class
from collections import deque
from queue import Queue

q=Queue(5) #here we can specify the size of the queue optional
def enqueue(element):
    #q.put(element,block=True,timeout=1)
    #q.put(element) # it has generally three parameters as above if the queue is full this will go infinite
    #but if you keep the timeout=soome finite seconds it will terminate the program
    q.put_nowait(element) # here put_nowait() will automatically terminate the program if queue is full

def dequeue():
   # q.get(block=True,timeout=2)
   # print('dequeued element is ',q.get())#here get() has also three parameters as above
    #it will go infinte if the queue is empty so of we keep the
   # timeout parameter to 1 second it will terminate the program in 1 second
   #we can also use the get_nowait() it will directly terminate the program if queue is empty
   print('dequeued element ',q.get_nowait())

while True:
    print('enter choice\n1.enqueue \n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        enqueue(input('enter element'))
    elif choice==2:
        dequeue()
    elif choice==3:
        print(q.queue)
    elif choice==4:
        exit()
    else:
        print('enter a valid choice')







