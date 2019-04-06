import sys

s = sys.stdin.readline()

cnt = 0
ans = 0
for i in range(len(s)):
    tmp = s[i]
    if tmp in 'ACGT':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)
