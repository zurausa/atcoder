import sys

a, b = map(int, sys.stdin.readline().split())


def check(x):
    if x % 4 == 0:
        return x
    elif x % 2 == 0:
        return x + 1
    elif (x+1)/2 % 2 == 0:
        return 0
    else:
        return 1


a = check(a-1)
b = check(b)
print(a ^ b)
