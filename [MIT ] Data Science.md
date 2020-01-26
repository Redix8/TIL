# [MIT ] Data Science

## Chapter 1. Introduction and Optimization Problems

### Optimization Model



목적함수를 최대화 또는 최소화한다.

제한 조건을 둘 수 있다.



- knapsack problem -냅색(배낭) 문제

  - 가방 안에 들어갈 수 있는 가장 비싼 물건을 넣는다.

  - 목적함수 : 가장 비싼 물건

  - 제한 : 가방의 크기

  - 0/1 knapsack problem

    - 가져가거나, 가져가지 않거나 둘 중의 하나만 선택

    - V[i] 는 0또는 1, I[i]는 물건의 가치
  $$
      \sum_{i=0}^{n-1} V[i]*I[i].value
  $$
      제한 조건 
  $$
      \sum_{i=0}^{n-1} V[i]*I[i].weight \le w
      $$
      
    - Brute Force
  
    - 모든 Power set(멱집합 - 주어진 집합의 모든 부분집합의 집합)
      - 허용된 무게를 넘는 조합들은 제거
    - 남은것들중 가장 큰 것을 선택
      - 시간이 오래 걸리는 단점이 있다. (멱집합의 조합 개수는 $2^n$)

    - Greedy Algorithm
  
      - Knapsack이 가득 차지 않는 한 가장 좋은것(key)을 넣는다.
      - 가장 좋은것(key) 를 정의하는것이 필요
      - 알고리즘의 효율성
        - 정렬을 위한 $nlogn$ + 순회를 위한 n. 즉, $O(nlogn)$
      - 구현하기 쉽고 빠르다.
      - 최적일 수도, 아닐수도 있는 해를 구한다.
  
  - Continuous knapsack problem (연속 냅색 문제)
  
    - 일부분을 가져갈 수 있는 경우



## Chapter 2. Optimization Problems

- Brute Force 

  - 트리 구조로 이루어지는 탐색 방법을 생각해 볼수 있다.

    이 탐색 방법에서는 재귀를 이용해 트리를 구성하고 

    더이상 조건이 맞지 않을때 중단하고 그 위의 노드로 돌아간다(Back tracking)

- Greedy Algorithm

  - 구현하기 쉽고 빠른 속도를 가지고 있다.
  - 하지만 최적일 수도, 아닐수도 있는 해를 구한다.
  - 그렇기 때문에 구한 해가 얼마나 최적에 가까운지 알수 없다.

- Dynamic Programming

  - 이름에는 아무 의미도 없음.
  - Memoization : 이전 결과를 저장할 공간을 소비하는 대신 계산 시간을 절약.
  - 중복 부분 문제가 있는 경우 빠르게 해결 가능
  - ex) 피보나치 수열



## Chapter 3. Graph-theoretic Models

- what's graph
  - set of Nodes 
  - edges 
    - directed or undirected
    - weighted or unweighted
- 그래프를 표현하는 방법
  - 행렬
  - 인접리스트
- 그래프를 탐색하는법
  - 깊이 우선 탐색(DFS)
    - 재귀로 쉽게 탐색 가능
  - 너비 우선 탐색(BFS)
    - 큐(Queue)를 이용
    - 루트에서 목표노드까지 간선의 최소 개수를 찾을때 사용할 수 있다.



## Chapter 4. Stochastic Thinking

- 확률에 관한 3가지 사실
  - 항상 0~1사이의 값
  - 어떤 사건이 일어날 확률이 `p`라고 했을때 사건이 일어나지 않을 확률은 `1-p`
  - 사건이 서로 독립적이라면 모든 사건이 일어날 확률은 각 사건이 일어날 확률을 곱한것이다.
    - A : 0.5,   B: 0.4 일때  A&B 는 0.2
- 시뮬레이션 모델
  - 사건이 드물게 발생한다면, 많은 시도를 하는것이 더 좋은 추정된 확률을 얻을 수 있음
  - 시뮬레이션 모델을 사용하여 얻는 추정 확률은 실제 확률을 계산하는것 보다 간단함.



