from collections import deque

def topological_sort(vertices, edges):
    sortedOrder = []
    
    # vertex means node
    if vertices <= 0:
        return sortedOrder
    
    # for every degree the incoming edges (in-degree), 
    # like source (i.e root will have 0)
    inDegree = {i: 0 for i in range(vertices)}
    
    # for every vertex, a list of its children
    graph = {i: [] for i in range(vertices)}  
    
    # populate indegree and graph
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        # appending child to the parent's list of children
        graph[parent].append(child)
        # incrementing in-degree of child
        inDegree[child] = inDegree[child] + 1
        
    # find all the sources (i.e roots, having zero in-degree)
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
      
    # pop each source, and append to sortedOrder
    # and for every source, decrement it's children's inDegree
    # by one and if it becomes zero then append child to sources
    while len(sources) != 0:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] = inDegree[child] - 1
            if inDegree[child] == 0:
                sources.append(child)
                
                
    # if not equal then graph has a cycle in it
    if len(sortedOrder) != vertices:
        return []
        
    
    return sortedOrder


print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))