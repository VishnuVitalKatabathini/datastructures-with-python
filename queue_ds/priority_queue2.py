#here we are going to implement the priority queue using the lists
q=[]
def enqueue(element):
    q.append(element)
    #here we are assigning the  priority as highest value as highest priority
    q.sort()

def dequeue():
    print('popped element ',q.pop())

while True:
    print('enter choice\n1.enqueue\n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        enqueue(int(input('enter element')))
    elif choice==2:
        dequeue()
    elif choice==3:
        print(q)
    elif choice==4:
        exit()
    else:
        print('enter valid input')