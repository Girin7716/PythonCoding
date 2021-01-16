# 백준 사이트 문제 풀이

## Q17298

<details>
<summary>오큰수</summary>

- 링크 : https://www.acmicpc.net/problem/17298
- 풀이 방법
  - 스택과 우선순위 큐를 사용해서 풀었다.
  - 앞에서부터 숫자를 읽어오면서 스택이 비어있을 경우 스택에 해당 index를 push해주고, 그 다음 숫자를 읽는다.
  - 이때, 스택의 제일 윗 숫자와 그 다음 숫자를 비교해서 만약 스택의 제일 윗 숫자가 더 작다면 pop()을 해준 뒤 우선순위 큐에 (stack에서 pop된 index, 읽어온 숫자)를 넣어준다.
  - 위 과정을 반복한다.
  - 위 과정이 끝난 후, (stack에 남아 있는 인덱스,-1)를 우선순위 큐에 넣어준다.
  - 그 후, 우선순위 큐를 꺼내면서 값을 출력한다.(인덱스 우선)
- 더 좋은 방법
  - stack안에는 해당 값의 index가 들어가야한다. 처음 입력했을 때 몇번째 index에 위치한 값인지를 넣어야 한다는 말이다. 다시 주어진 예제를 본다면 3 5 2 7에서 처음에 3의 index인 0을 push하고 5에 해당하는 index 1을 넣어줄 때에는 결과 리스트의 index 0에 해당하는 값을 5로 바꿔주고 stack에서는 pop시킨 후에 5에 해당하는 index 1을 push해주면 된다.
  
    ```python
    import sys 
    N = int(sys.stdin.readline()) 
    input = list(map(int, sys.stdin.readline().split()))
    stack = [] 
    result = [-1 for _ in range(N)] 
    stack.append(0) i = 1 
    while stack and i < N: 
        while stack and input[stack[-1]] < input[i]: 
            result[stack[-1]] = input[i] 
            stack.pop() 
        stack.append(i) 
        i += 1 
    for i in range(N): print(result[i], end = " ")
    ``` 
  - 출처: https://suri78.tistory.com/49 [공부노트]

</details>

---

## Q1655

<details>
<summary>가운데를 말해요</summary>

- 링크 : https://www.acmicpc.net/problem/1655
- 풀이 방법
  - 우선순위 큐를 사용하여 중간 값을 기준으로 낮은 값은 max_heap으로 저장하고, 큰 값은 min_heap으로 저장한다. 이때, max_heap의 root가 중간 값으로 생각한다.
  - 새로운 데이터를 push할때 max_heap과 min_heap의 원소 개수가 다르면 max_heap에 넣고, 그 외에는 min_heap에 넣어준다.
  - 그 후, 각각의 heap에의 root를 비교해서 이때 max_heap(즉 left)가 min_heap(즉 right)보다 클 경우 서로의 원소를 바꿔서 저장한 뒤, max_heap의 root를 출력하면 된다.
  <br/>
  ![Q1655](./readme_img/Q1655.JPG)

</details>

---

## Q1300

<details>
<summary>K번째 수</summary>

- 링크 : https://www.acmicpc.net/problem/1300
- 풀이 방법
  - K번째의 숫자를 알아야한다.
  - 이분탐색으로 mid보다 낮은 숫자의 개수를 알아낼 수 있다.
    - 각 row에서 mid보다 낮은 숫자의 개수는 mid//i(이때 i는 1~N)이다.
    - 이 모든 개수를 더하면 mid라는 숫자는 몇번째 위치한지 알 수 있다.
  - 이때, 개수가 같은 숫자가 있을 수 있는데 이때는 최솟값을 찾아야 하므로 result에 mid를 저장한 다음 end = mid - 1 해서 계속 진행한다.
- Binary Search가 끝나면 result를 출력한다.

</details>

---

## Q1753

<details>
<summary>최단경로</summary>

