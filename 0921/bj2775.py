t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    dp = [[0 for i in range(1, n + 1)] for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = i + 1
    for i in range(1, k + 1):
        for j in range(n):
            for l in range(j + 1):
                dp[i][j] += dp[i - 1][l]
    
    print(dp[k][n - 1])