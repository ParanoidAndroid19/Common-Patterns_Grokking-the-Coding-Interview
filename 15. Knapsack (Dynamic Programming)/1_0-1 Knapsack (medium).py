# Brute force, recursive only solution

# def solveKnapsack(profits, weights, capacity):
#     return recursiveKnapsack(profits, weights, capacity, 0)
    
    
# def recursiveKnapsack(profits, weights, capacity, currentIndex):
#     # base condition check
#     if capacity <= 0 or currentIndex >= len(profits):
#         return 0
        
#     # recursive call after chooing the element (profit and weight) at currentIndex
#     # consider element at currentIndex only if it's weight is less than or equal to capacity
#     profit1 = 0
#     if weights[currentIndex] <= capacity:
#         profit1 = profits[currentIndex] + recursiveKnapsack(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
        
#     # recursive call after excluding the element at currentIndex
#     profit2 = recursiveKnapsack(profits, weights, capacity, currentIndex + 1)
    
#     return max(profit1, profit2)



# Top-down Dynamic Programming with Memoization

def solveKnapsack(profits, weights, capacity):
    memo = {}
    return recursiveKnapsack(memo, profits, weights, capacity, 0)
    
    
def recursiveKnapsack(memo, profits, weights, capacity, currentIndex):
    # base condition check
    if capacity <= 0 or currentIndex >= len(profits):
        return 0
        
    if (currentIndex, capacity) in memo:
        return memo[currentIndex, capacity]
        
    # recursive call after chooing the element (profit and weight) at currentIndex
    # consider element at currentIndex only if it's weight is less than or equal to capacity
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + recursiveKnapsack(memo, profits, weights, capacity - weights[currentIndex], currentIndex + 1)
        
    # recursive call after excluding the element at currentIndex
    profit2 = recursiveKnapsack(memo, profits, weights, capacity, currentIndex + 1)
    
    memo[currentIndex, capacity] = max(profit1, profit2)
    
    return memo[currentIndex, capacity]
    

print(solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
