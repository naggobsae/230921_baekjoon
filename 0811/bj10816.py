import sys

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in card_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in num_list:
    if i in dic:
        print(dic[i], end = ' ')
    else:
        print(0, end = ' ')