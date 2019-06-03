q = int(input())
qur = [0] * q
for i in range(q):
    t = list(map(int, input().split()))
    if len(t) == 1:
        qur[i] = [2, 0, 0]
    else:
        qur[i] = t
fx = 0
x = 0
cnt = 0
sa = 0
sb = 0
alist = []


def sumx(x, alist):
    s = 0
    for i in alist:
        s += abs(x-i)
    return s


for o, a, b in qur:
    if o == 1:
        alist.append(a)
        sa += a
        sb += b
        cnt += 1
        x = sa // cnt
        fx = sumx(x, alist) + sb
    else:
        print(x, end=" ")
        print(fx)
