import sys

a, b, c = map(int, sys.stdin.readline().split())
if max(a, b) > c and min(a, b) < c:
    print('Yes')
else:
    print('No')
