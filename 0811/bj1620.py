import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

name_dic = {}
num_dic = {}

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    name_dic[name] = i
    num_dic[i] = name

for i in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(num_dic[int(temp)])
    else:
        print(name_dic[temp])

# rstrip은 input한 문자열에서 enter를 지워준다
# isdigit은 입력한 문자열이 0~9로만 이뤄져 있는지 boolean으로 반환하는 함수