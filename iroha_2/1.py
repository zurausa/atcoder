s = input()
t = input()

flg = True
ans = 0
for i in range(len(s))[::-1]:
    flg = True
    for j in range(len(s) - i + 1):
        tmp = s[j:j + i]
        if tmp in t:
            flg = False
            break
    if flg:
        ans = i
        break
print(ans)
