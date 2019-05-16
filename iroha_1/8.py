import math
x = int(input())

if x >= 10:
    # 各桁の和
    f = sum(list(map(int, str(x))))
    # 最終的に必要な桁数
    t = math.ceil(f / 9)
    ans = 0
    for i in range(t-1):
        ans += 10 ** i * 9
        f -= 9
    ans += (10 ** (t-1)) * f
    # 入力と同じ場合には一つずらす
    if x == ans:
        # 99みたいな場合の考慮(%9==0でもいいのでは...)
        if list(map(int, str(ans)))[0] == 9:
            ans = ans + 10 ** t - 10 ** (t - 1)
        else:
            ans = ans + 10 ** (t-1) - 10 ** (t-2)
    print(ans)
else:
    # 9以下
    print(10 + x-1)
