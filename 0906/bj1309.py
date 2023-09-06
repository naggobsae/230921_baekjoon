n = int(input())

dp = [[0 for _ in range(3)] for i in range(n + 1)]

dp[1] = [1, 1, 1]

for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901 # 아무것도 안하는 경우
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901 # 왼쪽에 추가하는 경우
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901 # 오른쪽에 추가하는 경우

print(sum(dp[n]) % 9901)