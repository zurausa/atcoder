n = int(input())
a = [int(i) for i in input().split()]

a_sum = abs(a[0])
a_min = abs(a[0])
cnt = 0
if a[0] < 0:
    cnt += 1
for i in range(n - 1):
    a_min = min(a_min, abs(a[i+1]))
    a_sum += abs(a[i+1])
    if a[i + 1] < 0:
        cnt += 1
if cnt % 2 == 0:
    print(a_sum)
else:
    print(a_sum-a_min*2)


'''
B = list(map(abs, a))
C = [a for i in a if a < 0]
if len(C) % 2 == 0:
    print(sum(B))
else:
    print(sum(B) - min(B)*2)
 '''
