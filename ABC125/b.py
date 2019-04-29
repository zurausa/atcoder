n = int(input())
v = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    ans += max(v[i] - c[i], 0)
print(ans)
