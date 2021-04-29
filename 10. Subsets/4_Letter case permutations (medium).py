def stringPermutations(strr):
    perms = []
    perms.append(strr)
    
    # processing every char of the string one by one
    for i in range(len(strr)):
        # do following only if char is alpha
        if strr[i].isalpha():
            # recording len before, since ele will be added to perms
            n = len(perms)
            # using all previous perms to create new perms for ith char
            for j in range(n):
                # converting to list cause str is immutable
                newPerm = list(perms[j])
                # for ith char
                newPerm[i] = newPerm[i].swapcase()
                # back to str and append finally to perms
                perms.append(''.join(newPerm))
    
    return perms

print(stringPermutations("ab7c"))