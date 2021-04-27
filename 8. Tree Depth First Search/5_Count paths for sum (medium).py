class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countPaths(node, S, currentPath):
    if node == None:
        return 0
    
    # add the current node to the path
    currentPath.append(node.val)
    
    pathSum = 0
    pathCount = 0
    
    # find the sum of all subpaths in the current path list
    # we start from bottom (reverse iteration of currentPath,
    # so that lastest added node is considered first.
    # finding sums of all sub-paths ending at the current node
    # with every single node added to the currentPath this process is done
    for i in range(len(currentPath)-1, -1, -1):
        pathSum = pathSum + currentPath[i]
        # increment path count if matched sum
        if(pathSum == S):
            pathCount = pathCount + 1
            
    # traverse left and right subtree
    # returning pathCounts to keep a track of it
    pathCount = pathCount + countPaths(node.left, S, currentPath)
    pathCount = pathCount + countPaths(node.right, S, currentPath)
    
    # removing the currentNode from path while backtracking,
    # going up the call stack
    del currentPath[-1]
    
    return pathCount


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)
print(countPaths(root, 12, []))
