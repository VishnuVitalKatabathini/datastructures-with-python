stack=[]
#this is a simple implementation of the stack in pyhton
#implementing stack using list built in functions
#append() and pop()
def push(element):
    stack.append(element)
def pop():
    print(stack.pop(-1))#poping the last element from the list called stack
def display():
    i=len(stack)-1
    while i>=0:
        print(stack[i])
        i=i-1

def peek():
    print('top of the stack ',stack[-1])

while True:
    print('enter your choice \n 1.push()\n2.pop()\n3.display()\n4.peek()\n5.exit()')
    choice=int(input())
    if choice==1:
        push(input('enter the element into stack'))
    elif choice==2:
        #print('popped element from stack: ',stack.pop())
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        exit()
    elif choice<=0 or choice>4:
        print('enter a valid choice')