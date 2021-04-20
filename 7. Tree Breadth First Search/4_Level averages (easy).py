from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelAverages(root):
    res = []

    if root == None:
        return res

    # to maintain a list of nodes to be traversed
    # queue for first in and first out
    # queue = []
    queue = deque()
    # starting from root
    queue.append(root)

    while len(queue) != 0:
        # no. of nodes to be traversed in this iteration
        levelSize = len(queue)
        # to store the sum of nodes at each level
        levelSum = 0

        for _ in range(levelSize):
            # removing current node from the queue
            # currentNode = queue.pop(0)
            currentNode = queue.popleft()
            # Adding to the sum
            levelSum = levelSum + currentNode.val

            # storing the children of current node in queue for future
            if(currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)

        # the current level ends here
        # levelSize is the total no. of nodes in the current level
        res.append(float(levelSum) / float(levelSize))

    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(levelAverages(root))