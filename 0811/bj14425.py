n, m = map(int, input().split())
n_list = []
m_list = []
count = 0

for i in range(n):
    n_list.append(input())
for i in range(m):
    m_list.append(input())

for i in range(m):
    if m_list[i] in n_list:
        count += 1
print(count)