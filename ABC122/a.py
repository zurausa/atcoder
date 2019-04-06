import sys

s = sys.stdin.readline()
if 'A' in s:
    print('T')
elif 'G' in s:
    print('C')
elif 'C' in s:
    print('G')
else:
    print('A')
