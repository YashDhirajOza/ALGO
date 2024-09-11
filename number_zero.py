def has_odd_number_of_zeros(number):
    num_str = str(number)
    zero_count = num_str.count('0')
    return zero_count % 2 != 0

def count_odd_zeros(arr):
    return sum(1 for num in arr if has_odd_number_of_zeros(num))

# Example usage
arr = [10, 200, 3000, 40000, 500000, 6000000, 700000]
result = count_odd_zeros(arr)
print(result)
