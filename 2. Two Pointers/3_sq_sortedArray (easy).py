def sq_sorted_array(arr):
    p1 = 0
    p2 = len(arr) - 1
    res = []
    
    if(arr[p1] >= 0):
        for num in arr:
            res.append(num**2)
    else:
        while(p1 <= p2):
            if(arr[p2]**2 >= arr[p1]**2):
                res.insert(0, arr[p2]**2)
                p2 = p2 - 1
            else:
                res.insert(0, arr[p1]**2)
                p1 = p1 + 1
            
    return res
    
print(sq_sorted_array([1, 2, 3]))