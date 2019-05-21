m, k = map(int, input().split())
l = int(2 ** (m + 1))
p = 2 ** m
if m == 0 or m == 1:
    if k == 0:
        if m == 0:
            print('0 0')
        else:
            print('0 0 1 1')
    else:
        print('-1')
else:
    if k >= p:
        print('-1')
    else:
        ans = []
        tmp = list(range(p))
        tmp.remove(k)
        ans.extend(tmp)
        ans.append(k)
        ans.extend(list(reversed(tmp)))
        ans.append(k)
        print(*ans)
