s = input()
n = int(input()) % len(s)
print(s[n:], end='')
print(s[:n])
