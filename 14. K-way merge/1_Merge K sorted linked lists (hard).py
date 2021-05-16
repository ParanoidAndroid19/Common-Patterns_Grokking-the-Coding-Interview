from heapq import *

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def printLL(head):
    curr = head
    st = ""
    while curr != None:
        st = st + str(curr.value) + "-->"
        curr = curr.next
    
    print(st + "||")


def mergeKLists(self, lists):
    minHeap = []
    # for result linked list
    resultHead = None
    resultTail = None

    # the linked lists are ordered
    # lists contains the root of all the k linked lists
    # pushing the root of all linked lists in minHeap, which would be the min
    # pushing (node.val, node) so that heap is arranged according to val
    for root in lists:
        if root != None:
            heappush(minHeap, (root.val, root))

    # keep popping the min from minHeap, and append to result linked list
    # Push the currentNode's next to minHeap
    # keep repeating till minHeap is empty
    while len(minHeap) > 0:
        # [1] cause the node is stored at index 1, (node.val, node)
        node = heappop(minHeap)[1]
        
        # if result LL is empty
        if resultHead == None:
            resultHead = resultTail = node
        
        # keeping it pointed to tail of LL, useful for appending to LL
        else:
            resultTail.next = node
            resultTail = resultTail.next
            
        # node.next push to minHeap
        if node.next != None:
            heappush(minHeap, (node.next.val, node.next))
            

    return resultHead



l1 = ListNode(5)
l1.next = ListNode(8)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(7)

mergeKLists([l1, l2])