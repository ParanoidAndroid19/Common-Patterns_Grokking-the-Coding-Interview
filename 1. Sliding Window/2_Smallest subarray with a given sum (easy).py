# Smallest contiguous subarray whose sum is greater than or equal 
# to ‘S’
# return the length of smallest subarray, if there is no such subarray then
# return 0

def smallestSubarray(S, arr):
    windowStart = 0
    windowSum = 0
    minWindowLen = 10**5

    for windowEnd in range(0, len(arr)):
        windowSum = windowSum + arr[windowEnd]

        # keep on shrinking the window by removing the windowStart, 
        # to get the smallest subarray
        while(windowSum >= S):
            minWindowLen = min(minWindowLen, windowEnd - windowStart + 1)

            # subtracting the windowStart and then moving it by 1
            windowSum = windowSum - arr[windowStart]
            windowStart = windowStart + 1
    
    if(minWindowLen == 10**5):
        return 0
    
    return minWindowLen

print(smallestSubarray(7, [2, 1, 5, 2, 3, 2]))