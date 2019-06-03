from collections import deque
n, k = map(int, input().split())
d = deque(list(map(int, input().split())), maxlen=n)


def cval():
    return 1


for i in range(k):

    print('a')
