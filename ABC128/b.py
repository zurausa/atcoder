n = int(input())
d = {}
for i in range(n):
    s, p = input().split()
    if d.get(s) == None:
        d[s] = [[int(p), i]]
    else:
        d.get(s).append([int(p), i])
for key in sorted(d.keys()):
    for v, i in sorted(d.get(key), key=lambda x: x[0], reverse=True):
        print(i+1)
