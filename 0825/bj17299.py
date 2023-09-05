# 풀이 1 : 시간초과 (o(n^2))
# import sys

# n = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# dic = {}
# ans = []

# for i in num_list:
#     if i not in dic:
#         dic[i] = num_list.count(i)

# for i in range(len(num_list)):
#     if i == len(num_list) - 1:
#         ans.append(-1)
#         break
#     for j in range(i+1, len(num_list)):
#         if dic[num_list[j]] > dic[num_list[i]]:
#             ans.append(num_list[j])
#             break
#         else:
#             if j == len(num_list) - 1:
#                 ans.append(-1)
#             else:
#                 continue

# for i in ans:
#     print(i, end = ' ')

import sys
import collections

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
count = collections.Counter(num_list)
stack = []
res = [-1] * n

for i in range(n):
    while stack and count[num_list[stack[-1]]] < count[num_list[i]]:
        res[stack.pop()] = num_list[i]
    stack.append(i)
    print(res)

for i in res:
    print(i, end = ' ')