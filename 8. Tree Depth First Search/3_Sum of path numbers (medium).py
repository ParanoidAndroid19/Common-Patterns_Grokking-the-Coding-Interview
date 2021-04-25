class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def getTotalSum(node, psum):
    # return 0 so that in the final return line, it's int + int 
    if node == None:
        return 0
    
    # since the node can have 0-9 val only, doing *10 is enough
    psum = psum*10 + node.val
    
    # base condition, if leaf node, return int path number
    if node.left == None and node.right == None:
        return psum
        
    # traverse left and right subtree, end goal if to add path num 
    # of all root-to-left paths.
    # To understand better take a small example of root and two children
    return getTotalSum(node.left, psum) + getTotalSum(node.right, psum)
        

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)
print(getTotalSum(root, 0))
