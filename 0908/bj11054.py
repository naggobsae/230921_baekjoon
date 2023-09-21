import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [1] * n # 바이토닉 수열의 중심일 때의 최대 길이
dp1 = [1] * n # 왼쪽에서 오름차순
dp2 = [1] * n # 오른쪽에서 오름차순

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

lst.reverse()

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

for i in range(n):
    dp[i] = dp1[i] + dp2[i] - 1

print(max(dp))