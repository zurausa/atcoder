n = int(input())
mp = list(map(int, input().split()))


def check(a, b):
    if (n - b - 1) % (a - b) != 0:
        return False
    if a % (a - b) == 0 and (a + b) >= n - 1:
        return True
    return False


ans = 0
if n == 3:
    print(0)
else:
    for a in range(2, n):
        for b in range(1, a):
            if check(a, b):
                continue
            else:
                ans = max(ans, 0)
    print(ans)
