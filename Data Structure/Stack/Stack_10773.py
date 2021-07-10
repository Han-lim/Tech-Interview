import sys
N = int(sys.stdin.readline())
s = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        s = s[:-1]
    else:
        s.append(num)
    
print(sum(s))
