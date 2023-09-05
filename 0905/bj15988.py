t = int(input())

lst = [0] * 1000001
lst[1] = 1
lst[2] = 2
lst[3] = 4

for i in range(t):
    n = int(input())
    if lst[n] != 0:
        print(lst[n])
        continue
    else:
        for j in range(4, n + 1):
            lst[j] = (lst[j - 1] + lst[j - 2] + lst[j - 3]) % 1000000009
    
    print(lst[n])