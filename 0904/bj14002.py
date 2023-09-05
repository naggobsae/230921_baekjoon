import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

lst = [1] * n
ans = []

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            lst[i] = max(lst[i], lst[j] + 1)

max_value = max(lst)

for i in range(n - 1, -1, -1):
    if lst[i] == max_value:
        ans.append(seq[i])
        max_value -= 1

print(max(lst))
ans.reverse()
print(*ans)