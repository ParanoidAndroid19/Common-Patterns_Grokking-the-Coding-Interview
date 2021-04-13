class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def hasCycle(link):
    slow = link
    fast = link
    
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        
        if(fast == slow):
            return True
            
    return False


def findCycleLength(slow):
    current = slow
    cycle_len = 0
    
    while True:
        current = current.next
        cycle_len = cycle_len + 1
        if(current == slow):
            break
    
    return cycle_len


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next
print(hasCycle(head))