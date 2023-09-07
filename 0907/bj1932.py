import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for i in range(n):
    lst = list(map(int, input().split()))
    triangle.append(lst)

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i - 1][0] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] = triangle[i - 1][-1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

print(max(triangle[n - 1]))