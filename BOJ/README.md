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