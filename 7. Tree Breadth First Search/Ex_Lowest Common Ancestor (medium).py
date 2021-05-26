from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def LCA(root, p, q):
    # first using breadth first search to populate parents dictionary
    queue = deque()
    queue.append(root)
    
    # key is node and val is node's parent
    parent = {root: None}
    
    # keep iterating until both p and q are found
    while p not in parent or q not in parent:
        level = len(queue)
        
        for _ in range(level):
            currentNode = queue.popleft()
            
            if currentNode.left != None:
                parent[currentNode.left] = currentNode
                queue.append(currentNode.left)
                
            if currentNode.right != None:
                parent[currentNode.right] = currentNode
                queue.append(currentNode.right)
    
    
    pAncestors = set()
    # finding all the ancestors of p by going up the tree using
    # parents dictionary, loop ends after reaching root
    while p != None:
        pAncestors.add(p)
        p = parent[p]

    # similarly going through ancestors of q, since direction is
    # q to root, the first time q's ancestor in pAncestors is the LCA
    while q not in pAncestors:
        q = parent[q]
        
    return q


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(LCA(root, root.left.left, root.left.right))