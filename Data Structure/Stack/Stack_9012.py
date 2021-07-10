import sys

K = int(sys.stdin.readline())

for i in range(K):
    close=[]
    ps = list(sys.stdin.readline().rstrip())
    answer = "YES"
    for p in ps[::-1]:
        if p == ")":
            close.append(p)
        elif p == "(":
            if close:
                close.pop()
            else:
                answer = "NO"
                break
    if close:
        answer = "NO"
    print(answer)
