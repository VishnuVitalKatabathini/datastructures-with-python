#here we implement the stack using the collection module
#we use deque() class of collection module to implement stack , we use the same
#append() for push and pop() for popping the element
from collections import deque
stack=deque()
def display():
    i=len(stack)-1
    while i>=0:
        print(stack[i])
        i=i-1

while True:
    print('enter your choice :')
    print('1.push()')
    print('2.pop()')
    print('3.display()')
    print('4.peek()')
    print('5.exit()')
    choice=int(input())
    if choice==1:
        stack.append(input('enter element to push '))
    elif choice==2:
        print('popped element :',stack.pop())
    elif choice==3:
        display()
    elif choice==4:
        print('top of the stack ',stack[-1])
    elif choice==5:
        exit()
    elif choice<=0 or choice>4:
        print('enter a valid choice')
