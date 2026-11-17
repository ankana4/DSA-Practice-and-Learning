class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def create(self, val):
        new=Node(val)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new
           
    def insert_at_mid(self, data, pos):
        if pos<0:
            print("Invalid position")
            return
        
        new=Node(data)
        if pos==0:
            new.next=self.head
            self.head=new
            return 
        
        temp=self.head
        for i in range(0, pos-1):
            if temp is None:
                print("Invalid Position")
                return
            temp=temp.next 
        if temp is None:
            print("Invalid Position")
            return
        new.next=temp.next
        temp.next=new
                    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
ll=LinkedList()

ll.create(3)
ll.create(5)
ll.create(6)
ll.create(2)

ll.insert_at_mid(12, 5)
ll.display()                    