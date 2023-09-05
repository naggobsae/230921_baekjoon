n = int(input())

lst = [[0 for _ in range(10)] for i in range(101)]

lst[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            lst[i][j] = lst[i - 1][j + 1] % 1000000000
        elif j == 9:
            lst[i][j] = lst[i - 1][j - 1] % 1000000000
        else:
            lst[i][j] = (lst[i - 1][j - 1] + lst[i - 1][j + 1]) % 1000000000

print(sum(lst[n]) % 1000000000)