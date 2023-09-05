# 14002번 문제와 매우 흡사해보임
# 풀이 1 : 시간 초과
import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

lst = []
for i in seq:
    lst.append(i)

for i in range(2, n):
    for j in range(i):
        if seq[i] < sum(seq[j:i+1]):
            lst[i] = max(lst[i], sum(seq[j:i+1]))

print(max(lst))