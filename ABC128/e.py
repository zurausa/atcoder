n, q = map(int, input().split())
st = [0] * n
mx = 0
for i in range(n):
    s, t, x = map(int, input().split())
    mx = max(t-x, mx)
    st[i] = [max(s-x, 0), max(t-x, 0), x]
st = sorted(st, key=lambda x: x[2], reverse=True)
l = [-1] * mx
for s, t, x in st:
    l[s:t] = [x] * (t-s)

for i in range(q):
    d = int(input())
    if d >= mx:
        print(-1)
    else:
        print(l[d])
