### Greedy Algorithm

- a.k.a 탐욕 알고리즘
- 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법을 의미함.

-----

#### 그리디 알고리즘을 사용해야 하는 문제
< Activity Selection Problem >
+ 문제 이해
  + 한 사람이 최대한 많이 할 수 있는 Activity 수와 종류를 구해보자.
  + 각 활동들은 시작시간과 종료시간이 주어져 있음.
  + 한 Acitivity가 종료되어야 다른 Activity를 시작할 수 있음.
<br><br/>
+ 문제 예시: 한 강의실에서 여러 개의 수업을 하려고 할 때 한 번에 가장 많은 수업을 할 수 있는 경우를 고르는 문제, 10원, 50원, 100원이 있을 때 최소 동전으로 교환하는 문제, 문자열 합치기(문자열들의 길이가 주어지고, 한 줄에 모든 문자열을 합칠 때 필요한 최소비용을 출력하는 문제)

<img src="https://media.vlpt.us/post-images/cyranocoding/ddc56d10-b228-11e9-89af-8fc0a61dbc3e/1DmVqtxbxeihu-J8a49OLRA.png" width="500" height="700"></img><br/>
<br/>
+ 해결 방법 제안
  1) 첫 번째 활동은 가장 먼저 끝나는 것을 선택하는 것이 현재 단계에서의 가장 최선의 선택 -> end[]를 기준으로 오름차순 정렬한 후(끝나는 시간이 같은 경우 시작 시간을 기준으로 정렬함), 가장 먼저 시작하는 'D'를 시작함.
  2) D가 끝난 후, 그 시점에서 가장 먼저 끝낼 수 있는 활동을 찾음. -> E를 선택
  3) E가 끝난 후, 2)의 과정을 반복함.
<br><br/>
+ Greedy가 잘 작동하기 위한 조건
    1) Greedy choice property: 앞의 선택이 이후의 선택에 영향을 주지 않는 조건
    2) Optimal Substructure: 문제에 대한 최종 해결 방법이 sub problem에 대해서도 최적 문제 해결 방법이었다는 조건
   
-----

<그 외 Greedy를 적용할 수 있는 문제들>
- MST, Minimum Spanning Tree
- 거스름돈 문제
- 분할 가능 배낭 문제
- Dijkstra Algorithm
- Kruskal Algorithm

---

<그리디 알고리즘의 장단점>
- 장점: 계산 속도가 빠름
- 단점: 항상 최적해를 보장하는 것은 아님. 근사해 추정을 위해 사용함.

-----

[참고 문헌]  
1) https://www.zerocho.com/category/Algorithm/post/584ba5c9580277001862f188  
2) https://velog.io/@cyranocoding/%EB%8F%99%EC%A0%81-%EA%B3%84%ED%9A%8D%EB%B2%95Dynamic-Programming%EA%B3%BC-%ED%83%90%EC%9A%95%EB%B2%95Greedy-Algorithm-3yjyoohia5
