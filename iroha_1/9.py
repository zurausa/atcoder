n, m, k = map(int, input().split())
br = [0] * m
for i in range(m):
    a, b, c = map(int, input().split())
    br[i] = [a, b, c]
br = sorted(br, key=lambda x: x[0])
t = len([br for i in br if i[0] == 1])
