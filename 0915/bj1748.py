n = input()
count = 0

for i in range(1, len(n)):
    count += 9 * (10**(i - 1)) * i

count += (int(n) - 10**(len(n) - 1) + 1) * len(n)

print(count)