- 링크 : https://www.acmicpc.net/problem/1753
- 풀이 방법
  - 최단경로를 구하는 알고리즘은 대표적으로 플로이드-워셜 과 다익스트라가 있다. 
    - 이 둘의 차이점은 <br/>
    플로이드-워셜의 경우 '모든 지점에서의 다른 모든 지점까지의 최단 경로'를 구할때 사용하며, graph[a][b] = w 이런식으로 배열을 사용하며, *O(N<sup>3</sup>)*이다.<br/>
    다익스트라의 경우 '시작 지점(한 지점)에서의 다른 모든 지점까지의 최단 경로'를 구할때 사용하며, graph[a].append((b,w)) 이런식으로 리스트를 사용하며, *O(ElogV)*이다.
  - 문제에서는 '시작 지점에서 다른 모든 지점까지의 최단 경로'를 구해야하므로 다익스트라를 이용하여 문제를 풀었다.
  - 다익스트라 구현
    - 변수 키워드
      - graph[a].append((b,w)), distance = [INF] *(N+1), heapq(우선순위 큐)
      - 처음으로, 우선순위 큐에 (0,start)를 넣는다.(자기 자신의 거리는 0)
      - 그 후, q가 빌때까지 while문을 돌면서 우선순위 큐에서 꺼낸 원소(dist,now)와 연결된 노드들의 거리들을 체크한다.
        - 현재 distance[next[0]](즉, start에서 next[0]까지의 직진 거리 혹은 그 전에 저장되어 있던 최소 비용 거리)와 cost(즉,dist + next[1], 돌아가서 가는 거리(now...next))를 비교하여 cost가 더 적을경우 distance[next[0]]에 대입 후 우선순위 큐에 (cost,해당 노드 번호)를 넣어준다.

</details>

---

## Q17144

<details>
<summary>미세먼지 안녕!</summary>

- 링크 : https://www.acmicpc.net/problem/17144
- 풀이 방법
  - 전형적인 구현 문제이다.
    - python3로 돌리면 시간초과가 뜨고, pypy로 돌리니까 통과했다.
  - 커다란 로직은 아래와 같다.
    - 미세먼지확산() <br/>
    공기청정기 작동() <br/>
    - 이렇게 위 작동이 1초
    - 이걸 T초 동안 돌리자
  - 각각의 함수의 로직들은 문제에 나와있으므로 그걸 그대로 구현했다.
  - move_dirty() == 미세먼지확산()
    - 이 같은 경우 주어진 graph의 원소를 하나씩 검사하면서 먼지가 있다면, 4방향을 검사하며 이때 퍼질 수 있는 방향을 세어야하며, 만약 퍼질 수 있다면 rem[nx][ny]에 퍼지는 양(==diffusion)을 더해준다.
    - 모든 원소를 마무리하면 graph에 rem을 옮겨준다.
  - air_cleaner() == 공기청정기 작동()
    - 위에는 반시계, 아래는 시계 방향으로 옮겨주어야한다.
    - 나같은 경우 옮기기 위해 rem이라는 큐를 선언 후 0(기계에서 나온 공기)를 넣은 후, 옮겨갈 다음 좌표를 큐에 넣고 해당 좌표에다가 큐를 pop()한 값을 넣음으로써 회전시켰다.

</details>

---

## Q1967

<details>
<summary>트리의 지름</summary>

- 링크 : https://www.acmicpc.net/problem/1967
- 풀이 방법
  - 주어진 트리의 root에서 bfs()를 시도하여 가장 최장 거리에 있는 노드 번호를 찾는다.
  - 그 후, 최장 거리에 있는 노드로 부터 다시 bfs()를 시도하여 가장 거리가 먼 값을 출력하면 트리의 지름이 가장 길다고 할 수 있다.
  - bfs를 할때 자기자신->노드->자기자신의 길이가 가장 큰 값을 가질 경우 잘못된 값이 나오므로 visited을 따로 두어 이러한 경우를 방지한다.

</details>

---

## Q1916

<details>
<summary>최소비용 구하기</summary>

- 링크 : https://www.acmicpc.net/problem/1916
- 풀이 방법
  - 하나의 노드에서 다른 노드까지의 최소 비용을 구하는 문제이므로 다익스트라 알고리즘을 이용하여 해결하였다.
  - 주어진 start 노드로 다익스트라 알고리즘을 돌린 후, start 노드에서 다른 모든 노드들까지의 최소 비용이 구해진 distance 리스트에서 distance[end]를 출력해주면 start->end의 최소 비용을 구할 수 있다.

</details>

---

## Q1043

<details>
<summary>거짓말</summary>

- 링크 : https://www.acmicpc.net/problem/1043
- 풀이 방법
  - 문제에서 '당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.' 라는 말을 보고 Disjoint Set(서로소 집합)을 통해 문제를 해결해야겠다는 생각을 했다.
  - 각각의 파티에 참여하는 사람들을 같은 그룹으로 묶은 후(Disjoint Set), 진실을 알고 있는 사람들의 번호도 아까 과정에서 형성된 parent를 이용해 find 연산을 통해 번호를 root로 바꿔준다.
  - 그 후, 각각의 파티의 사람들을 보며 진실을 알고 있는 그룹인 known_people안에 해당 root를 가지고 있으면(== 같은 그룹이면) 그 파티는 과장된 이야기를 할 수 있는 파티가 아니므로 제외해서 수를 세야한다.

