import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = lst[i]

for i in range(2, n + 1):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))