from heapq import *

def findKLargest(nums, k):
    
    minHeap = []
    
    for i in range(0, len(nums)):
        # to have at least k numbers in heap
        if i < k:
            heappush(minHeap, nums[i])
            
        # since we want the largest k numbers, don't insert numbers
        # less than root of minHeap (which is the smallest number in heap so far)
        elif(nums[i] > minHeap[0]):
            heappop(minHeap)
            heappush(minHeap, nums[i])
            
            
    return minHeap


print(findKLargest([3, 1, 5, 12, 2, 11], 3))