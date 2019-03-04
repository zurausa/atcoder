import sys

y, m, d = map(int, sys.stdin.readline().split("/"))
if (y == 2019 and m <= 4) or y < 2019:
    print('Heisei')
else:
    print('TBD')
