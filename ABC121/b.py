import sys

n, m, c = map(int, sys.stdin.readline().split())
blist = list([int(i) for i in sys.stdin.readline().split()])

ans = 0
for _ in range(n):
    tmp = list([int(i) for i in sys.stdin.readline().split()])
    check = c
    for i in range(m):
        check += tmp[i] * blist[i]
    if check > 0:
        ans += 1

print(ans)
