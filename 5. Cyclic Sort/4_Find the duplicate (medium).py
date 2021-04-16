# my solution

# def findDuplicate(arr):
#     i = 0
    
#     while i < len(arr):
#         # if number not in correct index
#         if arr[i] != i + 1:
#             val = arr[i]
#             # if duplicate, then return
#             if arr[i] == arr[val-1]:
#                 return arr[i]
#             # swap
#             else:
#                 arr[i], arr[val-1] = arr[val-1], arr[i]
#         else:
#             i = i + 1
    
# solution using fast and slow pointers, to detect the cycle in prob and return start of cycle

def findDuplicate(nums):
    # both start from same point
    slow = fast = nums[0]
    
    # phase 1
    # fast enters the loop first and then slow, fast is bound to intersect with slow
    # after loop ends both are at the intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # phase 2
    # setting slow at the start of array and fast is at the intersection point inside loop, 
    # and both pointers move at the same pace now
    # According to floyd's algo, F + a = nC, slow and fast will meet at the start of cycle
    # that would be duplicate number
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    # start of the cycle
    return fast


print(findDuplicate([3,1,3,4,2]))