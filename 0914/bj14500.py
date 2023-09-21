import sys
input = sys.stdin.readline

def is_max(square, is_check):
    max = 0
    max_x = 0
    max_y = 0
    for i in range(len(is_check)):
        for j in range(len(is_check[i])):
            if is_check[i][j] != 1:
                continue
            else:
                if i == 0:
                    if j == 0:
                        if max < max(square[i][j + 1], square[i + 1][j]):
                            max = max(square[i][j + 1], square[i + 1][j])
                            max_x = i
                            max_y = j
                    elif j == len(is_check[i]) - 1:
                        if max < max(square[i][j - 1], square[i + 1][j]):
                            max = max(square[i][j - 1], square[i + 1][j])
                            max_x = i
                            max_y = j
                    else:
                        if max < max(square[i][j - 1], square[i][j + 1], square[i + 1][j]):
                            max = max(square[i][j - 1], square[i][j + 1], square[i + 1][j])
                            max_x = i
                            max_y = j
                elif i == len(is_check) - 1:
                    if j == 0:
                        if max < max(square[i][j + 1], square[i - 1][j]):
                            max = max(square[i][j + 1], square[i - 1][j])
                            max_x = i
                            max_y = j
                    elif j == len(is_check[i]) - 1:
                        if max < max(square[i][j - 1], square[i - 1][j]):
                            max = max(square[i][j - 1], square[i - 1][j])
                            max_x = i
                            max_y = j
                    else:
                        if max < max(square[i][j - 1], square[i][j + 1], square[i - 1][j]):
                            max = max(square[i][j - 1], square[i][j + 1], square[i + 1][j])
                            max_x = i
                            max_y = j
                else:
                    if j == 0:
                        if max < max(square[i][j + 1], square[i - 1][j], square[i + 1][j]):
                            max = max(square[i][j + 1], square[i - 1][j], square[i + 1[j]])
                            max_x = i
                            max_y = j
                    elif j == len(is_check[i]) - 1:
                        if max < max(square[i][j - 1], square[i - 1][j], square[i + 1][j]):
                            max = max(square[i][j - 1], square[i - 1][j], square[i + 1][j])
                            max_x = i
                            max_y = j
                    else:
                        if max < max(square[i][j - 1], square[i][j + 1], square[i - 1][j]):
                            max = max(square[i][j - 1], square[i][j + 1], square[i + 1][j])
                            max_x = i
                            max_y = j

n, m = map(int, input().split())
square = []
is_check = [[0 for _ in range(m)] for i in range(n)]

for i in range(n):
    square.append(list(map(int, input().split())))

count = 0

while count != 4:
    for i in range(n):
        for j in range(m):
            is_check[i][j] = 1
            count += 1




