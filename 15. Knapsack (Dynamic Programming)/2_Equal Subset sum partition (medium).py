def canPartition(nums):
    # sum of all nums in i/p list
    ssum = sum(nums)
    
    # if sum is not even then equal partition cannot exist
    if ssum % 2 != 0 or len(nums) == 0:
        return False
    
    memo = {}
    
    return recursive_partition(memo, nums, ssum/2, 0)
    
    
def recursive_partition(memo, nums, ssum, currentIndex):
    # success condition
    if ssum == 0:
        return True
    
    # checks
    if currentIndex >= len(nums):
        return False
    
    # memoization
    if (currentIndex, ssum) not in memo:
        # including num at currentIndex
        if nums[currentIndex] <= ssum:
            if(recursive_partition(memo, nums, ssum - nums[currentIndex], currentIndex + 1)):
                memo[currentIndex, ssum] = True
                return True

        # excluding num at currentIndex
        memo[currentIndex, ssum] = recursive_partition(memo, nums, ssum, currentIndex + 1)
    
    
    return memo[currentIndex, ssum]
    
    
print(canPartition([1, 2, 3, 4]))