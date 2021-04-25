class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
# def pathRecur(node, seq, i):
#     if node == None:
#         return False
    
#     # if node matches the seq
#     if node.val == seq[i]:
#         # success condition is, node val matches seq[i] and 
#         # i is at last ele of seq leaf node 
#         if node.left == None and node.right == None and i == len(seq) - 1:
#             return True
        
#         # if seq matches but it's not least seq ele or leaf yet
#         else:
#             return pathRecur(node.left, seq, i+1) or pathRecur(node.right, seq, i+1)
            
#     return False


# given solution
def pathExists(root, seq):
    # if tree is empty and so is seq, then true
    if root == None:
        return len(seq) == 0
        
    return pathRecur(root, seq, 0)
    
    
def pathRecur(node, seq, i):
    if node == None:
        return False
    
    seqLen = len(seq)
    
    # i should not exceede length of seq, that means 
    # tree depth is bigger than seq, thus False
    # If anywhere in seq, node.val doesn't match, then False
    if i >= seqLen or node.val != seq[i]:
        return False
    
    # after above condition, node.val == seq[i]

    # success condition is, leaf node val matches seq[i] and 
    # i is at last ele of seq
    if node.left == None and node.right == None and i == seqLen - 1:
        return True
            
    # traverse left and right subtree
    return pathRecur(node.left, seq, i+1) or pathRecur(node.right, seq, i+1)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print(pathExists(root, [1, 1, 6]))
