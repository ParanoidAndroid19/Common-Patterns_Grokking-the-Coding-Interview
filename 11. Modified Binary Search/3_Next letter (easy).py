# my sol
def smallestLetter(letters, key):
    
    arr = []
    arr.append(letters[0])
    
    # removing duplicates
    for i in range(1, len(letters)):
        # print(i)
        if(letters[i] != letters[i-1]):
            arr.append(letters[i])
    
    # circular array
    if(ord(key) >= ord(arr[-1]) or ord(key) < ord(arr[0])):
        return arr[0]
        
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        mid = (first+last)//2
        
        if(arr[mid] == key):
            return arr[mid+1]
            
        elif(ord(key) < ord(arr[mid])):
            last = mid - 1
            
        else:
            first = mid + 1
            
    return arr[first]
    
    
print(smallestLetter(["c","f","j"], 'g'))