class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def create(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
            
    def del_first(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            temp=self.head
            self.head=temp.next
            temp=None            
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

ll=LinkedList()
ll.create(23)
ll.create(12)
ll.create(34)
ll.create(28)

ll.del_first()

ll.display()
                                       