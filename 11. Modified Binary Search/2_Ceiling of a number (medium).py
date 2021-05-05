# my sol
# def ceilingNumber(arr, key):
#     first = 0
#     last = len(arr) - 1
#     smallest = -1
    
#     while first <= last:
#         mid = (first+last)//2
        
#         if key == arr[mid]:
#             return mid
        
#         if (key < arr[mid]):
#             # return mid
#             if(arr[mid] <= arr[smallest]):
#                 smallest = mid
        
#         # reduce search range
#         if key > arr[mid]:
#             first = mid + 1
#         else:
#             last = mid - 1
    
    
#     return smallest


# Ceiling of number
# Find smallest element in array greater than or equal to the ‘key’
def ceilingNumber(arr, key):
    # if key is bigger than the biggest element
    if(key > arr[-1]):
        return -1
        
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        mid = (first+last)//2
        
        if(key == arr[mid]):
            return mid
        
        elif(key < arr[mid]):
            last = mid - 1
            
        else:
            first = mid + 1
    
    # since the loop is running until 'first <= last', so at the end of the while loop, 'first == last+1'
    # we are not able to find the element in the given array, so the next big number will be arr[start]
    return first
    
    
print(ceilingNumber([1, 3, 8, 10, 15], 12))
