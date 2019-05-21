from collections import deque
n = int(input())
q = deque(maxlen=n-1)

for i in range(n - 1):
    a, b, c = map(int, input().split())
    q.append([a-1, b-1, c % 2])

cllist = [-1] * n
a, b, c = q.popleft()
cllist[a] = 0
cllist[b] = c
while q:
    a, b, c = q.popleft()
    if cllist[a] != -1:
        cllist[b] = (cllist[a] + c) % 2
    elif cllist[b] != -1:
        cllist[a] = (cllist[b] + c) % 2
    else:
        q.append([a, b, c])
print(*cllist)
