def findComplement(num):
    # counting the no. of bits required to represent num (i.e 8 requires 
    # 4 bits, 1000. 7 requires 3 bits 111)
    n = num
    bit_count = 0
    
    while n > 0:
        bit_count = bit_count + 1
        # left shifting n to reduce it
        n = n >> 1
        
    # The decimal number for all bits set of length bit_count, 
    # eg: pow(2, 4) - 1 = 16 - 1 = 15 (1111)
    all_bits_set = pow(2, bit_count) - 1
    
    if(num == 0):
        return 1
    
    return num ^ all_bits_set
    

print(findComplement(2))