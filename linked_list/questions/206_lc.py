#Reverse Linked List

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        
class Solution:
    
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
                    
    def reverse (self):
        prev=None
        curr=self.head
        next=None
        
        while curr is not None:
            next=curr.next
            curr.next=prev
            
            prev=curr
            curr=next
            
        self.head=prev  
                  
    def display(self):
        temp=self.head
        while temp:
            print(temp.val, end="->") 
            temp=temp.next
        print("None")
        

sol=Solution()
sol.create(2)
sol.create(4)
sol.create(3)

# sol.reverse()

sol.display()                         