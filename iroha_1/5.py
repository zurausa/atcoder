import math
n, a, b = map(int, input().split())
if b == 0:
    print(n - n // a)
else:
    d = [int(i) for i in input().split()]
    d.insert(0, 0)
    d = sorted(d)
    date = 0
    for i in range(1, b + 1):
        date += math.ceil((d[i] - d[i - 1])/a)

    print(n-(date + (n - d[b])//a))
