import sys

a, b, c = map(int, sys.stdin.readline().split())
print(min(int(b/a), c))
