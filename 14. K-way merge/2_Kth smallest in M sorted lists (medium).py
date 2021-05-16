from heapq import *

def kthSmallest(lists, k):
    minHeap = []
    # result = []
    counter = 0
    
    # lists consists of M sorted lists
    # adding first num from all lists to minHeap, along with
    # corresponding index and list
    # heap will be ordered according to val
    for li in lists:
        val = li[0]
        heappush(minHeap, (val, 0, li))
        
    while len(minHeap) > 0:
        liData = heappop(minHeap)
        
        # so if we want the 5th smallest num, it will be at index 4
        if counter < k-1:
            # result.append(liData[0])
            counter = counter + 1
            
            nextLi = liData[2]
            i = liData[1] + 1
            if i < len(nextLi):
                heappush(minHeap, (nextLi[i], i, nextLi))
        
        # when counter = k - 1         
        else:
            return liData[0]
        
        
    return result
    

print(kthSmallest([[5, 8, 9], [1, 7]], 3))