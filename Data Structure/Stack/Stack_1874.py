import sys

num = int(sys.stdin.readline())
stack = []
nums = []
operation = []
last = 0
for i in range(num):
    nums.append(int(sys.stdin.readline()))

for k in nums:
    if last < k:
        for j in range(last, k):
            stack.append(j+1)
            operation.append("+")
        x = stack.pop()
        last = max(last,x)
        operation.append("-")
    elif last >k:
        x = stack.pop()
        if x == k:
            operation.append("-")
        else:
            operation = ["NO"]
            break
        last = max(last,x)
           
for i in operation:
    print(i)