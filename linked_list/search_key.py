class Node:
    def __init__(self, val):
        self.val=val
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
            
    def search(self, key):
        temp=self.head   
        i=0
        while temp is not None:
            if temp.val==key:
                return i
            temp=temp.next
            i+=1
        return -1      
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.val, end="->")
            temp=temp.next
        print("None") 

ll=LinkedList()

ll.create(3)
ll.create(12)
ll.create(6)
ll.create(7)
ll.create(13)

print(ll.search(6))

ll.display()                                          