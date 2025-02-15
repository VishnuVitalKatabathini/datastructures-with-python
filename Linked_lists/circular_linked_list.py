# here we are going to implement circular double linked list from scratch


# creating the node to build double linked list
class CreateNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


# creating double linked list
class Double_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # inserting a node at end of the list
    def insert_at_end(self):
        self.newnode = CreateNode(input('enter data to insert at end'))
        if self.head == None or self.tail == None:
            self.head = self.newnode
            self.tail = self.newnode
            self.tail.next=self.head
            self.head.prev=self.tail
            self.count += 1
        else:
            self.newnode.prev = self.tail
            self.tail.next = self.newnode
            self.tail = self.newnode
            self.tail.next=self.head
            self.head.prev=self.tail
            self.count += 1

    # inserting node at beginning of the list
    def insert_at_begin(self):
        self.newnode = CreateNode(input('enter data to insert at begin'))
        if self.head == None or self.tail == None:
            self.head = self.newnode
            self.tail = self.newnode
            self.tail.next=self.head
            self.head.prev=self.tail
            self.count += 1
        else:
            self.head.prev = self.newnode
            self.newnode.next = self.head
            self.head = self.newnode
            self.count += 1
            self.tail.next=self.head
            self.head.prev=self.tail

    # inserting node at specific position
    def insert_at_position(self):
        pos = int(input('enter position or location(1-n)  to insert data'))
        if self.head == None or self.tail == None:
            self.head = self.newnode
            self.tail = self.newnode
            self.tail.next=self.head
            self.head.prev=self.tail
            self.count += 1
        elif pos == 1:
            self.insert_at_begin()
        elif pos == self.count + 1:
            self.insert_at_end()
        else:
            self.newnode = CreateNode(input('enter data to insert at position {}'.format(pos)))
            self.temp = self.head
            for i in range(1, pos - 1):
                self.temp = self.temp.next
            self.newnode.next = self.temp.next
            self.newnode.prev = self.temp
            self.temp.next.prev = self.newnode
            self.temp.next = self.newnode
            self.count += 1
            self.tail.next=self.head
            self.head.prev=self.tail

    # delete node at end from the list
    def delete_at_end(self):
        if self.head == None or self.tail == None:
            print('list is  empty')
        else:
            self.temp = self.tail
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = self.head
            del self.temp

    # delete node at begin
    def delete_at_begin(self):
        if self.head == None or self.tail == None:
            print('list is empty')
        else:
            self.temp = self.head
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = self.tail
            self.count -= 1

    # delete node at specific position
    def delete_at_position(self):
        pos = int(input('enter the position(1-n) to delete'))
        if self.head == None or self.tail == None:
            print('list is empty')
        elif pos == 1:
            self.delete_at_begin()
        elif pos == self.count + 1:
            self.delete_at_end()
        else:
            self.temp = self.head
            for i in range(pos - 1):
                self.temp = self.temp.next
            self.temp.prev.next = self.temp.next
            self.temp.next.prev = self.temp.prev
            del self.temp
            self.count -= 1

    # reversing the double linked list
    def reverse_list(self):
        if self.tail == None:
            print('list is empty')
        else:
            self.temp = self.tail
            print('head<-->', end='')
            while self.temp.prev!=self.tail :
                print(self.temp.data, end='<-->')
                self.temp = self.temp.prev
            print(self.temp.data,end='<-->')
            print('null')

    # display the list
    def display(self):
        if self.head == None:
            print('list is empty')
        else:
            self.temp = self.head
            print('head<-->', end='')
            while self.temp.next!=self.head:
                print(self.temp.data, end='<-->')
                self.temp = self.temp.next
            print(self.temp.data,end='<-->')
            print('null')


dll = Double_linked_list()
while True:
    print('choose one from below\n1.insert_end\n2.display\n3.reverse_list\n4.insert_at_begin'
          '\n5.insert_at_position\n6.delete_at_end\n7.delete_at_begin\n8.delete_at_position\n9.exit')
    choice = int(input())
    if choice == 1:
        dll.insert_at_end()
    elif choice == 2:
        dll.display()
    elif choice == 3:
        dll.reverse_list()
    elif choice == 4:
        dll.insert_at_begin()
    elif choice == 5:
        dll.insert_at_position()
    elif choice == 6:
        dll.delete_at_end()
    elif choice == 7:
        dll.delete_at_begin()
    elif choice == 8:
        dll.delete_at_position()
    elif choice == 9:
        exit()
    else:
        print('invalid choice')


