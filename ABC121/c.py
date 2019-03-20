import sys

n, m = map(int, sys.stdin.readline().split())
matlist = []
for _ in range(n):
    matlist.append(list([int(i) for i in sys.stdin.readline().split()]))
matlist = sorted(matlist, key=lambda x: x[0])

ans = 0
for c, v in matlist:
    if v >= m:
        ans += c * m
        break
    else:
        ans += c * v
        m -= v

print(ans)
