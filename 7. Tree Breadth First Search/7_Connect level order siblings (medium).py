class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def levelOrderSiblings(root):
    if root == None:
        return None
        
    # to maintain a list of nodes to be traversed
    # queue for first in and first out
    # queue = []
    queue = deque()
    # starting from root
    queue.append(root)

    while len(queue) != 0:
        # no. of nodes to be traversed in this iteration
        levelSize = len(queue)
        # to keep a track of prev pointer
        # when moving to next level, prev will be none
        prev = None

        for i in range(levelSize):
            # removing current node from the queue
            # currentNode = queue.pop(0)
            currentNode = queue.popleft()

            if(prev != None):
                prev.next = currentNode

            # that is current node is final node of current level
            if(i == levelSize - 1):
                currentNode.next = None

            # storing the children of current node in queue for future
            if(currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)

            prev = currentNode    

        # the current level ends here
    
    return root
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(levelOrderSiblings(root))