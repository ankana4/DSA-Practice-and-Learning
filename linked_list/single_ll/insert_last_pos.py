class Node:
    def __init__(self, info):
        self.data=info
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_last_pos(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

ll=LinkedList()
ll.insert_last_pos(5)
ll.insert_last_pos(3)
ll.insert_last_pos(8)

ll.display()                                    
                    
                