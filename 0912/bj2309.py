import sys
input = sys.stdin.readline

height = []
sum = 0
for i in range(9):
    height.append(int(input()))
    sum += height[i]

for i in range(len(height)):
    flag = False
    for j in range(i + 1, len(height)):
        if sum - height[i] - height[j] == 100:
            height.pop(i)
            height.pop(j - 1)
            flag = True
            break
    if flag:
        break

height.sort()
for i in height:
    print(i)
