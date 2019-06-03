n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
bc = [[0] * 2 for _ in range(m)]
for i in range(m):
    bc[i] = list(map(int, input().split()))
bc = sorted(bc, key=lambda x: x[1], reverse=True)
mat = []
for b, c in bc:
    if len(mat) + b > n:
        mat.extend([c] * (n - len(mat)))
        break
    else:
        mat.extend([c]*b)

for i, t in enumerate(a):
    if i == len(mat):
        break
    if t < mat[i]:
        a[i] = mat[i]
    else:
        break

print(sum(a))
