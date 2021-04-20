class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderSuccessor(root, node):
    successor = False
    
    if root == None:
        return None
        
    queue = []
    queue.append(root)
    
    while len(queue) != 0:
        currentNode = queue.pop(0)
            
        if(currentNode.left != None):
            queue.append(currentNode.left)
        if(currentNode.right != None):
            queue.append(currentNode.right)
                
        if(currentNode.val == node):
            break
    
    # that is the node right after currentNode in the queue
    if len(queue) != 0:
        return queue[0].val
    else:
        return None
        
        
        
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(levelOrderSuccessor(root, 9))
