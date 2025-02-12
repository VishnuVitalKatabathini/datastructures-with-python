#here we are going to implement the queue using the insert() instead of append()
#and pop()
queue=[]
while True:
    print('enter choice \n1.enqueue\n2.dequeue\n3.display\n4.exit')
    choice=int(input())
    if choice==1:
        queue.insert(0,input('enter element'))
    elif choice==2:
        print('dequeued element ',queue.pop())
    elif choice==3:
        print(queue)
    elif choice==4:
        exit()
    else:
        print('invalid input..!')