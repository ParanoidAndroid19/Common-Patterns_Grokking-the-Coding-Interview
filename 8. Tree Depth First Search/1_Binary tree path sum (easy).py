class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def findPathSum(node, sum):
    if node == None:
        return False
    
    # success condition, current node is leaf and it's val is such
    # that when subtracted from sum, sum will be 0 
    if node.val == sum and node.left == None and node.right == None:
        return True
    
    # recursive call to traverse left and right subtree
    # return true if any of the recursive call returns true
    return findPathSum(node.left, sum - node.val) or findPathSum(node.right, sum - node.val)

# or

# def rootToLeaf(node, sum, res):
#     if node == None:
#         return False
        
#     if node.left == None and node.right == None:
#         if node.val == sum:
#             res.append(node.val)
#             return True
#         else:
#             return False
            
#     if rootToLeaf(node.left, sum - node.val, res):
#         res.append(node.val)
#         return True
    
#     if rootToLeaf(node.right, sum - node.val, res):
#         res.append(node.val)
#         return True
        
#     return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
findPathSum(root, 10)
