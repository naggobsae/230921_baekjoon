import sys

t = int(sys.stdin.readline())
d = [[0 for _ in range(3)] for i in range(100001)]
# ★shallow copy를 조심하기!! [[0, 0, 0]] * 100001로 풀면 틀리게 된다★
d[1] = [1, 0, 0]
d[2] = [0, 1, 0]
d[3] = [1, 1, 1]
check = 3

for i in range(t):
    n = int(sys.stdin.readline())
    if n <= check:
        print(sum(d[n]) % 1000000009)
        continue
    else:
        for j in range(check + 1, n + 1):
            d[j][0] = (d[j - 1][1] + d[j - 1][2]) % 1000000009 # 여기서 미리 안나눠주면  수가 너무 커져 시간 초과
            d[j][1] = (d[j - 2][0] + d[j - 2][2]) % 1000000009
            d[j][2] = (d[j - 3][0] + d[j - 3][1]) % 1000000009
        check = n
    
    print(sum(d[n]) % 1000000009)