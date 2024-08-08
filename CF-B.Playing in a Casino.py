def total_winnings(t, test_cases):
    results = []
    
    for n, m, cards in test_cases:
        total_sum = 0
        
        # Calculate winnings for each column
        for j in range(m):
            column = sorted(cards[i][j] for i in range(n))
            for i in range(n):
                total_sum += column[i] * (2*i - n + 1)
        
        results.append(total_sum)
    
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    cards = []
    for _ in range(n):
        cards.append(list(map(int, input().split())))
    test_cases.append((n, m, cards))

# Getting results
results = total_winnings(t, test_cases)

# Printing results
for result in results:
    print(result)
