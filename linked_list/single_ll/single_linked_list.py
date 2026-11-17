class Node:
    def __init__(self, info):
        self.info=info
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def create(self, info):
        new=Node(info)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new
    
    def display(self):
        temp=self.head
        while temp:
            if temp is not None:
                print(temp.info, end=" -> ")
                temp=temp.next
        print("None")    
                
ll=LinkedList()
ll.create(10) 
ll.create(20)
ll.create(30)
ll.create(40)                        

ll.display()