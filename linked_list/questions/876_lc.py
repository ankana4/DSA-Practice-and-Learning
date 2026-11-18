#876. Middle of the Linked List

#Brute-force approach
class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
    
class Solution:
    def __init__(self):
        self.head=None
        
    def create(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def middle(self):
        size=0
        temp=self.head
        
        while temp is not None:
            size+=1
            temp=temp.next
        mid=size//2+1
        
        temp=self.head
        for i in range(1, mid):
            temp=temp.next
        return temp
    
    def show(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None") 
        
sol=Solution()
sol.create(1)
sol.create(2)
sol.create(3)
sol.create(4)
sol.create(5)
sol.create(6)

middle_node= sol.middle()
print(middle_node.data)
sol.show()              


#Better Approach
class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
    
class Solution:
    def __init__(self):
        self.head=None
        
    def create(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
    def middle(self):
        slow=self.head
        fast=self.head
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
        return slow    
        
    def show(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None") 
        
sol=Solution()
sol.create(1)
sol.create(2)
sol.create(3)
sol.create(4)
sol.create(5)
sol.create(6)

middle_node= sol.middle()
print(middle_node.data)
sol.show()              
