import sys

sentence = list(sys.stdin.readline().rstrip())
lst = []
while(sentence != ['.']):
    answer = "yes"
    for s in sentence:
        if s in ["(", "{", "["]:
            lst.append(s)
        elif s in [")", "}", "]"]:
            if lst ==[]:
                answer = "no"
                break
            elif s == ")" and lst[-1] == "(":
                lst.pop()
            elif s == "}" and lst[-1] == "{":
                lst.pop()
            elif s == "]" and lst[-1] == "[":
                lst.pop()
            else:
                answer = "no"
                break
    if lst:
        answer = "no"
    print(answer)
    lst = []
    sentence = list(sys.stdin.readline().rstrip())


