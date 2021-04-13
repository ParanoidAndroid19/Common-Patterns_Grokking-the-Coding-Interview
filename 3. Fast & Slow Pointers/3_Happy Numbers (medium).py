
# My Solution: Recursive approach

# dictSums = {}

# def happyNumbers(digits):
#     sqSum = 0
#     for d in digits:
#         sqSum = sqSum + d**2
    
#     if(sqSum == 1):
#         return True
        
#     elif dictSums.get(sqSum, 0) == 1:
#         return False
    
#     else:
#         dictSums[sqSum] = 1
#         # converting sqSum into arr of digits
#         sumStr = str(sqSum)
#         arr = []
#         for s in sumStr:
#             arr.append(int(s))
        
#         return happyNumbers(arr)
    

# print(happyNumbers([1, 9]))


# Solution 2: Given sol

def find_happy_number(num):
    slow = num
    fast = num
    
    while True:
        slow = find_sq_sum(slow)
        fast = find_sq_sum(find_sq_sum(fast))
        
        if(fast == slow):
            break
        
    return slow == 1
        
        
def find_sq_sum(num):
    sqSum = 0
    while num > 0:
        # get the last digit
        digit = num % 10 
        sqSum = sqSum + digit**2
        # remove the last digit
        num = num // 10
        
    return sqSum
    
print(find_happy_number(13))