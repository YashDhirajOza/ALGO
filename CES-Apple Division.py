

def find_min_difference(n, weights):
    total_weight = sum(weights)##  sum all the weights
    min_diff = float('inf')   ## declare it as float type 

    def backtrack(index, current_sum):
        nonlocal min_diff ## da fuq is this
        if index == n:
            other_sum = total_weight - current_sum
            min_diff = min(min_diff, abs(current_sum - other_sum))
            return

        # Choose the current apple in the first group
        backtrack(index + 1, current_sum + weights[index])
        
        # Choose the current apple in the second group
        backtrack(index + 1, current_sum)
    
    backtrack(0, 0)
    return min_diff

#################################################Main ##########################################################################
n = int(input())
weights = list(map(int, input().split()))

# Output
print(find_min_difference(n, weights))
