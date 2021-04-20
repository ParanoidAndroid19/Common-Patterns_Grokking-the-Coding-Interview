class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def zigZagTraversal(root):
    res = []
    if root == None:
        return res
    
    # so first in and first out    
    queue = []
    # starting from root
    queue.append(root)

    # for alternating order
    leftToRight = True
    
    while len(queue) != 0:
        levelSize = len(queue)
        currentLevel = []
        
        for _ in range(levelSize):
            # getting it out of queue
            currentNode = queue.pop(0)
            # pushing the current node to current level
            # if leftToRight is true then append like usual
            if(leftToRight):
                currentLevel.append(currentNode.val)
            # if it's false then reverse, that is insert at start
            else:
                currentLevel.insert(0, currentNode.val)
            
            # kepping the current node's children in queue for future
            if(currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)
        
        # current level ends, pushing all the nodes in current level to res
        res.append(currentLevel)
        
        leftToRight = not leftToRight
        
    
    return res
            

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigZagTraversal(root))