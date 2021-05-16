from heapq import *

def KthSmallest(nums, k):
    maxHeap = []
    
    for num in nums:
        heappush(maxHeap, -num)
        
        if len(maxHeap) > k:
            heappop(maxHeap)
            
    return -maxHeap[0]
    
    
print(KthSmallest([5, 12, 11, -1, 12], 3))