import sys
import collections
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = collections.deque(list(map(int, input().split())))
    
    flag = True
    count = 0
    while flag:
        out = queue[0]
        for j in range(len(queue)):
            if queue[j] > out:
                queue.append(queue.popleft())
                if m == 0:
                    m  = len(queue) - 1
                else:
                    m -= 1
                break
            elif j == len(queue) - 1:
                queue.popleft()
                count += 1
                if m == 0:
                    print(count)
                    flag = False
                else:
                    m -= 1
