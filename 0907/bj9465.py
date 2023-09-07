import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    dp = [[0 for _ in range(3)] for l in range(n + 1)]
    dp[1] = [0, up[0], down[0]] # 아무것도 안고름, 위 고름, 아래 고름
    for j in range(2, n + 1):
        dp[j][0] = max(dp[j - 1])
        dp[j][1] = max(dp[j - 1][0], dp[j - 1][2]) + up[j - 1]
        dp[j][2] = max(dp[j - 1][0], dp[j - 1][1]) + down[j - 1]
    
    print(max(max(dp)))

