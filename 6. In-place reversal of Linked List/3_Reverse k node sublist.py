class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

def reverseKSublist(head, k):
    current = head
    prev = None
    
    while True:
        
        i = 1
        node_before_sublist = prev
        last_node_sublist = current
        temp = None
        
        while current != None and i <= k:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i = i + 1
            
        # conneting to first part
        if node_before_sublist != None:
            node_before_sublist.next = prev
        else:
            head = prev
            
        # connect with next part
        last_node_sublist.next = current
        
        if current == None:
            break
        
        prev = last_node_sublist
        
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
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

printLL(head)

printLL(reverseKGroup(head, 3))