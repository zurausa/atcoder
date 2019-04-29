n = int(input())
v = [int(i) for i in input().split()]


def gcd(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    if x % y == 0:
        return y
    return gcd(y, x % y)


l = [0 for i in range(n)]
r = l[:]

for i in range(1, n):
    l[i] = gcd(l[i - 1], v[i - 1])
    r[-i-1] = gcd(r[-i], v[-i])
m = [gcd(l[i], r[i]) for i in range(n)]
print(max(m))
