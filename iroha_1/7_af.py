n, m, k = map(int, input().split())
a = list(map(int, input().split()))
if k * (m + 1) - 1 < n:
    print(-1)
else:
    dp = [[0] * n for i in range(m)]
    # 初回分の分の探索
    for i in range(k):
        dp[0][i] = a[i]
    # 2回目以降の探索
    for i in range(1, m):
        # 2回目で行ける範囲(i, min(n, k * (m + 1)))を指定して探索
        for j in range(i, min(n, k * (m + 1))):
            # 前行の中で[j-k:j-1]地点を探し最大のものを選択した上でその地点の数値を加算
            dp[i][j] = max(dp[i - 1][max(0, j - k):j]) + a[j]
    # 最終行でNにたどり着けるものの中で最大のものを選択し出力
    print(max(dp[m-1][n-k:]))
