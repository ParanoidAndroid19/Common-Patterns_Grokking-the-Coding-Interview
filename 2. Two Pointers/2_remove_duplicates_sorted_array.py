def remove_duplicates(arr):
    p1 = 0
    p2 = 1
    
    while(p2 <= len(arr) - 1):
        if(arr[p1] != arr[p2]):
            p1 = p2
            p2 = p2 + 1
            
        else:
            del arr[p2]
            
    return len(arr)
    
    
print(remove_duplicates([2, 2, 2, 11]))
