from heapq import *

def freqSort(strr):
    freqs = {}
    maxHeap = []
    res = ""
    
    # recording freqs of all chars
    for char in strr:
        freqs[char] = freqs.get(char, 0) + 1
        
    # add all the chars and their freq to the max heap
    # freq first in tuple so that heap is arranged according to it
    for char in freqs:
        heappush(maxHeap, (-freqs[char], char))
        
    # pop the max freq char and append it to the resultant string
    while len(maxHeap) != 0:
        pair = heappop(maxHeap)
        res = res + pair[1]*(-pair[0])
        
    return res


freqSort("Programming")