a, b = map(int, input().split())
k ,x = map(int, input().split())

count = 0
for i in range(a, b + 1):
    if abs(i - k) <= x:
        count += 1

print(count)