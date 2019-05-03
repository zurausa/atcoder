import math
n, m, k = map(int, input().split())
a = [int(i) for i in input().split()]

if math.ceil(n / k) > m:
    print(-1)
else:
    pos = -1
    cnt = 0
    pnt = 0
    mid = []
    while pos < n - k:
        tmp = [v * (i+1) for i, v in enumerate(a[pos+1:min(pos+k+1, n)])]
        mx = 0
        plpos = 0
        for i, v in enumerate(tmp):
            if mx <= v:
                mx = v
                plpos = i+1
        pos += plpos
        pnt += a[pos]
        cnt += 1
        mid.append(pos)
    if cnt < m:
        for i, v in enumerate(mid):
            a.pop(v - i)
        a = sorted(a, reverse=True)
        for i in range(m - cnt):
            pnt += a[i]
print(pnt)
