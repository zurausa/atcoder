n, m = map(int, input().split())
ks = [[0] for i in range(m)]
jud = []
for i in range(m):
    tmp = list([int(i)-1 for i in input().split()])
    ks[i] = tmp[1:]
jud = list(map(int, input().split()))

ans = 0
c = True
for i in range(2 ** n):
    tmp = list()
    c = True
    for j in range(m):
        t = ks[j]
        ch = 0
        for m in t:
            ch += tmp[m]
        if ch % 2 != jud[j]:
            c = False
            break
    if c:
        ans += 1
print(ans)
