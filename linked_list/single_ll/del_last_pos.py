class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def create(self, val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
            
    def del_last(self):
        if self.head is None:
            print("Empty linked list")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None                
    
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
ll=LinkedList()
ll.create(4)
ll.create(33)
ll.create(25)
ll.create(13)

ll.del_last()

ll.display()                                
                