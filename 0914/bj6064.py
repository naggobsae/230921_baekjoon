# 풀이 1 : 시간초과 => 1씩 증가시키면 시간 초과가 발생
# import sys
# input = sys.stdin.readline

# t = int(input())

# for i in range(t):
#     m, n, x, y = map(int, input().split())
#     first_x, first_y = 1, 1
#     year = 1
#     while not (first_x == x and first_y == y):
#         first_x += 1
#         first_y += 1
#         year += 1
#         if first_x > m:
#             first_x = 1
#         if first_y > n:
#             first_y = 1
#         if first_x == m and first_y == n:
#             if first_x == x and first_y == y:
#                 break
#             else:
#                 year = -1
#                 break
#     print(year)

# 풀이 2 : 좀 더 간단한 방법을 생각하자, 1씩 더하면 안됨

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    m, n, x, y = map(int, input().split())
    temp = x
    while temp <= m * n: # temp는 mn을 넘길 수 없음. mn을 넘기면 m과 n의 공배수이므로 종말의 날을 지난다.
        if (temp - x) % m == 0 and (temp - y) % n == 0:
            print(temp)
            break
        else:
            temp += m # 1씩 안더하고 m씩 더하는 이유는 temp의 초기값이 x이므로 답은 x + m의 배수여야 하기 때문
    if temp > m * n:
        print(-1)
        