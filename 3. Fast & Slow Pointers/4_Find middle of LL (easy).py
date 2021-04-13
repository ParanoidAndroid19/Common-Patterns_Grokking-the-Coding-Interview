class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

# solution 1: my brute force sol

# def find_middle(head):
#     p1 = head
#     p2 = head
#     ll_len = 0
#     half = 0
    
# 	 # find length of LL
#     while p1 != None:
#         ll_len = ll_len + 1
#         p1 = p1.next
        

#     # find middle node
#     while half != (ll_len//2):
#         half = half + 1
#         p2 = p2.next
        
#     return p2.data

# Solution 2: given sol

def find_middle(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    return slow.data


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(find_middle(head))
