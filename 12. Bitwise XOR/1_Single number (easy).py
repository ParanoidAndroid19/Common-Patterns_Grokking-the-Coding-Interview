def singleNum(arr):
    single = arr[0]
    for i in range(1, len(arr)):
        single = single ^ arr[i]
        
    return single
    

print(singleNum([7, 9, 7]))