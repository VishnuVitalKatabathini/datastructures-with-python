#here we are going to implement the queue using heapq module
#here by default  heapq will implement the min heap smallest element will remove  first

#here we use heappush() and heappop() for enqueue and dequeue operation
#heappush will take two paramaeters 1 queue and another one is element that is enter into queue
import heapq

q=[]
def enqueue(element):
    heapq.heappush(q,element)

def dequeue():
    print('dequeued element ',heapq.heappop(q))

while True:
    print('enter choice \n1.enqueue\n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        enqueue(input('enter element'))
    elif choice==2:
        dequeue()
    elif choice==3:
        print(q)
    elif choice==4:
        exit()
    else:
        print('enter valid input')
