import sys

n = int(sys.stdin.readline())

jpy = 0
btc = 0
for _ in range(n):
    x, y = sys.stdin.readline().split()
    if 'JPY' in y:
        jpy += int(x)
    else:
        btc += float(x) * 380000

print(jpy + btc)
