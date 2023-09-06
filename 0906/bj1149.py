# 풀이 1 : 틀렸습니다. 100 100 100 인 경우 index가 맨 앞만 결정되는 문제를 해결하지 못함
# import sys

# n = int(sys.stdin.readline())
# color_price = [[0 for _ in range(3)]]
# dp = [0] * (n + 1)

# for i in range(n):
#     rgb = list(map(int, sys.stdin.readline().split()))
#     color_price.append(rgb)

# dp[1] = min(color_price[1])

# for i in range(2, n + 1):
#     idx = color_price[i - 1].index(dp[i - 1])
#     if idx == 0:
#         minimum = min(color_price[i][1], color_price[i][2])
#     else:
#         minimum = color_price[i][0]
#         for j in range(1, 3):
#             if minimum > color_price[i][j] and idx != j:
#                 minimum = color_price[i][j]
#     dp[i] = minimum

# print((dp))

# 풀이 2 : 합을 한번에 저장하자!

import sys

n = int(sys.stdin.readline())
color_price = [[0 for _ in range(3)]]

for i in range(n):
    rgb = list(map(int, sys.stdin.readline().split()))
    color_price.append(rgb)

dp = [[0 for _ in range(3)] for i in range(n + 1)]

dp[1] = color_price[1]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color_price[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color_price[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color_price[i][2]

print(min(dp[n]))