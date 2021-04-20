class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

def reverseSublist(head, p, q):
    if(p==q):
        return head
        
    i = 1
    current = head
    prev = None
    
    # skip all nodes before p
    while current != None and i < p:
        prev = current
        current = current.next
        i = i + 1
        
    # useful later for connecting the sublist to the list
    # prev is at p - 1
    node_before_sublist = prev
    # as of now, current is p 
    last_node_sublist = current
    
    temp = None
    
    # reversing nodes b/w p and q
    while current != None and i <= q:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        i = i + 1
    
    # connecting to the front
    if node_before_sublist != None:
        # prev is now the first node of sublist, prev is at q
        node_before_sublist.next = prev
    # this means p == 1
    else:
        head = prev
        
    # connecting to the last part, current is at q + 1
    last_node_sublist.next = current
    
    return head
    

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

printLL(reverseSublist(head, 2, 4))
