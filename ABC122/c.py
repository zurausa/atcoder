import sys

n, q = map(int, sys.stdin.readline().split())
s = sys.stdin.readline()

elist = [0] * (n+1)
for i in range(n - 1):
    elist[i + 2] = elist[i + 1] + (1 if 'AC' == s[i:i+2] else 0)

for i in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(elist[r] - elist[l])
