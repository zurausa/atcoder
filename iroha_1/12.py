import math
import numpy as np
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
bit_range = math.floor(math.log2(max(a)))+1
mp = np.reshape(np.zeros(bit_range*(n+1)), (n+1, bit_range))
for i in range(n):
    tmp = np.array(list(map(int, list(format(a[i], 'b')))))
    if tmp.size < bit_range:
        tmp = np.pad(tmp, (bit_range-tmp.size, 0), 'constant')
    mp[i + 1] = mp[i] + tmp
mid = 2 ** (bit_range-1)
mx = 2 ** bit_range - 1
mn = 0


def mp_to_int(x):
    ret = 0
    l = len(x)
    for i, x in enumerate(x.tolist()):
        if x > 0:
            ret += 2 ** (l - i - 1)
    return ret


ans = []
while True:
    cnt = 0
    for i in range(1, n+1):
        if a[i - 1] >= mid:
            cnt += n+1 - i
        else:
            for j in range(i+1, n + 1):
                if mp_to_int(mp[j] - mp[i - 1]) >= mid:
                    cnt += n + 1 - j
                    break

    if cnt >= k:
        ans.append(mid)
        mn = mid
        mid = math.ceil((mn + mx)/2)
    else:
        mx = mid
        mid = math.floor((mn + mx) / 2)
    if mid in ans:
        break
print(mid)
