#here we are discussing the implementation of the stack using the queue module
#here we use the LIFOQUEUE type and put() for push operation and get() for pop operation
#here we can set the limit to the stack to store finite elements into it.
from queue import LifoQueue
stack=LifoQueue()
def display():
    print(stack.queue)
while True:
    print('enter choice \n1.push()\n2.pop()\n3.display()\n4.peek\n5.exit()')
    choice=int(input())
    if choice==1:
        stack.put(input('push an element into stack'))
    elif choice==2:
        print('popped element ',stack.get(timeout=1))
    elif choice==3:
        display()
    elif choice==4:
        print('top of the element is ',stack.queue[-1])

    elif choice==5:
        exit()
    else:
        print('enter a valid choice')

#but if we pop the last element and again trying to pop the empty stack the get() will go infinite
#so to avoid we use the parameter called 'timeout' parameter to avoid the infinite loop
#stack.get(timeout=1)1 in the sense 1 second program will terminate automatically

