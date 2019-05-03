n, x, y = map(int, input().split())
a = [int(i) for i in input().split()]
a = sorted(a, reverse=True)

for i in range(n)[::2]:
    x += a[i]
    y += a[i+1]
if x > y:
    print('Takahashi')
elif x == y:
    print('Draw')
else:
    print('Aoki')
