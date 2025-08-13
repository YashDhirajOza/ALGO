# bubbble sort is a simple algo 
# compaers adjacent elemtns and swaps them if they are in the wronf order 
# gets name from bubble in water 
def bubble_sort(arr):
  
  n=len(arr)
  for i in range(n):
    swapped=False 
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
           arr[j],arr[j+1]=arr[j+1],arr[j]
          swapped=True 
      if not swapped:
        break
  return arr
  
