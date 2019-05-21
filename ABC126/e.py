n, m = map(int, input().split())

p = list(range(n))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)
    p[x] = p[y] = min(x, y)


for _ in range(m):
    x, y, z = [int(i) - 1 for i in input().split()]
    if find(x) != find(y):
        union(x, y)

ans = set()
for i in range(n):
    find(i)
print(len(set(p)))
