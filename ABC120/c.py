import sys
s = list(sys.stdin.readline())
l = len(s)
cnt0, cnt1 = 0, 0
for i in s:
    if "0" in i:
        cnt0 += 1
    elif "1" in i:
        cnt1 += 1

print(min(cnt0, cnt1)*2)
