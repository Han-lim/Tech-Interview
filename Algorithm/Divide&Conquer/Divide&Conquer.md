### Divide and Conquer
- 문제를 나눌 수 없을 때까지 나누어서(Divide) 각각 풀면서(Conquer) 다시 합병하여 문제의 답을 얻는 알고리즘

-----
#### 알고리즘을 설계하는 요령
(1) Divide: 문제가 분할이 가능한 경우, 2개 이상의 문제로 나눔  
(2) Conquer: 나누어진 문제가 여전히 분할이 가능하면, 또 다시 Divide를 수행함. 그렇지 않으면 문제를 품.  
(3) Combine: Conquer한 문제들을 Combine하여 원래 문제의 답을 얻음.  
<br></br>
- 문제를 제대로 나누면 Conquer 하는 것은 쉽기 때문에 Divide를 제대로 하는 것이 제일 중요함.
- 분할정복 알고리즘은 재귀 알고리즘이 많이 사용되는데, 이 점에서 분할정복 알고리즘의 효율성이 떨어질 수 있음.
- 일반 재귀 호출은 항상 문제를 한 조각과 나머지로 쪼개는 방식, 분할정복법은 항상 문제를 절반씩으로 나누는 분할 정복 알고리즘

<img src="https://t1.daumcdn.net/cfile/tistory/99BB27375D75CC2B2B"></img><br/>

----
#### 분할정복 알고리즘의 응용
1) Merge Sort  
- 시간 복잡도: O(nlogn)
- 공간 복잡도: O(n)
- 알고리즘
  + 정려할 데이터 집합의 크기가 0 또는 1이면 이미 정렬된 것으로 보고, 그렇지 않으면 데이터 집합을 반으로 나눔
  + 원래 같은 집합에서 나뉘어져 나온 데이터 집합 둘을  병합하여 하나의 데이터 집합으로 만듦. 단, 병합할 때 데이터 집합의 원소는 순서에 맞춰 정렬함.
  + 데이터 집합이 다시 하나가 될 때까지 conquer 후 combine을 반복함.
- 두 데이터 집합을 정렬하면서 합치는 방법
  + 두 데이터 집합의 크기 합만큼의 크기를 갖는 빈 데이터 집합을 생성
  + 두 데이터 집합의 첫 번째 요소들을 비교하여 작은 요소를 빈 데이터 집합에 추가함. 그리고 새 데이터 집합에 추가한 요소는 원래 데이터 집합에서 삭제함.
  + 원래 두 데이터 집합의 요소가 모두 삭제될 때까지 2번째 방법을 반복함.

<br></br>
2) Quick Sort

- 시간 복잡도  
  - 주어진 문제를 두 개의 부분 문제로 나누는 파티션 과정, 파티션에는 주어진 수열의 길이에 비례하는 시간이 걸림

  - 분할된 두 부분 문제가 비슷한 크기로 나눠진다는 보장이 없으므로 최악의 경우 O(n2)의 시간 복잡도가 나올 수 있음

  - 대부분 퀵 정렬 구현은 가능한 절반에 가까운 분할을 얻기 위해 좋은 기준을 뽑는 다양한 방법들을 사용

  - 평균적으로 부분 문제가 절반에 가깝게 나눠질 경우는 O(nlon)으로 병합 정렬과 같음

- 알고리즘
  - 각 부분 수열의 맨 처음(또는 맨 끝)에 있는 수를 기준으로 삼고, 이들보다 작은 수를 왼쪽, 큰 수를 오른쪽으로 가도록 분해  

  - 배열을 단순하게 가운데에서 쪼개는 대신, 병합 과정이 필요 없도록 한쪽의 배열에 포함된 수가 다른 쪽 배열의 수보다 항상 작도록 배열을 분할 -> 파티션(partition)이라고 부르는 단계 도입
     * 파이션은 배열에 있는 수 중 임의의 수 '기준 수(pivot)'를 지정한 후 기준보다 작거나 같은 숫자를 왼쪽, 더 큰 숫자를 오른쪽으로 보내는 과정

  <img src="https://t1.daumcdn.net/cfile/tistory/995832455D7667A91F"></img><br/>

<br></br>
3) 수열의 빠른 합
- 1부터 n까지의 합을 n개의 조각으로 나눈 뒤, 이들을 반으로 잘라 n/2개 조각들로 만들어진 부분 문제 두 개를 만듦  

- 1 ~ ![first equation](https://latex.codecogs.com/gif.latex?n%20%5Cover%202) 과 <img src="https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D%20&plus;1" width="40" height="25">~ n로 나눌 수 있음

- 첫 번째 부분은 fastSum(![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D))로 나타낼 수 있지만, 두 번째 문제는 나타낼 수 있는 방법을 생각해야 함

- (![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)+1) + ... + n  
   = (![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)+1) + (![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)+2) + ... (![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)+![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D))   // 결국, ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + .... 가 ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)번 반복되고, 1+ 2+ 3+ ... + ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)가 남게 됨  
   = ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) x ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + (1 +2 + 3 + ... + ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D))
   = ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) * ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + fastSum(![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D))
<br></br>
- fastSum(n) 
   = 2 x fastSum(![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)) + ![third](https://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cfrac%7Bn%5E2%7D%7B4%7D)  (n은 짝수)   // fastSum(![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D)) + ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) * ![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D) + fastSum(![second](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bn%7D%7B2%7D))  

<br></br>

4) 행렬의 거듭제곱
- n x n 크기의 행렬 A가 주어질 때, A의 거듭 제곱(power) Am은 A를 연속해서 m번 곱한 것  

- m이 커질수록 시간이 오래 걸리는 작업  

- 분할 정복을 적용한다면 ![fourth](https://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Csmall%20A%5Em) = ![fifth](https://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Csmall%20A%5E%5Cfrac%7Bm%7D%7B2%7D) * ![fifth](https://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Csmall%20A%5E%5Cfrac%7Bm%7D%7B2%7D)  
- 같은 문제라도 어떻게 분할하느냐에 따라 시간 복잡도 차이가 커지게 됨 (계속 분할할지, 짝수번째만 분할할지)  

- 계속해서 절반으로 나누는 알고리즘이 큰 효율 저하를 불러 오는 이유는 여러번 중복되어 계산이 되면서 시간을 소모하는 부분이 문제  

- 주어신 수열을 크기 순서대로 정렬하는 문제는 전산학에서 가장 유명한 문제 중 하나

- 정렬 문제를 해결하는 수많은 알고리즘 중 가장 널리 쓰이는 알고리즘들이 병합 정렬, 퀵 정렬

- 같은 문제를 해결하는 알고리즘이라도 어떤 식으로 분할하느냐에 따라 다른 알고리즘이 될 수 있음


-----
<분할정복을 사용하기 위한 조건>
- 문제를 둘 이상의 부분 분제로 나누는 자연스러운 방법이 있어야 함.  

- 부분 문제의 답을 조합해 원래 문제의 답을 계산하는 효율적인 방법이 있어야 함.  

----
<분할정복의 장점>
- 같은 작업을 더 빠르게 처리할 수 있음.

[참고 사이트]  
1) https://data-make.tistory.com/232

