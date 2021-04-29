from collections import deque

def permutations(nums):
    res = []
    # using deque since will be using popleft()
    perms = deque()
    perms.append([])
    numsLen = len(nums)
    
    # to iterate through the nums list
    for num in nums:
        # recording it before, since through the next loop, more 
        # ele are appended to perms
        n = len(perms)
        # iterate through all the permutations in the queue
        for _ in range(n):
            # consider first perm in the perms queue
            oldPerm = perms.popleft()
            # iterate through all the positions in the oldPerm
            # for eg. 0, 1, 2, 3, ...
            # +1 since we will adding another num in the oldPerm
            for j in range(0, len(oldPerm)+1):
                # not using oldPerm since the loop depends on its len
                newPerm = list(oldPerm)
                # inserting the new num in every position
                newPerm.insert(j, num)
                # That means the perm is ready, no more scope for
                # insertion, thus finally append to res
                if len(newPerm) == numsLen:
                    res.append(newPerm)
                # If not then that means more insertions can be done
                # thus add it to the perms queue
                else:
                    perms.append(newPerm)
    
    return res


print(permutations([1, 3, 5]))