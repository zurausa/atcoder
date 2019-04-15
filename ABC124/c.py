import sys
import math

mat = list(sys.stdin.readline().strip())

odd = 0
even = 0
for i, x in enumerate(mat):
    flg = i % 2
    if flg:
        if int(x) == 1:
            even += 1
        else:
            odd += 1
    else:
        if int(x) == 1:
            odd += 1
        else:
            even += 1

print(min(odd, even))

## t = S[0::2].count('0')+S[1::2].count('1')
## print(min(t, len(S)-t))