</details>

---

## Q1238

<details>
<summary>파티</summary>

- 링크 : https://www.acmicpc.net/problem/1238
- 풀이 방법
  - 각각의 학생들의 왕복하는 길의 최단 시간을 구해야한다. 그러므로 start 노드 -> 다른 모든 노드의 최단 거리를 구해야하므로 다익스트라를 떠올렸다.
  - 하지만, 왕복이므로 'start 노드 -> 다른 모든 노드'와 다른 모든 노드 -> start 노드' 이 2개의 최단 거리를 모두 알아야 왕복의 최단 거리를 알 수 있다.
  - 이를 해결하고자, 주어진 그래프와 주어지는 그래프의 역방향 그래프를 만들어 각각 start 노드에서 다익스트라 알고리즘을 수행하여 만들어지는 distance 리스트 2개를 더하여 가장 큰 값을 출력하면 'N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.'를 구할 수 있다.

</details>

---

## Q15663

<details>
<summary>N과 M (9)</summary>

- 링크 : https://www.acmicpc.net/problem/15663
- 풀이 방법
  - 'N개의 자연수 중에서 M개를 고른 수열'를 구하는 것이므로 from itertools import permutations를 이용하여 구한 뒤 해당 값을 정렬 후 출력하였다.

</details>

---

## Q15650

<details>
<summary>N과 M (2)</summary>

- 링크 : https://www.acmicpc.net/problem/15650
- 풀이 방법
  - '1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열'이므로 from itertools import combinations를 이용하여 구한 뒤 출력하였다.
  - 1~N까지의 리스트를 만든 후 combinations(리스트,M)을 한 뒤 해당 내용을 출력하면 된다.

</details>

---

## Q1504

<details>
<summary>특정한 최단 경로</summary>

- 링크 : https://www.acmicpc.net/problem/1504
- 풀이 방법
  - 1번 노드에서 시작하여 주어진 두 정점을 거치면서 N번 노드로 가는 최단 경로를 가야하므로 다익스트라를 떠올렸다.
  - 1번노드 에서 두 정점 v1,v2를 거쳐 N번 노드로 가는 최단 경로는 두가지 경우가 나온다.
    - 1 → v1 → v2 → n
    - 1 → v2 → v1 → n
  - 다익스트라 알고리즘은 start node에서 다른 모드 노드까지의 최단 경로를 구하므로 이에 대한 최소 비용을 저장한 distance 리스트를 가지고 구할 수있다.
  
    ```python
    one = dijkstra(1)
    ```
    ```python
    rem_v1 = dijkstra(v1)
    ```
    ```python
    rem_v2 = dijkstra(v2)
    ```
    - one 은 '1에서 다른 모든 노드로 가는 최소 비용'이 저장된 리스트이다.
    - rem_v1 은 'v1에서 다른 모든 노드로 가는 최소 비용'이 저장된 리스트이다.
    - rem_v2 는 'v2에서 다른 모드 노드로 가는 최소 비용'이 저장된 리스트이다.
  - 위에서 구한 리스들로 1에서 출발하여 v1,v2를 거쳐 n으로 가는 최소비용을 구할 수 있다.
    ```python
    result = min(one[v1]+rem_v1[v2]+rem_v2[N],one[v2]+rem_v2[v1]+rem_v1[N])
    print(result if result < INF else -1)
    ``` 

</details>

---

## Q2263

<details>
<summary>트리의 순회</summary>

- 링크 : https://www.acmicpc.net/problem/2263
- 참고 : https://whereisend.tistory.com/112
- 풀이 방법
  - 문제에서 주어진 inorder와 postorder를 바탕으로 preorder를 구해야한다.
  - preorder는 VLR(value-left-right)형식으로 순회하며 즉 해당 트리의 root를 먼저 도착한다.
  - 그러므로, print(root) → left_tree → right_tree로 진행해야하며, 각각의 트리(부분 트리)들을 순회할때 그에 맞는 inorder의 부분트리와 postorder의 부분트리도 알기위해 변수로 해당 트리의 inorder start, end 와 postorder start, end를 주었다.
  - ![Q2263](./readme_img/Q2263.JPG)

</details>