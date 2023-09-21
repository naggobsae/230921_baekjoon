from collections import Counter

t = int(input())
lst = []
counts = {}

for i in range(t):
    n = int(input())
    lst.append(n)
    if n not in counts:
        counts[n] = 1
    else:
        counts[n] += 1

max_counts = max(counts.values())
mode = [k for k, v in counts.items() if max_counts == v]
mode.sort()

lst.sort()
mean = round(sum(lst) / t)
median = lst[t//2]
range_lst = lst[-1] - lst[0]

print(mean)
print(median)
print(mode[1] if len(mode) > 1 else mode[0])
print(range_lst)