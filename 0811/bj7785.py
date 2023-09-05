n = int(input())
enter_dic = {}

for i in range(n):
    name, cond = input().split()
    if cond == "enter":
        enter_dic[name] = 1
    else:
        del enter_dic[name]

enter_dic = sorted(enter_dic, reverse = True)

for names in range(len(enter_dic)):
    print(enter_dic[names])