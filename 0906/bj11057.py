n = int(input())

dp = [[0 for _ in range(10)] for i in range(n + 1)]

dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 길이가 1인 끝나는 자리가 0 ~ 9인 수의 개수

for i in range(2, n + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][j:]) % 10007

print(sum(dp[n]) % 10007)