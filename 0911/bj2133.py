# n이 2일 때는 3가지
# n이 4일 때는 3 * 3 + 2 (n을 2 2로 쪼갠 것과 n이 4일때만 가능한 모양 2개)
# n이 6일 때는 dp[4] * dp[2] + dp[2] * 2 + 2 (n을 4 2로 쪼갠 것과 n이 4일 때 특수도형 2개, n이 6일 때 특수도형 2개)
# 따라서 점화식은 dp[n] = dp[n - 2] * dp[2] + dp[n - 4] * 2 + dp[n - 6] * 2 + ... + 2

n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 11

for i in range(4, n + 1):
    if i % 2 == 0:
        dp[i] = dp[i - 2] * dp[2] + sum(dp[:i - 2]) * 2 + 2

print(dp[n])