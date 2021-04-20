class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

def reverseLL(head):
    current = head
    prev = None
    
    while current != None:
        # temporarily store the next node
        temp = current.next
        if(temp == None):
            newHead = current
        
        # reversing the current node
        current.next = prev
        
        # updating prev node
        prev = current
        # moving to next node
        current = temp
        
    return newHead
    

def printLL(head):
    curr = head
    st = ""

    while curr != None:
        st = st + str(curr.data) + "-->"
        curr = curr.next
        
    print(st + "||")
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

printLL(head)

printLL(reverseLL(head))
