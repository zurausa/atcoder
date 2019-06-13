n = int(input())
w = list(map(int, input().split()))
s = sum(w)
l = 0
ans = 10 ** 9
for i in range(n):
    l += w[i]
    s -= w[i]
    ans = min(ans, abs(s-l))
print(ans)
