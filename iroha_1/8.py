import math
x = int(input())

if x >= 10:
    f = sum(list(map(int, str(x))))
    t = math.ceil(f / 9)
    ans = 0
    for i in range(t-1):
        ans += 10 ** i * 9
        f -= 9
    ans += (10 ** (t-1)) * f
    if x == ans:
        if list(map(int, str(ans)))[0] == 9:
            ans = ans + 10 ** t - 10 ** (t - 1)
        else:
            ans = ans + 10 ** (t-1) - 10 ** (t-2)
    print(ans)
else:
    print(10 + x-1)
