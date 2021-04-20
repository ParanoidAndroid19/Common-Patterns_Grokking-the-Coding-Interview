from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimumDepth(root):
    if root == None:
        return 0

    # to maintain a list of nodes to be traversed
    # queue for first in and first out
    # queue = []
    queue = deque()
    # starting from root
    queue.append(root)

    minDepth = 0

    while len(queue) != 0:
        # no. of nodes to be traversed in this iteration
        levelSize = len(queue)

        minDepth = minDepth + 1

        for _ in range(levelSize):
            # removing current node from the queue
            # currentNode = queue.pop(0)
            currentNode = queue.popleft()

            # storing the children of current node in queue for future
            if(currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)
            
            # when first leaf is encountered, that level is the min depth
            if(currentNode.left == None and currentNode.right == None):
                return minDepth

        # the current level ends here


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(minimumDepth(root))