class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

def checkCycle(link):
    slow = link
    fast = link
    
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        
        if(fast == slow):
            return cycleLength(slow)
            
    return False
    

def cycleLength(slow):
    current = slow
    cycleLen = 0
    
    while True:
        current = current.next
        cycleLen = cycleLen + 1
        
        if(current == slow):
            break
        
    return cycleLen
    

def findStartCycle(head, cycleLen):
    p1 = head
    p2 = head
    
    while cycleLen > 0:
        p2 = p2.next
        cycleLen = cycleLen - 1
        
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
            
    return p1.data
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next

cycleLen = checkCycle(head)
print(cycleLen)    
print(findStartCycle(head, cycleLen))
