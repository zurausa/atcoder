import sys

x, y, z, k = map(int, sys.stdin.readline().split())

xlist = sorted(list([int(i)
                     for i in sys.stdin.readline().split()]), reverse=True)[:min(x, k)]
ylist = sorted(list([int(i)
                     for i in sys.stdin.readline().split()]), reverse=True)[:min(y, k)]
zlist = sorted(list([int(i)
                     for i in sys.stdin.readline().split()]), reverse=True)[:min(z, k)]


anslist = [0]
for i in range(min(x, k)):
    for j in range(min(y, k)):
        for l in range(min(z, k)):
            if (i+1)*(j+1)*(l+1) <= k:
                anslist.append(xlist[i] + ylist[j] + zlist[l])
            else:
                break

anslist = sorted(anslist, reverse=True)
for i in range(k):
    print(anslist[i])
