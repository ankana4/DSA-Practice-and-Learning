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
                    
    def insert_1st_pos(self, info):
        new=Node(info)
        if self.head is None:
            self.head=new
        else:    
            new.next=self.head
            self.head=new

    def show(self):
        temp=self.head
        while temp:
            if temp is not None:
                print(temp.info, end=" -> ") 
                temp=temp.next
        print("None")
        
ll=LinkedList()   
ll.create(2)
ll.create(13)
ll.create(4)
ll.create(17)
ll.insert_1st_pos(3)  
ll.insert_1st_pos(34)  


ll.show()                       