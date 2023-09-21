import sys
import collections
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    document = collections.deque(list(map(int, input().split())))
    order = 0
    while document:
        flag = True
        print_doc = document.popleft()
        m -= 1
        if m < 0:
            m = len(document)
        for i in document:
            if i > print_doc:
                document.append(print_doc)
                flag = False
                break
        if flag:
            order += 1
            if m == 0:
                print(order)
                break