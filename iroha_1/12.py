import math
n, k = map(int, input().split())
t = [0] * (n + 1)
a = [t[:] for i in range(n + 1)]
a[0][1:] = [int(i) for i in input().split()]


for i in range(1, n+1):
    for j in range(i, n+1):
        a[i][j] = a[0][j] | a[i][j-1]

ans = []
for i in range(1, n + 1):
    ans.extend(a[i])
ans = sorted(ans, reverse=True)
print(ans[k-1])
