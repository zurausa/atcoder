n, m, k = map(int, input().split())

dist = [0] * n
r = range(1, n)
for i in range(n):
    if i == 0 or i == n - 1:
        dist[i] = sum(r)
    else:
        dist[i] = sum(r[:i]) + sum(r[:n - i - 1])
