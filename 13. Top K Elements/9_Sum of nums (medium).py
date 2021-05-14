from heapq import *

def sumOfEles(nums, k1, k2):
    minHeap = []
    ssum = 0
    
    # first insert all numbers in minHeap
    for num in nums:
        heappush(minHeap, num)
        
    # pop numbers from minHeap one by one
    # add nums falling b/w k1 and k2
    for i in range(1, len(nums)+1):
        temp = heappop(minHeap)
        
        if k1 < i and i < k2:
            ssum = ssum + temp
            
    return ssum
    
print(sumOfEles([3, 5, 8, 7], 1, 4))