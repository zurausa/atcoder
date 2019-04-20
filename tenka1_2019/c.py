import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

bcnt = 0
wcnt = 0
bst = 10 ** 6
lastlen = 0

for i in range(n):
    tmp = s[i:i + 1]
    if tmp == "#":
        bcnt += 1
        if bst > i:
            bst = i
        lastlen += 1
    else:
        if i > bst:
            wcnt += 1
        lastlen = 0

print(min(wcnt, bcnt-lastlen))
