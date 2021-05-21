from collections import deque

def scheduleTasks(n, tasks):
    sortedOrder = []
    
    # inDegree
    inDegree = {i: 0 for i in range(0, n)}
    # graph
    graph = {i: [] for i in range(0, n)}
    
    # populating
    for taskPair in tasks:
        parent = taskPair[0]
        child = taskPair[1]
        graph[parent].append(child)
        inDegree[child] = inDegree[child] + 1
        
    # queue of sources
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
            
    # ordering
    while len(sources) != 0:
        task = sources.popleft()
        sortedOrder.append(task)
        for child in graph[task]:
            inDegree[child] = inDegree[child] - 1
            if inDegree[child] == 0:
                sources.append(child)
                
                
    # check if topological sort is possible or does graph have cycle
    if len(sortedOrder) != n:
        return False
        
    return True
    
    
print(scheduleTasks(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))