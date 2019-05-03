import numpy as np
n = int(input())
a = [0] * n
aset = []


def func1(value):
    for i, x in enumerate(aset):
        if x == value:
            return i


for i in range(n):
    a[i] = int(input())
    if a[i] not in aset:
        aset.append(a[i])
aset.sort()
adic = dict()
for i, x in enumerate(aset):
    adic[x] = i+1
for i in a:
    print(adic[i])
