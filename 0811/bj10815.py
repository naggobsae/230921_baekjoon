n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
num_list = list(map(int, input().split()))

dic = {}

for i in num_list:
    dic[i] = 0

for i in card_list:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end = ' ')

print(dic)
