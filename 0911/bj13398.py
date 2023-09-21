import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [[i for i in lst] for _ in range(2)] # 특정요소를 제거하지 않은 경우와 제거한 경우

for i in range(1, n):
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + lst[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + lst[i])

print(max(max(dp[0]), max(dp[1])))