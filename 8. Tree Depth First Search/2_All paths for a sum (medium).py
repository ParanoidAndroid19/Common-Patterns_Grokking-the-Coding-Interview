class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathsSum(node, sum):
    allPaths = []
    recursiveSum(node, sum, [], allPaths)
    return allPaths
    

def recursiveSum(node, sum, currentPath, allPaths):
    if node == None:
        return
    
    # add current node to the path
    currentPath.append(node.val)
    
    # success condition
    if node.val == sum and node.left == None and node.right == None:
        allPaths.append(list(currentPath))

    else:
        # traverse left subtree
        recursiveSum(node.left, sum - node.val, currentPath, allPaths)
        # traverse right subtree
        recursiveSum(node.right, sum - node.val, currentPath, allPaths)
        
    # remove the current node from path to backtrack
    # removing it while we go up the recursive call stack
    del currentPath[-1]


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.right = TreeNode(7)
print(allPathsSum(root, 12))
