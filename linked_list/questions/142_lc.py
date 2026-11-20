#142. Linked List Cycle II

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
    
    def detectCycle(self):
        slow=self.head
        fast=self.head
        isCycle=False
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                isCycle=True
                break   
        if isCycle == False:
            return None
        slow=self.head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow             
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

ll=LinkedList()
ll.create(3)
ll.create(2)
ll.create(0)
ll.create(-4)

# Create cycle at index 1
second_node = ll.head.next

last_node = ll.head

while last_node.next is not None:
    last_node = last_node.next

last_node.next = second_node

# Detect cycle
result = ll.detectCycle()

if result:
    print("Cycle starts at:", result.data)
else:
    print("No cycle found")
# ll.display()                                           