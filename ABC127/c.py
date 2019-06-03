n, m = map(int, input().split())

l, r = 0, 10 ** 6
for i in range(m):
    tl, tr = map(int, input().split())
    l = max(tl, l)
    r = min(tr, r)
print(len(range(l, r+1)))
