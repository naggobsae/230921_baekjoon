t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    front = n % h
    back = n // h + 1
    if front == 0:
        front = h
        back -= 1
    if len(str(back)) == 1:
        print(str(front) + "0" + str(back))
    else:
        print(str(front) + str(back))
    