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
    c = True
    ib = format(i, 'b')
    for iks, j in enumerate(ks):
        ch = 0
        for m in j:
            if len(ib) >= m+1:
                ch += int(ib[-m-1])
        if ch % 2 != jud[iks]:
            c = False
            break
    if c:
        ans += 1
print(ans)
