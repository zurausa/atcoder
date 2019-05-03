import math
n, k = map(int, input().split())
tmp = int(math.sqrt(n)) + 1
factor = []
check = n

for num in range(2, tmp):
    while n % num == 0:
        n //= num
        factor.append(num)
if n != 1:
    factor.append(n)
l = len(factor)

if l >= k:
    for i in range(k-1):
        print(factor[i], end=' ')
        check = check // factor[i]
    print(check)
else:
    print(-1)
