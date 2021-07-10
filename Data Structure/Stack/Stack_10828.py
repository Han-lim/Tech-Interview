import sys

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else -1
    def size(self):
        return len(self.stack)
    def empty(self):
        return 0 if self.stack else 1
    def top(self):
        return self.stack[-1] if self.stack else -1

N = int(sys.stdin.readline())
s =Stack()

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        s.push(cmd[1])
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        print(s.empty())
    elif cmd[0] == "top":
        print(s.top())