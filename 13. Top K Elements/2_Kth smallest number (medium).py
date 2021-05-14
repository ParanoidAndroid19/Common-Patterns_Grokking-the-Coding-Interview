from heapq import *

def Kth_Smallest(nums, k):
    maxHeap = []
    
    for i in range(0, len(nums)):
        # to have at least k numbers in heap
        if i < k:
            heappush(maxHeap, -nums[i])
    
        # since we want the Kth smallest number, don't insert numbers
        # greater than root of maxHeap (which is the largest number in heap so far)
        # it's > because -ve sign
        elif(-nums[i] > maxHeap[0]):
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])
            
    # at the root of the heap will be Kth smallest number
    return -maxHeap[0]

print(Kth_Smallest([1, 5, 12, 2, 11, 5], 3))