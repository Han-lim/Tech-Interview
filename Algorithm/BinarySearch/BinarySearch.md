### Binary Search

- "정렬되어 있는" 배열에서 데이터를 찾으려 시도할 때, 탐색의 범위를 절반씩 줄여가며 찾아가는 Search 방법
- 분할 정복 기법을 응용한 방법으로 정렬되어 있을 때만 사용 가능한 방법임을 명심!
- 시간복잡도: O(log n)

-----
#### 알고리즘을 설계하는 요령
(1) 배열의 중간에 있는 임의의 값을 선택하여 찾고자 하는 값 X와 비교한다.  
(2) X가 중간 값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로, X가 중간값보다 크면 배열의 우측을 대상으로 다시 탐색한다.  
(3) 동일한 방법으로 다시 중간의 값을 임의로 선택하고 비교한다.  
(4) 해당 값을 찾을 때까지 이 과정을 반복한다.  

<br></br>
- 종료 조건: 원하는 값을 찾으면 종료, 탐색하고자 하는 배열이 더 이상 존재하지 않으면, 찾고자 하는 값이 배열에 존재하지 않으므로 탐색을 종료함.

<img src="https://mblogthumb-phinf.pstatic.net/MjAyMDA5MDJfMTQ2/MDAxNTk4OTgxNTc0NzYz.KxIVK8jH7PKaUSxAS5ayxbbFdfJaWOjDQ3I7uoQqf-Ug.Y95s-LtTPg0JR3JN0NO8M7_uYVXt3Gv4R3-adDAo7Ycg.PNG.qbxlvnf11/233C703B577E34840E.png?type=w800"></img><br/>

----

#### 재귀 함수로 구현한 이진 탐색
```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)
```
    >>> 4

    # sample input
    # 10 7
    # 1 3 5 7 9 11 13 15 17 19

#### 반복문으로 구현한 이진 탐색
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우 인덱스 반환
        if array[mid] == target:
            return mid
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재 X')
else:
    print(result + 1)
```        
    >>> 4

    # sample input
    # 10 7
    # 1 3 5 7 9 11 13 15 17 19

