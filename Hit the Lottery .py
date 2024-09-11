def min_number_of_bills(n):
    denominations = [100, 20, 10, 5, 1]
    bill_count = 0    
    for bill in denominations:
        count = n // bill
        bill_count += count
        n %= bill
    
    return bill_count

n = int(input())
print(min_number_of_bills(n))
