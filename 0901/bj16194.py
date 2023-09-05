import sys

n = int(sys.stdin.readline())
card_list = [0] + list(map(int, sys.stdin.readline().split()))

d = card_list
for i in range(1, n + 1):
    for j in range(1, i + 1):
        d[i] = min((d[i - j] + card_list[j]), d[i])

print(d[n])