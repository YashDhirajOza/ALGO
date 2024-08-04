stone_num = int(input())
# height is 1-indexed so it can match up with dp
height = [0] + [int(s) for s in input().split()]
assert stone_num == len(height) - 1

"""
dp[N] is the minimum cost to get to the Nth stone
(we initially set all values to INF)
"""
dp = [float("inf") for _ in range(stone_num + 1)]
# dp[1] = 0 is our base case since we're already at the first stone
dp[1] = 0

for i in range(1, stone_num + 1):
	if i + 1 <= stone_num:
		dp[i + 1] = min(dp[i + 1], dp[i] + abs(height[i] - height[i + 1]))
	if i + 2 <= stone_num:
		dp[i + 2] = min(dp[i + 2], dp[i] + abs(height[i] - height[i + 2]))

print(dp[stone_num])