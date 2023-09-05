n = int(input())

lst = [0] * (n + 1)

for i in range(n+1):
    lst[i] = i

for i in range(2, n + 1):
    for j in range(1, int(i**(1/2) + 1)):
        lst[i] = min(lst[i], lst[i - j**2] + 1)

print(lst[n])