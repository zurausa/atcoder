import sys
n, m = map(int, input().split())
bf = -1
way = [-1] * (n+1)
way[0] = 1
way[1] = 1
mod = 10 ** 9 + 7
for i in range(m):
    tmp = int(input())
    if bf + 1 == tmp:
        print(0)
        sys.exit()
    bf = tmp
    way[tmp] = 0
for i in range(2, n+1):
    if way[i] == -1:
        way[i] = way[i-2] + way[i-1]
print(way[n] % mod)
