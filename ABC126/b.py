s = input()
a, b = int(s[:2]), int(s[2:])
ch = 0
if 0 < a < 13:
    ch += 1
if 0 < b < 13:
    ch += 2
if ch == 0:
    print("NA")
elif ch == 1:
    print('MMYY')
elif ch == 2:
    print('YYMM')
elif ch == 3:
    print('AMBIGUOUS')
