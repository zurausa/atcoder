n, k = map(int, input().split())
d = list(map(int, input().split()))

ans = 0
for i in range(1, min(k + 1, len(d)+1)):
    s = 0
    for left in range(i+1):
        j = []
        if left > 0:
            j.extend(d[:left])
        if i-left > 0:
            j.extend(d[min(-(i - left), -1):])
        j = sorted(j)
        s = sum(j)
        for m in range(k - i):
            if len(j) <= m:
                break
            elif j[m] >= 0:
                break
            else:
                s -= j[m]
        ans = max(s, ans)
print(ans)
