from collections import deque

def invertTree(root):
    # so basically do BFS, traverse every node
    # for every node, exchange its left and right subtrees
    # to exchange subtrees, just exchange the currentNode.left and currentNode.right
    
    if root == None:
        return root
    
    queue = deque()
    queue.append(root)
    
    while len(queue) != 0:
        level = len(queue)
        
        for _ in range(level):
            currentNode = queue.popleft()
            
            # so even if left or right node is not there i.e null
            # this still works
            # currentNode will never be null, since null is never added to queue
            temp = currentNode.left
            currentNode.left = currentNode.right
            currentNode.right = temp
            
            if currentNode.left != None:
                queue.append(currentNode.left)
                
            if currentNode.right != None:
                queue.append(currentNode.right)
                
    return root