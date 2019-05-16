''' sparse table
参考コード(https://atcoder.jp/contests/iroha2019-day1/submissions/5340178 )
n,k = 9 37
a=[2,0,1,2,5,7,0,2,3]のときについて解説

sparse_table[n][n.bit_length()] で構築
※以降stと表記
st[0] には 長さ2**0のa[i]のみを代入
st[1] には 長さ2**1のa[i:i+1]のor値を入力
(ex: st[1] = [2,1,3,7,7,7,2,3,0])となる ※右詰で
st[2] には 長さ2**2のa[i:i+3]の全部のor値を入力
これはst[1]を利用すれば最小限のコストで構築可能
同様に処理
[2,0,1,2,5,7,0,2,3],
[2,1,2,7,7,7,2,3,0],
[2,7,7,7,7,7,0,0,0],
[7,7,0,0,0,0,0,0,0]

・検索部分について
利用するst列に関しては
検索の長さから決定する
ex:) r-l = 0,1 => 0列目
         = 2,3 => 1列目
         = 4,5,6,7 => 2列目
         ...
これはログテーブルを作成すれば問題なし
# log_table = [0,0,1,1,2,2,2,2,3,3,3,3,3....]
for i in range(2, len(self.log_table)):
            self.log_table[i] = self.log_table[i//2] + 1

or部分に関しては右側をr - (1 << row)のようにする
同じ要素をorしても解は変わらないので
例えば(L,R) = (0,3)のような場合
L ... st[1][0] => (a[0] | a[1] )
R ... st[1][1] => (a[1] | a[2] )
になる。

L,RのOR結果が二分探索で出している値より大きい場合、
それ以降のRに関しては同様の結果が求められるため、
cnt += n - r + 1とできる
これを繰り返し、cnt がkより大きければ探索値を切り替える
 '''

import math
import numpy as np
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

lt = [0 for _ in range(n+1)]
for i in range(2, n + 1):
    lt[i] = lt[i//2]+1


def make_st(a, n):
    rs = n.bit_length()
    st = [[0]*n for _ in range(rs)]
    for i in range(n):
        st[0][i] = a[i]
    for row in range(1, rs):
        for i in range(n - (1 << row) + 1):
            st[row][i] = st[row - 1][i] | st[row - 1][i + (1 << (row - 1))]
    return st


def query(l, r):
    if l == r:
        return - 1
    row = lt[r - l]
    return st[row][l] | st[row][r - (1 << row)]


def solve(mid):
    l = 0
    r = 1
    cnt = 0
    while True:
        while (r < n and query(l, r) < mid):
            r += 1
        if query(l, r) < mid:
            break
        cnt += n - r + 1
        l += 1
    return cnt


st = make_st(a, n)
mn = 0
mx = query(0, n) + 1

while abs(mx - mn) > 1:
    mid = (mn + mx) // 2
    if solve(mid) < k:
        mx = mid
    else:
        mn = mid
print(mn)
