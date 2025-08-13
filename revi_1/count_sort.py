def counting_sort(arr):
    if not arr:
        return arr
      ## base line 

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
# find the maax value and min value then range like how many comparmeents do we need to  
  # suppose array 1,23,444,3454,123
  # then we need 3454 rooms to store the freq of this number 
    #  this is used to count the freq of the number 
    count = [0] * k
  ## makes and array of 3454 with all the zeros
    for x in arr:
      # loops through the array and then increase the freq counter is present 
      ## supoose x= 444 then why do we need x-min_val 
      # 444-1 = 443 because of zero based indexing ? 
        count[x - min_val] += 1

    ## loop through the freq counter array to bulid the position of where to place what 
  
    for i in range(1, k):
      # prefix sum 
        count[i] += count[i - 1]

    # 3) Build output (right to left for stability)
    output = [0] * len(arr)
  # final answer
    for x in reversed(arr):
      
        idx = count[x - min_val] - 1
        output[idx] = x
        count[x - min_val] -= 1

    # 4) Copy back (optional)
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr
