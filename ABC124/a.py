import sys

x, y = map(int, sys.stdin.readline().split())

if x == y:
    print(x * 2)
else:
    print(max(x, y)*2-1)
