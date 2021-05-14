from heapq import *

# k closest numbers
# heap will be based on X - current number
# use minheap

def k_closest(nums, k, x):
    # to reduce the scope of our search, we'll use binary search
    # and consider the numbers k distance away from x, in both directions
    xIndex = binSearch(nums, x)
    start = xIndex - k
    end = xIndex + k
    
    start = max(start, 0)
    end = min(end, len(nums)-1)
    
    minHeap = []
    res = []
    
    for i in range(start, end+1):
        heappush(minHeap, (abs(x - nums[i]), nums[i]))
        
    for _ in range(k):
        res.append(heappop(minHeap)[1])
        
    res.sort()
        
    return res
        

def binSearch(nums, x):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low+high)//2
        
        if nums[mid] == x:
            return mid
            
        elif x < nums[mid]:
            high = mid - 1
            
        else:
            low = mid + 1
            
    if low > 0:
        return low - 1
    else:
        return low


print(k_closest([1,2,3,4,5], 4, 3))