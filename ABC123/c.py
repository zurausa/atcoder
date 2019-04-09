import sys
import math

n = int(sys.stdin.readline())

mn = 10 ** 16
for i in range(5):
    mn = min(mn, int(sys.stdin.readline()))

print(math.ceil(n/mn)+4)
