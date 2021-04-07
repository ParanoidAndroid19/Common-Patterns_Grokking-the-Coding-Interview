def avgSubarrays(nums, k):
    res = []
    # window starts from 0th element
    windowStart = 0
    windowSum = 0
    
    for windowEnd in range(0, len(nums)):
        # in that start only this line will execute till Kth element is reached
        # so we have our first window sum
        # as the window slides, we keep on adding the next element
        windowSum = windowSum + nums[windowEnd]
        
        # once we have the base sum of the first k elements, complete window
        if(windowEnd >= k - 1):
            # here we have the correct sum of a particular window
            res.append(windowSum/k)
            # as the window slides, we keep on subtracting the previous window start
            windowSum = windowSum - nums[windowStart]
            # update the window start for new window
            windowStart = windowStart + 1
    
    return res

print(avgSubarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))