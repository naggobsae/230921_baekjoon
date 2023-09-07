import sys
input = sys.stdin.readline

n = int(input())
wine = [0]

for i in range(n):
    amount = int(input())
    wine.append(amount)

if n == 1: # 예외처리
    print(wine[1])
    exit()

dp = [[0, 0] for _ in range(n + 1)]
dp[1] = [0, wine[1]] # 1번째 잔을 마시지 않았을 때, 마셨을 때 최댓값
dp[2] = [wine[1], wine[1] + wine[2]] # 2번째 잔을 마시지 않았을 때, 마셨을 때 최댓값

for i in range(3, n + 1):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = max(dp[i - 2][1] + wine[i], dp[i - 2][0] + wine[i - 1] + wine[i])

print(max(dp[n]))