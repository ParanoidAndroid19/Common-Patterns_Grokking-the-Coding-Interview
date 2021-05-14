from heapq import *

def k_freq(nums, k):
    freqs = {}
    minHeap = []
    res = []
    
    # recording the freq of each num in nums
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
        
    for num in freqs:
        # pushing tuple with freq first, so that minHeap is created
        # according to the frequency
        heappush(minHeap, (freqs[num], num))
        # if the length of minHeap exceeds k, then remove the smallest freq
        # that way only the top k freqs remain in the minHeap
        if len(minHeap) > k:
            heappop(minHeap)
            
    # pushing top k freq num to res list
    for pair in minHeap:
        res.append(pair[1])
        
    return res


print(k_freq([5, 12, 11, 3, 11], 2))