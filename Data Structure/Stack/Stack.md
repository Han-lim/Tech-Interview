## Stack

### Stack 개념
- 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out)형식의 자료구조
-----
### Stack 연산
(1) pop(): 스택에서 가장 위에 있는 항목을 제거  
(2) push(item): item 하나를 스택의 가장 윗 부분에 추가  
(3) peek(): 스택의 가장 위에 있는 항목을 반환  
(4) isEmpty(): 스택이 비어 있을 때에 true를 반환  

----
### Stack 구현

```python
class Stack:
    #리스트를 이용하여 stack 초기화
    def __init__ (self):
        self.stack = []
    
    #stack 길이 return
    def __len__(self):
        return len(self.stack)

    #stack의 내용을 string으로 변환하여 return
    def __str__(self):
        return str(self.top[::1])
    
    #stack 초기화
    def clear(self):
        self.top=[]

    #push
    def push (self, item):
        self.top.append(item)

    #pop
    def pop(self):
        #if Stack is not empty
        if not self.isEmpty():
            #pop and return 
            return self.top.pop(-1)
        else:
            print("Empty")
            exit()
    
    #stack 내에 item이 있는지를 return
    def isContain(self, item):
        return item in self.top
    
    #stack의 top을 return
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("Empty")
            exit()

    #stack이 비어있는지 return
    def isEmpty(self):
        return len(self.top)==0
    
    #stack size 반환
    def size(self):
        return len(self.top)
    
```
----
### Stack 응용
+ 재귀 알고리즘
    + 재귀적으로 함수를 호출해야 하는 경우에 임시 데이터를 스택에 넣어줌  
    + 재귀함수를 빠져 나와 backtrack을 할 때는 스택에 넣어 두었던 임시 데이터를 pop 해야 함  
    + 또한 스택은 재귀 알고리즘을 반복적 형태(iterative)를 통해서 구현할 수 있음  
+ 웹 브라우저 방문기록 (뒤로가기)
+ 실행 취소 (undo)
+ 역순 문자열 만들기
+ 수식의 괄호 검사 (연산자 우선순위 표현을 위한 괄호 검사)
    + Ex) 올바른 괄호 문자열(VPS, Valid Parenthesis String) 판단하기
+ 후위 표기법 계산


[출처] https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html

