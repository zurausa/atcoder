import math
import numpy as np
# Rが最大である場合を考えた上で構築する(最後に3倍(G,Bの場合を考える))
n = int(input())
matlist = np.array([int(input()) for _ in range(n)])
s = np.sum(matlist)
mod = 998244353
dp = np.zeros((n+1, s+1))
dp[0, 0] = 1
half_dp = np.zeros((n+1, s//2+1))
half_dp[0, 0] = 1
for i, mat in enumerate(matlist):
    # Rに一切採用しない場合があるので[0,0]が1,[1,0]が2になる(B,Gそれぞれが考えられるため)
    dp[i+1, :] += dp[i, :] * 2 % mod
    dp[i + 1, mat:] += dp[i, : - mat]
    # dp2はB=Gの場合なので、* 2をしない
    half_dp[i+1, :] += half_dp[i, :] % mod
    half_dp[i + 1, mat:] += half_dp[i, : - mat]

# Rの合計値がs/2を超える場合を考えるため、以下のような式になる(格納されているのは場合数)
subset1 = np.sum(dp[n, math.ceil(s / 2):])
# s % 2 == 1ならR=B= s/2, G=0のようなパターンが存在しないため0になる
subset2 = 0 if s % 2 == 1 else half_dp[n, s//2]
print((3 ** n - 3 * subset1 + 3 * subset2) % mod)
