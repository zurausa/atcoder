import sys

mx = 0

mn = 124
mx = 0
for i in range(5):
    tmp = int(sys.stdin.readline())
    mn = min(mn, tmp)
    mx = max(mx, tmp)

if (mx-mn) > int(sys.stdin.readline()):
    print(':(')
else:
    print('Yay!')
