#queue implementation using lists
#here we implemented using the append() and pop(0) 'deleteing at index 0' for enqueue and dequeue operation

queue =[]
def enqueue(element):
    queue.append(element)

def dequeue():
    print('dequeued element is ',queue.pop(0))

def display():
    print(queue)

while True:
    print('enter your choice \n1.enqueue\n2.dequeue\n3.display\n4.exit ')
    choice=int(input())
    if choice==1:
        enqueue(input('enter an element'))
    elif choice ==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        exit()
    else:
        print('invalid input...!')
