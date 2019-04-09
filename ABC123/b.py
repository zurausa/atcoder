import sys
import math

matlist = [0] * 5
for i in range(5):
    matlist[i] = int(sys.stdin.readline())

mn = 11
idx = 0
for i in range(5):
    tmp = matlist[i] % 10
    if tmp == 0:
        tmp = 10
    if mn > tmp:
        idx = i
        mn = tmp

ans = 0
for i in range(5):
    if i != idx:
        ans += math.ceil(matlist[i]/10)*10
    else:
        ans += matlist[i]

print(int(ans))
