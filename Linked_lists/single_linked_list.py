#here we are going to implement single linked list from scratch

#1.creating the node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#2.creating the linked list
class SingleLinkedList:
    def __init__(self):
        self.head=None
        self.count=0

    # 1.inserting newnode at end of the list
    def insert_at_end(self):
        self.newnode=Node(input('enter data'))
        if self.head==None:
            self.head=self.newnode
            self.count+=1
        else:
            self.temp=self.head
            while self.temp.next!=None:
                self.temp=self.temp.next
            self.temp.next=self.newnode
            self.count+=1

    #2.inserting newnode at beginning of the list
    def insert_at_begin(self):
        self.newnode=Node(input('enter data to add beginning of the list'))
        if self.head==None:
            self.head=self.newnode
        else:
            self.newnode.next=self.head
            self.head=self.newnode
            self.count+=1

    #3. insert newnode at position specified by user
    def insert_at_position(self):
        pos = int(input('enter position to insert data'))
        if self.head==None:
            print("can't insert at position list is empty ")
        elif pos==1:
            self.insert_at_begin()
        elif pos > self.count+1:
            print("can't insert at this position since list is smaller than the position you want to insert")
            print(self.count,pos)
        else:
            self.newnode=Node(input('enter data to insert at {}'.format(pos)))
            self.temp=self.head
            for i in range(1,pos-1):
                self.temp=self.temp.next

            self.newnode.next=self.temp.next
            self.temp.next=self.newnode
            self.count+=1

    #4.deleting a node at the end of the linked list
    def delete_at_end(self):
        if self.head==None:
            print('linked list is empty unable to perform deletion operation')
        else:
            self.temp=self.head
            if self.head.next==None:
                 self.head=None
                 del self.temp
                 self.count-=1
            else:
                self.node = None
                while self.temp.next!=None:
                    self.node=self.temp
                    self.temp=self.temp.next
                self.node.next=None
                print('deletion at end successful ')
                del self.temp
                self.count-=1

    #5. deleting a node at beginning of the linked list
    def delete_at_begin(self):
        if self.head==None:
            print("list is empty can't perform delete operation")
        else:
            self.temp=self.head
            self.head=self.head.next
            self.temp.next=None
            self.count-=1

    #6.delete a node at particular position
    def delete_at_position(self):
        if self.head==None:
            print("linked list is empty can't perform delete operation")
        else:
            pos=int(input('enter position to delete'))
            if pos==1:
                self.delete_at_begin()
            else:
                self.temp=self.head
                self.x=self.head
                for i in range(pos-1):
                    self.x=self.temp
                    self.temp=self.temp.next
                self.x.next=self.temp.next
                self.temp.next=None
                del self.temp
                self.count-=1

    #7.printing the linked list
    def display(self):#
        if self.head==None:
            print('list is empty ')
        else:
            print('head ->',end='')
            self.temp=self.head
            while self.temp!=None:
                print(self.temp.data,end='->')
                self.temp=self.temp.next
            print('null')

    #8. reversing the linked list
    def reverse_list(self):
        if self.head==None:
            print('linked list is empty')
        else:
            self.temp=self.head
            self.current=self.head
            self.previous=None
            while self.temp!=None:
                self.temp=self.temp.next
                self.current.next=self.previous
                self.previous=self.current
                self.current=self.temp

            self.head=self.previous

#main starting from here
sll=SingleLinkedList()
while True:
    print('enter choice\n1.insert_at_end\n2.display'
          '\n3.insert_at_begin\n4.insert_at_position'
          '\n5.delete_at_end\n6.delete_at_begin\n7.delete_at_position\n8.reverse_list\n9.exit')
    choice=int(input())
    if choice==1:
        sll.insert_at_end()
    elif choice==2:
        sll.display()
    elif choice==3:
        sll.insert_at_begin()
    elif choice==4:
        sll.insert_at_position()
    elif choice==5:
        sll.delete_at_end()
    elif choice==6:
        sll.delete_at_begin()
    elif choice==7:
        sll.delete_at_position()
    elif choice==8:
        sll.reverse_list()
    elif choice==9:
        exit()
    else:
        print('enter a valid choice..!')