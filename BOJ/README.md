# ���� ����Ʈ ���� Ǯ��

## Q17298

<details>
<summary>��ū��</summary>

- ��ũ : https://www.acmicpc.net/problem/17298
- Ǯ�� ���
  - ���ð� �켱���� ť�� ����ؼ� Ǯ����.
  - �տ������� ���ڸ� �о���鼭 ������ ������� ��� ���ÿ� �ش� index�� push���ְ�, �� ���� ���ڸ� �д´�.
  - �̶�, ������ ���� �� ���ڿ� �� ���� ���ڸ� ���ؼ� ���� ������ ���� �� ���ڰ� �� �۴ٸ� pop()�� ���� �� �켱���� ť�� (stack���� pop�� index, �о�� ����)�� �־��ش�.
  - �� ������ �ݺ��Ѵ�.
  - �� ������ ���� ��, (stack�� ���� �ִ� �ε���,-1)�� �켱���� ť�� �־��ش�.
  - �� ��, �켱���� ť�� �����鼭 ���� ����Ѵ�.(�ε��� �켱)
- �� ���� ���
  - stack�ȿ��� �ش� ���� index�� �����Ѵ�. ó�� �Է����� �� ���° index�� ��ġ�� �������� �־�� �Ѵٴ� ���̴�. �ٽ� �־��� ������ ���ٸ� 3 5 2 7���� ó���� 3�� index�� 0�� push�ϰ� 5�� �ش��ϴ� index 1�� �־��� ������ ��� ����Ʈ�� index 0�� �ش��ϴ� ���� 5�� �ٲ��ְ� stack������ pop��Ų �Ŀ� 5�� �ش��ϴ� index 1�� push���ָ� �ȴ�.
  
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
  - ��ó: https://suri78.tistory.com/49 [���γ�Ʈ]

</details>

---

## Q1655

<details>
<summary>����� ���ؿ�</summary>

- ��ũ : https://www.acmicpc.net/problem/1655
- Ǯ�� ���
  - �켱���� ť�� ����Ͽ� �߰� ���� �������� ���� ���� max_heap���� �����ϰ�, ū ���� min_heap���� �����Ѵ�. �̶�, max_heap�� root�� �߰� ������ �����Ѵ�.
  - ���ο� �����͸� push�Ҷ� max_heap�� min_heap�� ���� ������ �ٸ��� max_heap�� �ְ�, �� �ܿ��� min_heap�� �־��ش�.
  - �� ��, ������ heap���� root�� ���ؼ� �̶� max_heap(�� left)�� min_heap(�� right)���� Ŭ ��� ������ ���Ҹ� �ٲ㼭 ������ ��, max_heap�� root�� ����ϸ� �ȴ�.
  <br/>
  ![Q1655](./readme_img/Q1655.JPG)

</details>

---

## Q1300

<details>
<summary>K��° ��</summary>

- ��ũ : https://www.acmicpc.net/problem/1300
- Ǯ�� ���
  - K��°�� ���ڸ� �˾ƾ��Ѵ�.
  - �̺�Ž������ mid���� ���� ������ ������ �˾Ƴ� �� �ִ�.
    - �� row���� mid���� ���� ������ ������ mid//i(�̶� i�� 1~N)�̴�.
    - �� ��� ������ ���ϸ� mid��� ���ڴ� ���° ��ġ���� �� �� �ִ�.
  - �̶�, ������ ���� ���ڰ� ���� �� �ִµ� �̶��� �ּڰ��� ã�ƾ� �ϹǷ� result�� mid�� ������ ���� end = mid - 1 �ؼ� ��� �����Ѵ�.
- Binary Search�� ������ result�� ����Ѵ�.

</details>

---

## Q1753

<details>
<summary>�ִܰ��</summary>

- ��ũ : https://www.acmicpc.net/problem/1753
- Ǯ�� ���
  - �ִܰ�θ� ���ϴ� �˰����� ��ǥ������ �÷��̵�-���� �� ���ͽ�Ʈ�� �ִ�. 
    - �� ���� �������� <br/>
    �÷��̵�-������ ��� '��� ���������� �ٸ� ��� ���������� �ִ� ���'�� ���Ҷ� ����ϸ�, graph[a][b] = w �̷������� �迭�� ����ϸ�, *O(N<sup>3</sup>)*�̴�.<br/>
    ���ͽ�Ʈ���� ��� '���� ����(�� ����)������ �ٸ� ��� ���������� �ִ� ���'�� ���Ҷ� ����ϸ�, graph[a].append((b,w)) �̷������� ����Ʈ�� ����ϸ�, *O(ElogV)*�̴�.
  - ���������� '���� �������� �ٸ� ��� ���������� �ִ� ���'�� ���ؾ��ϹǷ� ���ͽ�Ʈ�� �̿��Ͽ� ������ Ǯ����.
  - ���ͽ�Ʈ�� ����
    - ���� Ű����
      - graph[a].append((b,w)), distance = [INF] *(N+1), heapq(�켱���� ť)
      - ó������, �켱���� ť�� (0,start)�� �ִ´�.(�ڱ� �ڽ��� �Ÿ��� 0)
      - �� ��, q�� �������� while���� ���鼭 �켱���� ť���� ���� ����(dist,now)�� ����� ������ �Ÿ����� üũ�Ѵ�.
        - ���� distance[next[0]](��, start���� next[0]������ ���� �Ÿ� Ȥ�� �� ���� ����Ǿ� �ִ� �ּ� ��� �Ÿ�)�� cost(��,dist + next[1], ���ư��� ���� �Ÿ�(now...next))�� ���Ͽ� cost�� �� ������� distance[next[0]]�� ���� �� �켱���� ť�� (cost,�ش� ��� ��ȣ)�� �־��ش�.

</details>

---

## Q17144

<details>
<summary>�̼����� �ȳ�!</summary>

- ��ũ : https://www.acmicpc.net/problem/17144
- Ǯ�� ���
  - �������� ���� �����̴�.
    - python3�� ������ �ð��ʰ��� �߰�, pypy�� �����ϱ� ����ߴ�.
  - Ŀ�ٶ� ������ �Ʒ��� ����.
    - �̼�����Ȯ��() <br/>
    ����û���� �۵�() <br/>
    - �̷��� �� �۵��� 1��
    - �̰� T�� ���� ������
  - ������ �Լ��� �������� ������ ���������Ƿ� �װ� �״�� �����ߴ�.
  - move_dirty() == �̼�����Ȯ��()
    - �� ���� ��� �־��� graph�� ���Ҹ� �ϳ��� �˻��ϸ鼭 ������ �ִٸ�, 4������ �˻��ϸ� �̶� ���� �� �ִ� ������ ������ϸ�, ���� ���� �� �ִٸ� rem[nx][ny]�� ������ ��(==diffusion)�� �����ش�.
    - ��� ���Ҹ� �������ϸ� graph�� rem�� �Ű��ش�.
  - air_cleaner() == ����û���� �۵�()
    - ������ �ݽð�, �Ʒ��� �ð� �������� �Ű��־���Ѵ�.
    - ������ ��� �ű�� ���� rem�̶�� ť�� ���� �� 0(��迡�� ���� ����)�� ���� ��, �Űܰ� ���� ��ǥ�� ť�� �ְ� �ش� ��ǥ���ٰ� ť�� pop()�� ���� �������ν� ȸ�����״�.

</details>

---

## Q1967

<details>
<summary>Ʈ���� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/1967
- Ǯ�� ���
  - �־��� Ʈ���� root���� bfs()�� �õ��Ͽ� ���� ���� �Ÿ��� �ִ� ��� ��ȣ�� ã�´�.
  - �� ��, ���� �Ÿ��� �ִ� ���� ���� �ٽ� bfs()�� �õ��Ͽ� ���� �Ÿ��� �� ���� ����ϸ� Ʈ���� ������ ���� ��ٰ� �� �� �ִ�.
  - bfs�� �Ҷ� �ڱ��ڽ�->���->�ڱ��ڽ��� ���̰� ���� ū ���� ���� ��� �߸��� ���� �����Ƿ� visited�� ���� �ξ� �̷��� ��츦 �����Ѵ�.

</details>

---

## Q1916

<details>
<summary>�ּҺ�� ���ϱ�</summary>

- ��ũ : https://www.acmicpc.net/problem/1916
- Ǯ�� ���
  - �ϳ��� ��忡�� �ٸ� �������� �ּ� ����� ���ϴ� �����̹Ƿ� ���ͽ�Ʈ�� �˰����� �̿��Ͽ� �ذ��Ͽ���.
  - �־��� start ���� ���ͽ�Ʈ�� �˰����� ���� ��, start ��忡�� �ٸ� ��� ��������� �ּ� ����� ������ distance ����Ʈ���� distance[end]�� ������ָ� start->end�� �ּ� ����� ���� �� �ִ�.

</details>

---

## Q1043

<details>
<summary>������</summary>

- ��ũ : https://www.acmicpc.net/problem/1043
- Ǯ�� ���
  - �������� '�翬��, � ����� � ��Ƽ������ ������ ���, �Ǵٸ� ��Ƽ������ ����� �̾߱⸦ ����� ���� �����̴� ���������̷� �˷����� �ȴ�. �����̴� �̷� ���� ��� ���ؾ� �Ѵ�.' ��� ���� ���� Disjoint Set(���μ� ����)�� ���� ������ �ذ��ؾ߰ڴٴ� ������ �ߴ�.
  - ������ ��Ƽ�� �����ϴ� ������� ���� �׷����� ���� ��(Disjoint Set), ������ �˰� �ִ� ������� ��ȣ�� �Ʊ� �������� ������ parent�� �̿��� find ������ ���� ��ȣ�� root�� �ٲ��ش�.
  - �� ��, ������ ��Ƽ�� ������� ���� ������ �˰� �ִ� �׷��� known_people�ȿ� �ش� root�� ������ ������(== ���� �׷��̸�) �� ��Ƽ�� ����� �̾߱⸦ �� �� �ִ� ��Ƽ�� �ƴϹǷ� �����ؼ� ���� �����Ѵ�.

</details>

---

## Q1238

<details>
<summary>��Ƽ</summary>

- ��ũ : https://www.acmicpc.net/problem/1238
- Ǯ�� ���
  - ������ �л����� �պ��ϴ� ���� �ִ� �ð��� ���ؾ��Ѵ�. �׷��Ƿ� start ��� -> �ٸ� ��� ����� �ִ� �Ÿ��� ���ؾ��ϹǷ� ���ͽ�Ʈ�� ���÷ȴ�.
  - ������, �պ��̹Ƿ� 'start ��� -> �ٸ� ��� ���'�� �ٸ� ��� ��� -> start ���' �� 2���� �ִ� �Ÿ��� ��� �˾ƾ� �պ��� �ִ� �Ÿ��� �� �� �ִ�.
  - �̸� �ذ��ϰ���, �־��� �׷����� �־����� �׷����� ������ �׷����� ����� ���� start ��忡�� ���ͽ�Ʈ�� �˰����� �����Ͽ� ��������� distance ����Ʈ 2���� ���Ͽ� ���� ū ���� ����ϸ� 'N���� �л��� �� ���� ���µ� ���� ���� �ð��� �Һ��ϴ� �л��� �������� ���Ͽ���.'�� ���� �� �ִ�.

</details>

---

## Q15663

<details>
<summary>N�� M (9)</summary>

- ��ũ : https://www.acmicpc.net/problem/15663
- Ǯ�� ���
  - 'N���� �ڿ��� �߿��� M���� �� ����'�� ���ϴ� ���̹Ƿ� from itertools import permutations�� �̿��Ͽ� ���� �� �ش� ���� ���� �� ����Ͽ���.

</details>

---

## Q15650

<details>
<summary>N�� M (2)</summary>

- ��ũ : https://www.acmicpc.net/problem/15650
- Ǯ�� ���
  - '1���� N���� �ڿ��� �߿��� �ߺ� ���� M���� �� ����'�̹Ƿ� from itertools import combinations�� �̿��Ͽ� ���� �� ����Ͽ���.
  - 1~N������ ����Ʈ�� ���� �� combinations(����Ʈ,M)�� �� �� �ش� ������ ����ϸ� �ȴ�.

</details>

---

## Q1504

<details>
<summary>Ư���� �ִ� ���</summary>

- ��ũ : https://www.acmicpc.net/problem/1504
- Ǯ�� ���
  - 1�� ��忡�� �����Ͽ� �־��� �� ������ ��ġ�鼭 N�� ���� ���� �ִ� ��θ� �����ϹǷ� ���ͽ�Ʈ�� ���÷ȴ�.
  - 1����� ���� �� ���� v1,v2�� ���� N�� ���� ���� �ִ� ��δ� �ΰ��� ��찡 ���´�.
    - 1 �� v1 �� v2 �� n
    - 1 �� v2 �� v1 �� n
  - ���ͽ�Ʈ�� �˰����� start node���� �ٸ� ��� �������� �ִ� ��θ� ���ϹǷ� �̿� ���� �ּ� ����� ������ distance ����Ʈ�� ������ ���� ���ִ�.
  
    ```python
    one = dijkstra(1)
    ```
    ```python
    rem_v1 = dijkstra(v1)
    ```
    ```python
    rem_v2 = dijkstra(v2)
    ```
    - one �� '1���� �ٸ� ��� ���� ���� �ּ� ���'�� ����� ����Ʈ�̴�.
    - rem_v1 �� 'v1���� �ٸ� ��� ���� ���� �ּ� ���'�� ����� ����Ʈ�̴�.
    - rem_v2 �� 'v2���� �ٸ� ��� ���� ���� �ּ� ���'�� ����� ����Ʈ�̴�.
  - ������ ���� ������� 1���� ����Ͽ� v1,v2�� ���� n���� ���� �ּҺ���� ���� �� �ִ�.
    ```python
    result = min(one[v1]+rem_v1[v2]+rem_v2[N],one[v2]+rem_v2[v1]+rem_v1[N])
    print(result if result < INF else -1)
    ``` 

</details>

---

## Q2263

<details>
<summary>Ʈ���� ��ȸ</summary>

- ��ũ : https://www.acmicpc.net/problem/2263
- ���� : https://whereisend.tistory.com/112
- Ǯ�� ���
  - �������� �־��� inorder�� postorder�� �������� preorder�� ���ؾ��Ѵ�.
  - preorder�� VLR(value-left-right)�������� ��ȸ�ϸ� �� �ش� Ʈ���� root�� ���� �����Ѵ�.
  - �׷��Ƿ�, print(root) �� left_tree �� right_tree�� �����ؾ��ϸ�, ������ Ʈ��(�κ� Ʈ��)���� ��ȸ�Ҷ� �׿� �´� inorder�� �κ�Ʈ���� postorder�� �κ�Ʈ���� �˱����� ������ �ش� Ʈ���� inorder start, end �� postorder start, end�� �־���.
  - ![Q2263](./readme_img/Q2263.JPG)

</details>

---

## Q17070

<details>
<summary>������ �ű��1</summary>

- ��ũ : https://www.acmicpc.net/problem/17070
- Ǯ�� ���
  - �־��� ���ǿ� ���� bfs�� �����ϸ� ť�� pop������ x2,y2 ��ǥ�� N-1,N-1�϶� result�� �÷� bfs�� ������ result�� ����Ѵ�.
  - ������, �̷��� ������� ����Ž������ �� ��� ���̽��� ��� �ð��ʰ��� �߻��ϸ�, c++ ��� ����� �ȴ�.
  - ã�ƺ��� ���̽㿡�� ������ ����ϱ����ؼ��� dp�� Ǯ����Ѵ�.
  - dp�� ���߿� Ǯ�����.
  - python �ڵ带 c++�� �����ϴ� ����� �� �ʿ䰡 �ִٴ� ���� ���ݴ� ��������.
  - ![Q17070](./readme_img/Q17070.JPG)

</details>

---

## Q11725

<details>
<summary>Ʈ���� �θ� ã��</summary>

- ��ũ : https://www.acmicpc.net/problem/11725
- Ǯ�� ���
  - Ʈ���� root�� 1�̹Ƿ� 1�� ������ bfs�� Ž���ϸ鼭 ����� ������ parent�� visited ����Ʈ�� ������ �� ����ϸ� �ȴ�.

</details>

---

## Q1991

<details>
<summary>Ʈ�� ��ȸ</summary>

- ��ũ : https://www.acmicpc.net/problem/1991
- Ǯ�� ���
  - �׷����� dictionary �ڷ����� �̿��Ͽ� �������.
    ```python
    N = int(input())
    graph = {}
    for i in range(N):
        a,b,c = input().split()
        graph[a] = graph.get(a,[]) + [b]
        graph[a] = graph.get(a, []) + [c]
    ```
    ![1991](./readme_img/1991.JPG)
  - preorder, inorder, postorder�� ��������� �Լ��� ���������� �����������δ� node�� '.'�� ��� �����ϵ��� �ߴ�.
  - preorder �� VLR(value-left-right)
  - inorder �� LVR(left-value-right)
  - postorder �� LRV(left-right-value)

</details>

---

## 18119

<details>
<summary>�ܾ� �ϱ�</summary>

- ��ũ : https://www.acmicpc.net/problem/18119
- Ǯ�� ���
  1. ó������ �������´�� �־��� �ܾ �ؾ���� �ܾ �ִ��� Ȯ���ϴ� ������ naive�� �ڵ带 § �� �õ������� TLE
  ```python
  import sys
  input = sys.stdin.readline

  N, M = map(int,input().split())
  words = [input() for _ in range(N)]

  forget = []

  for i in range(M):
      num, word = input().split()
      answer = 0
      if num == '1':  # �ؾ������
          forget.append(word)
          for j in words:
              check = False
              for k in forget:
                  if k in j:
                      check = True
                      break
              if check == False:
                  answer += 1
          print(answer)
      else:   # ����س���
          forget.remove(word)
          for j in words:
              check = False
              for k in forget:
                  if k in j:
                      check = True
                      break
              if check == False:
                  answer += 1
          print(answer)
  ``` 
  2. �־��� ���ڿ��� �ؾ���� ���ڰ� �ִ��� Ȯ���ϴµ� �ð��� ���� �ɷȳ� �;� �̺�Ž������ �̸� Ž���Ͽ� Ȯ���غ� -> TLE
  ```python
  from bisect import bisect_left, bisect_right

  # ���� [left_value,right_value]�� �������� ������ ��ȯ�ϴ� �Լ�
  def count_by_range(a, left_value, right_value):
      right_index = bisect_right(a,right_value)
      left_index = bisect_left(a,left_value)
      return right_index - left_index

  N,M=map(int,input().split())
  words = [list(input()) for _ in range(N)]
  for word in words:
      word.sort()
  forget = []
  #print(count_by_range(a,5,5))
  for i in range(M):
      num, fg = input().split()
      answer = 0
      if num == '1':  # ��Ա�
          forget.append(fg)
          for word in words:
              check = False
              for f in forget:
                  if count_by_range(word,f,f) !=0:
                      check = True
              if check == False:
                  answer+=1
          print(answer)
      else:   # ���
          forget.remove(fg)
          for word in words:
              check = False
              for f in forget:
                  if count_by_range(word,f,f) !=0:
                      check = True
              if check == False:
                  answer+=1
          print(answer)
  ```
  3. ��Ʈ����ŷ���� �ذ�
    - alpha ����Ʈ�� 'a'�� 0��°, 'z'�� 25��° �ε����̸� �־��� ���ڿ����� ������ ���ڿ����� �ش� ���ڸ� ���� ��� �־��� ���ڿ��� ���� ���� index�� alpha[�ش� ���� ����]�� �߰����ش�.
      ```python
      alpha = [[] for _ in  range(26)]
      for i in range(N):
          words = set(input())
          for word in words:
              alpha[ord(word)-ord('a')].append(i)
              print(word,ord(word)-ord('a'))
      ``` 
      - ex>���� �������� ó�� �־��� 'apple'�� ���, 'a'==0, 'p'==15, 'l'==11,'e'==4�̴�. �׷��Ƿ� alpha[0]=[0], alpha[15]=[0],alpha[11]=[0],alpha[4]=[0]�� �ȴ�.<br/> �ι�°�� �־��� actual�� ��� 'a'==0,c=='2',t=='19','u'==20,'l'==11�̴�. �׷��Ƿ� ù��° ���ڿ��� ����� �����ؼ� alpha����Ʈ�� ��Ÿ���� alpha[0]=[0,1],alpha[2]=[1],alpha[4]=[0],alpha[11]=[0,1],alpha[15]=[0],alpha[19]=[1],alpha[20]=[1]�� �ȴ�.
    - check ����Ʈ�� �־��� ���ڿ����� ����� ������ ������ ������� ��Ÿ���� ����Ʈ�̴�.
    - answer�� ��� ó������ ���ڸ� ���� �˰� �����Ƿ� �־����� ���ڿ��� ������ N����ŭ ���ڿ��� �˰��ִ�.
      - �׷���, ���ڿ��� ��԰ų� ����س��� �ൿ�� �� ������ �̷��� answer���� + Ȥ�� -�� �ȴ�. ��, �ൿ �ϳ��Ҷ����� answer ���� ��ȭ�� �Ͼ�� �� ���� ������ָ� �ȴ�.
    - �������� �ش� ���ĺ��� ������ �ִ� ���ڿ��� �˱� ���ؼ� alpha ����Ʈ�� �̿��Ѵ�. �̶�, �ش� ���ڿ��� ���� �ؾ���� ���ڰ� ���� ����(check[i]==0)�� ���, ���ڸ� ��Ծ�������� answer-=1�Ͽ� �˰� �ִ� ���� ������ �ٿ��� �� check[i]+=1�� �Ͽ� �ش� ���ڿ����� �𸣴� ���� ������ �߰����ش�.
      ```python
      if o == '1':    # �����
      for i in alpha[ord(x)-ord('a')]:
          if check[i] == 0:
              answer-=1
          check[i]+=1
      ```
     - ����س� ��쵵 ����� ���� ���������̴�. �׷��� ����� �س����Ƿ� ����� ���� �ٸ��� ���� check[i]-=1�� ���� �� check[i]==0�� ��� answer+=1�� ���ָ� �ȴ�.
     ```python
    else:   #����س�
      for i in alpha[ord(x)-ord('a')]:
          check[i] -= 1
          if check[i] == 0:
              answer +=1
     ```

</details>

---

## Q9184

<details>
<summary>�ų��� �Լ� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/9184
- Ǯ�� ���
  - ����Լ��� DP�� �ٲٴ� �����̴�.
  - ����Լ��� �����ߴٸ� �޸����̼��� �̿��Ͽ� DP�� �ٲ� �� �ִ�.
    - �޸����̼� : ��Ϳ��� �� �� Ǭ ������ �� ����� ������ ���Ҵٰ� ���߿� ������ ������ Ǯ��� �� �� �̹� ������ ���� ��ȯ.
      ```python
      def w(a,b,c):
          ## �����~~~
          if dp[a][b][c] != 0:
            return dp[a][b][c]
          ## �����~~~
      ```
  - ��, dp��� ��� ����� ������ �� ���� ��ŭ�� ũ���� �迭�� ���� ��, �ش� ����� �����Ѵ�. �׷��� ���� �ڵ�ó�� �Ȱ��� ������ ���� ��� ����� ���������ʰ� �ٷ� �迭���� ���� �ҷ����� ���.

</details>

---

## Q1904

<details>
<summary>01Ÿ��</summary>

- ��ũ : https://www.acmicpc.net/problem/1904
- Ǯ�� ���
  - 1���� �����ؼ� ���� �־ �������ٺ��� ��ȭ���� �߰���
    - f(n) = f(n-1) + f(n-2), f(1)=1, f(2)=2
    - �״�� n�� �ݺ��ؼ� bottom-up���� ���ߴ�.

</details>

---

## Q9461

<details>
<summary>�ĵ��� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/9461
- Ǯ�� ���
  - ![Q9461](./readme_img/9461.JPG)
  - �� �׸����� ���� N��° �ﰢ���� ������ (N-1)��° �ﰢ���� ���� + (N-5)��° �ﰢ���� �����̶�� ��Ģ�� ã�� �� �ִ�.
    - ��ȭ�� : f(N) = f(N-1)+f(N-5)
    - ��ȭ�Ŀ��� N-5�� �����Ƿ� f(5)������ �̸� ���� �־��־���Ѵ�.

</details>

---

## Q2579

<details>
<summary>��� ������</summary>

- ��ũ : https://www.acmicpc.net/problem/2579
- Ǯ�� ���
  - ���������� ������ ������ ����� ��ƾ��Ѵ�. �׷��� ���� ������ ����� ��Ҵٰ� �����ϰ� ��ȭ���� �������Ҵ�.
  - �׷����, ���� 2���� ��찡 ���´�.
    1. N-1�� ����� ��� �� ���(�̷��� ���, N-2�� ����� ������ �ȵȴ�.)
    2. N-2�� ����� ��� �� ���
  - ��ȭ��
    - dp[i] = max(dp[i-2]+data[i],dp[i-3]+data[i]+data[i-1])
  - ��ȭ���� �̷��ϹǷ� dp���� dp[0],dp[1],dp[2]�� ���� �̸� �� �־�� �ϸ�, N==1�϶��� N==2�϶��� case�� ���� ó��������Ѵ�.

</details>

---

## Q2156

<details>
<summary>������ �ý�</summary>

- ��ũ : https://www.acmicpc.net/problem/2156
- Ǯ�� ���
  - ![2156](./readme_img/2156.JPG)

</details>

---

## Q11053

<details>
<summary>���� �� �����ϴ� �κ� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/11053
- Ǯ�� ���
  - LIS(Longest Increasing Subsequence)�� ���ϴ� �����̴�.
    - LIS�� ���ϴ� ������ ũ�� 2������ ������ �ִ�.
      1. DP�� �ذ�(�̹� ���������� DP�� �ذ�)
      2. �̺�Ž������ �ذ�(���� �����ؾ���)
  - DP ����Ʈ�� �ش� ���ڱ����� �ִ� ���̶�� �����Ѵ�.
  - �� ��, �־��� �Է��� ���ʴ�� �տ������� �˻��ϸ鼭 �ִ��� ���ڸ� DP�� �����Ѵ�. �׷��� ���ؼ��� 2�� for���� ����ؼ� 1)������ ���ڵ��� dp���� �����ϸ�, 2)������ ���ں��ٴ� Ŀ���Ѵ�.
    ```python
    for i in range(N):
      for j in range(i):
          if arr[i] > arr[j]:
              result[i] = max(result[i],result[j]+1)
    ```

</details>

---

## Q11054

<details>
<summary>���� �� ������� �κ� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/11054
- Ǯ�� ���
  - Q11053 ������ �����ϴ�.
  - �־��� �Է¿��� LIS�� ���̸� ���ϰ�, �̸� �Ųٷ� ���� �ٽ� LIS�� ���� �� �� ����Ʈ�� ��ģ��. �� ��, ���� ū ���� ������ ������ -1�� ���ش�.(-1�� �ߺ��� �����Ƿ� ���ִ� ����).
  - ![11054](./readme_img/11054.JPG)

</details>

---

## Q2565

<details>
<summary>������</summary>

- ��ũ : https://www.acmicpc.net/problem/2565
- Ǯ�� ���
  - A �����뿡 ���ؼ� ������ �� ��, B �����뿡 ���ؼ� LIS�� �ִ� ���̸� ���Ͽ� N - (LIS �ִ� ��)�� �ϸ� �����ؾ��� �������� ������ ���´�.
  - ![2565](./readme_img/2565.JPG)
    - ����� �κ��� ���ܾ��� ��������.

</details>

---

## Q9251

<details>
<summary>LCS</summary>

- ��ũ : https://www.acmicpc.net/problem/9251
- Ǯ�� ���
  - ���ĺ��� ������ (���� �밢��+1)
  - ���ĺ��� �ٸ��� ���� ������ ���� ū ���� �����´�.
  - ![9251](./readme_img/9251.JPG)

</details>

---

## Q1912

<details>
<summary>������</summary>

- ��ũ : https://www.acmicpc.net/problem/1912
- Ǯ�� ���
  - dp[i] : i��°���� ���� �� �ִ� �� �� ���� ū �� ����.
  - dp[i]�� �׷��Ƿ� data[i]�� �����ؼ� �� �������� �ִ��� �̰ų� data[i]�̰ų� �� �� �� ū ���̴�.
  - dp[i] = max(dp[i-1]+data[i],data[i])

</details>

---

## Q9935

<details>
<summary>���ڿ� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/9935
- Ǯ�� ���
  - ó���� result ����Ʈ(stack���� ����Ұ���)�� bomb(���ڿ� ��ź)�� ���̸�ŭ �־��� ���ڿ��� �տ������� ��´�.
  - �� ��, result ���ÿ��� ���� ���ʿ������� bomb���̸�ŭ Ȯ���ؼ� �ش� ���ڿ��� bomb�� �Ȱ����� bomb�� ���̸�ŭ pop ���ش�.
  - �� ����, result���� ���� ���ڸ� ��µ� ������ ���� ������ٸ� �� ������ �ݺ��ϸ�, ������ �����(index�ʰ�) break�Ͽ� result�� ����Ѵ�.

</details>

---

## Q14938

<details>
<summary>�����׶���</summary>

- ��ũ : https://www.acmicpc.net/problem/14938
- Ǯ�� ���
  - �÷��̵� ���� �˰����� �̿��Ͽ� Ǯ����.
  - �� ��忡�� �ٸ� ���� �� �� �ִ� �ִ� �Ÿ��� ���� ����Ʈ D�� ���� ��, �ϳ��� row�� �˻縦 �ϸ鼭 �̵��Ÿ� m ������ ������ items�� result�� ���Ͽ� ������ row�� ���� result�� ���� �� ������ �� �� ���� ū ���� ������ش�.<br/><br/><br/>
  
  - ���ͽ�Ʈ��� ���� Ǯ���!

</details>

---

## Q1005

<details>
<summary>ACM Craft</summary>

- ��ũ : https://www.acmicpc.net/problem/14938
- Ǯ�� ���
  - ���� ������ �������ִٴ� ������ ���������� ���÷ȴ�.
  - delays��� dp ����Ʈ�� �������.
    - �� ����Ʈ�� i��° ��尡 ���� �� �ִ� �ִ� delays �ð��� �����ϰ� �ִ�. ��, ���������� �ϸ鼭 now�� ����Ǿ��ִ� ������ ���� Ȯ���Ѵ�. (���� �������ִ� ���� �� ���� �����(now)�� �ִ� + �ڽ��� �Ǽ� ���) �� ū ���� �����ϸ� �ȴ�. �Ʒ��� �� ��ȭ���̴�.
  ```python
  delays[i - 1] = max(delays[i - 1], delays[now - 1] + rem[i - 1])
  ```

</details>

---

## Q1197

<details>
<summary>�ּ� ���д� Ʈ��</summary>

- ��ũ : https://www.acmicpc.net/problem/1197
- Ǯ�� ���
  - �ּ� ���д� Ʈ���� ���ϴ� �����̴�.
  - �ּ� ���д� Ʈ���� ���ϴ� ����� ��ǥ���� ������δ� ũ�罺Į �˰���� ���� �˰������ִ�.
  - ���� ���⼭ ũ�罺Į �˰����� ����Ͽ� ������ Ǯ����.
  - edges�� ����� �������� �������� �����Ͽ���(�� �κ��� ���� �ð��� ���� ��Ƹ����Ƿ� ũ�罺Į �˰����� �ð����⵵�� O(ElogE)�̴�)
  - �� ��, cost�� ���� edge���� Ȯ���ϸ鼭 �ش� edge�� ������ �ִ� edge��� ����Ŭ���� �˻��ϰ� �ƴҰ�� ���д�Ʈ���� �߰����ش�.
  - �� ��, �� ����� ������ش�.

</details>

---

## Q1806

<details>
<summary>�κ���</summary>

- ��ũ : https://www.acmicpc.net/problem/1806
- Ǯ�� ���
  - �κ���, ~~���� ���ڸ��� �� ������ �˰����� ���÷ȴ�.
  - ���������� �κ���(S) �̻��� �� �� ���� ª�� ���̸� ���϶�� �Ͽ����Ƿ�, �� ������ �˰����� �̿��Ͽ� �κ����� ���ϸ鼭 �ش� ���� S �̻��� ��� �ش� ���̸� �����ϰ� �ּ� ���̸� ����ϸ� �ȴ�.

</details>

---

## Q2056

<details>
<summary>�۾�</summary>

- ��ũ : https://www.acmicpc.net/problem/1806
- Ǯ�� ���
  - �������� + dp
  - ������ �� : �׷����� �������� ���, �׳� ���� �����ɸ� �׷����� ���� ����ϸ� ��.
  - ��ȭ�� : dp[i] = max(dp[i],dp[now]+data[i-1][0])
  - dp�� i�� �۾��� ������ �� �ɸ��� �ִ� �ð��̴�.(�׷��Ƿ�, ������ �ִ� �ð��� (���� �۾��� ���� �۾�+i�� �ɸ��� �ð�) �� ū ���� �����.)

</details>

---

## Q2252

<details>
<summary>�� �����</summary>

- ��ũ : https://www.acmicpc.net/problem/2252
- Ǯ�� ���
    - �� �л����� ���� ū������ �˷� �־����� �̸� ���� ���������� ���÷ȴ�.
    - Ű�� ���� �л��� Ű�� ū �л��� ����Ű�� �������� �׷����� �����ϰ�, �� ����� indegree�� ������� ��, ���� ������ �ϸ� �ȴ�. �̶�, ��� ���� ���� ���������� ��� �ƹ��ų� ����ص� �ǹǷ�, ����2�� ���� ��� 4 2 3 1 �̳� 3 4 1 2 �̳� ���� �����̴�.(�ֳ��ϸ� 4 2�� ������ 3 1�� ��Ű�� �ǰ� �� �ܿ��� ����� ���� �����̴�.)

</details>


---

## Q2467

<details>
<summary>���</summary>

- ��ũ : https://www.acmicpc.net/problem/2467
- Ǯ�� ���(���� Ǭ ���)
  <details>
  <summary>�ڵ�</summary>

  ```python
  import sys
  input = sys.stdin.readline

  N = int(input())
  data = list(map(int,input().split()))

  start = 1
  end = N-1
  result = [data[0],data[1]]

  near_zero = int(1e9)
  for i in range(N):
    start = i
    end = N-1

    while start <= end:
        mid = (start + end) // 2

        if data[i] + data[mid] == 0:
            result[0] = data[i]
            result[1] = data[mid]
            near_zero = data[i] + data[mid]
            break
        elif data[i] + data[mid] < 0:
            start = mid + 1
        else:  # data[i]+data[mid] > 0
            end = mid - 1
        if i == mid:
            continue
        if abs(near_zero) > abs(data    [i] + data[mid]):
            near_zero = data[i] + data[mid]
            result[0] = data[i]
            result[1] = data[mid]


  print(result[0],result[1])
  ```

  </details>


  - �ð� ������ 1���̰�, N = 10,000�̹Ƿ� �� ������ ��� O(NlogN)�� Ǯ����Ѵ�. �׷��� ������ ������ �̺� Ž���̾���.
  - �־��� ����Ʈ�� ó������ �˻��ϸ鼭 �ٸ� ����� ã������ �̺�Ž���� �̿��Ͽ� Ž���ϰ��Ͽ���. 
  - �׷��� �� ���� 0�� ���� �״�� ����ϰ�,
  - 0���� ���� ��� start = mid + 1 ���ְ�
  - 0���� Ŭ ��� end = mid - 1 ���ָ鼭,
  - near_zero���� 0�� ������ �ش� ���� �������ش�.
  - �׷���, �̷������� Ǯ���Ͽ� ���������� ����ó���� �Ǿ����� �ٸ� ������ ���Ͽ� ��û ���� �ð��� �ɸ��ٴ� ���� Ȯ���Ͽ���, �ٸ� ������� Ǯ�̸� ���� �������ͷ� �ذ��Ͽ��ٴ� ���� �˰� �������ͷ� �ٽ� Ǯ�� ���Ҵ�.

- Ǯ�� ���(��������)
  <details>
  <summary>�ڵ�</summary> 

  ```python
  import sys
  input = sys.stdin.readline

  N = int(input())
  data = list(map(int,input().split()))

  left = 0
  right = N-1

  near_zero = int(1e9)
  result = [data[0],data[1]]
  while left < right:
    sum_value = data[left] + data[right]
    if abs(near_zero) > abs(sum_value):
        near_zero = sum_value
        result[0] = data[left]
        result[1] = data[right]
    if sum_value > 0:
        right -= 1
    elif sum_value < 0:
        left += 1
    else:   # sum_value == 0
        break
  print(result[0],result[1])
  ```

  - ���������Ǿ��ִ� ����Ʈ�� �Է����� �־����Ƿ�, left = 0, right = N-1�� �Ͽ� �ش� �ε����� data ���� ���� ���� 0�� ����� ���� �����Ѵ�.
  - ���� ���� 0���� ũ��, ����� ���ڸ� �ٿ����ϹǷ� right -=1
  - ���� ���� 0���� ������, ������ ���ڸ� �ٿ����ϹǷ� left -=1
  - ���� ���� 0�̸�, �ش� data�� ���


  </details>

</details>

---

## Q2567

<details>
<summary>������ - 2</summary>

- ��ũ : https://www.acmicpc.net/problem/2568
- Ǯ�� ���
  - https://www.acmicpc.net/problem/2467 �� ����Ʈ ����� ������.
  - �ٵ� ȿ������ ����� �ƴѵ�
  - 320ms �ɸ��� ������ ���� Ž���غ���.

</details>

---

## Q2623

<details>
<summary>�������α׷�</summary>

- ��ũ : https://www.acmicpc.net/problem/2623
- Ǯ�� ���
  - >������ ���ϱ� ���ؼ��� ���� ������ ������ �Ѵ�.
  - �� �������� ���� ������ �̿��Ͽ� Ǯ��߰ڴٰ� �����ߴ�.
  - ������ �Է��� ���÷� ��� �׷����� �Ʒ��� ���� �����Ѵ�.
    ![2623](./readme_img/2623.JPG)
  - ���� ���� ������ �����ϸ�, queue���� pop�ɶ����� �ش� ���� result�� �����Ѵ�.
  - ���������� ������ result�� ������ ������ �ľ��ϰ� ������ N�̶� �ٸ��ٸ�(��, ����) 0, �� �ܿ��� result�� ����ϸ� �ȴ�.

</details>

---

## Q1717

<details>
<summary>������ ǥ��</summary>

- ��ũ : https://www.acmicpc.net/problem/1717
- Ǯ�� ���
  - �ܼ��� union-find �����̴�
  - �ٸ� ��͸� ����� ��� ���ȣ���Ѱ踦 Ǯ���־���Ѵ�.
    ```python
    import sys
    sys.setrecursionlimit(10**5)
    ```
  - ����, parent�� ��� ������ ���־������ ����� �� �־���.(�������� �˰� �־��� �ڵ�� ��ξ����� ������)
    - ex1> ��� ���� X(parent�� ��� update ����)
      ```python
      def find_parent(parent,x):
        if parent[x] != x:
          return find_parent(parent,parent[x])
        return parent[x]
      ``` 
    - ex2> ��� ���� o(parent�� ��� update ��)
      ```python
      def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]
      ```
      - ����
      > 100000 100000<br>
      > 0 0 1<br>
      > 0 0 2<br>
      > 0 0 3<br>
      > 0 0 4<br>
      > ��<br>
      > 0 0 99999<br>
      > 0 0 100000<br>
      �̷������� �Է��� ������ ex1>�� ��� �־ǿ��� O(N^2)�� �ɸ�����, ex2>�� ���� �뷫 O(NlogN)�̴�.
</details>

---

## Q1759

<details>
<summary>��ȣ �����</summary>

- ��ũ : https://www.acmicpc.net/problem/1759
- Ǯ�� ���(���� Ǭ ���)
  - combinations�� �̿��Ͽ� Ǯ����.
  - �־��� ���ڿ��� ������������ ���� �� �� combinations(data,L)�� �ϸ� L��ŭ�� ��� ����� ���� ���´�.
  - �ش� ����� ���� �ϳ��� �˻��ϸ鼭 ������ �ϳ� �̻��̸鼭 ������ 2���̻��� ��� ������ָ� �ȴ�. �̶� �־��� ���ڿ��� ������������ ���� �� �� combinations �����ϱ� �˻��ϴ� �͵� �������� ������� �˻��ؼ� ������ش�.

  <details>
  <summary>�ڵ�</summary>

  ```python
  # ��ȣ �����
  from itertools import combinations
  import sys
  input = sys.stdin.readline

  L, C = map(int,input().split())
  data = sorted(list(input().split()))
  comb = list(combinations(data,L))

  for c in comb:
    cnt = 0
    for i in range(L):
        if c[i] in 'aeiou':
            cnt +=1
    if cnt >=1 and L-cnt >=2:
        print(''.join(list(c)))

  ```

  </details> 

</details>

---

## Q1987

<details>
<summary>���ĺ�</summary>

- ��ũ : https://www.acmicpc.net/problem/1987
- Ǯ�̹��(bfs)
  - bfs�� �� �� queue�� set���� ���� �ϴ°� �����ϴٴ� ����� �˾Ҵ�.(q.append -> q.add)
  - ���̸� ���ϴ� �����϶��� bfs�� dfs���� ������.
  - �ڵ�
  ```python
  def bfs():
    mx = 0
    q = set()
    q.add((0,0,board[0][0]))
    while q:
        x,y,sentence = q.pop()
        mx = max(mx,len(sentence))
        if mx == 26:
            return 26
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] in sentence:
                continue
            q.add((nx,ny,sentence+board[nx][ny]))
    return mx

  R,C = map(int,input().split())
  board = []
  for i in range(R):
      board.append(list(input()))

  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  print(bfs())
  ```

- Ǯ�̹��(dfs)
  - ���ĺ� ���� ������ ������ ��Ʈ ����ŷ�� ���÷��� ȿ�������� �� ������ �ؾ��Ѵ�
    - alpha = [0] * 26
  - 
  ```python
  alpha[table[nx][ny]] = 1
  solve(nx,ny,l+1)
  alpha[table[nx][ny]] = 0
  ```
  �̷������� ��ȭ-���-�ǵ����� �������� �Ѵ�.
  - �ڵ�
    ```python
    def solve(x,y,l):
    global ans
    ans = max(ans,l)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and alpha[table[nx][ny]] == 0:
            alpha[table[nx][ny]] = 1
            solve(nx,ny,l+1)
            alpha[table[nx][ny]] = 0

    R, C = map(int,input().split())
    table = []
    for i in range(R):
      table.append(list(map(lambda x:ord(x)-65, input().rstrip())))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    alpha = [0] * 26
    ans = 0
    alpha[table[0][0]] = 1
    solve(0,0,1)

    print(ans)
    ``` 

</details>

---

## Q5014

<details>
<summary>��ŸƮ��ũ</summary>

- ��ũ : https://www.acmicpc.net/problem/5014
- Ǯ�� ���
  - bfs�� �����ϸ鼭 �ö� �� ������ loc+U�� ť�� �ְ�, �ش� ���� �湮�ߴٴ� �ǹ̷� �� ���� �� �� �ִ� �ּ� ��ư ���� �ִ´�.
  - ����������, ������ �� ������ loc-D�� ť�� �ְ�, �ش� ���� �湮�ߴٴ� �ǹ̷� �� ���� �� �� �ִ� �ּ� ��ư ���� �ִ´�.
  - �� ��, visited[G]�� -1(�ʱⰪ)�̸� 'use the stairs'�� ����ϰ�, �ƴ� ��� visited[G]���� ����ϸ� �ȴ�.

</details>

---

## Q2573

<details>
<summary>����</summary>

- ��ũ : https://www.acmicpc.net/problem/5014
- Ǯ�� ���(ó�� Ǭ ���(�޸� �ʰ�))
  <details>
  <summary>�ڵ�</summary>
  
  ```python
  import sys
  import copy
  from collections import deque
  input = sys.stdin.readline

  N, M = map(int,input().split())

  board = []
  for i in range(N):
    board.append(list(map(int,input().split())))

  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  def after_year():
    temp = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
                        cnt+=1
                temp[i][j] = board[i][j] - cnt
                if temp[i][j] < 0:
                    temp[i][j] = 0
    return temp

  def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        visited[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny] == 0 and board[nx][ny]!=0:
                q.append((nx,ny))

  # return 0,1,2 -> 0 : all melt, 1 : one thing, 2 : more than 2
  def is_separate():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                bfs(i,j,cnt)

    if cnt > 2:
        return 2
    else:
        return cnt

  time = 0
  while(True):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    board = after_year()
    time+=1
    flag = is_separate()
    if flag == 0:
        print(0)
        break
    elif flag == 2:
        print(time)
        break
  ```

  </details> 

  - ó������ �ϴ� Ŀ�ٶ� �������δ� �Ʒ��� ���� ��������. 
    1. ������ ���δ�(after_year()) (�̶�, ������ ���ÿ� ��´ٴ� ���� �����ؾ���)(board�� ũ�Ⱑ �Ȱ��� temp�� ���� ���� ���� ���� ���� �� temp ��ȯ)
    2. ���� ������� �и��Ǿ��ִ��� Ȯ���Ѵ�(is_separate)
  - ������, �� ������ �����ϸ鼭 ���к��ϰ� 2���� �迭�� �����ϸ鼭(after_year���� temp, bfs���� visited) �޸� �ʰ��� �޾Ҵ�.

- Ǯ�� ���2(pypy���, python �ð��ʰ�)
  <details>
  <summary>�ڵ�</summary>

  ```python
  from collections import deque
  import sys
  input = sys.stdin.readline

  N,M=map(int,input().split())
  board = []
  for i in range(N):
    board.append(list(map(int,input().split())))

  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  def check_near_zero(rem):
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
                        cnt += 1
                rem.append((i,j,cnt))

  def melting(rem):
    while rem:
        x,y,cnt = rem.popleft()
        board[x][y] -= cnt
        if board[x][y] <= 0:
            board[x][y] = 0

  def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = cnt

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0 and board[nx][ny]!=0:
                visited[nx][ny] = cnt
                q.append((nx,ny))


  def is_separate():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and visited[i][j] == 0:
                cnt+=1
                bfs(i,j,cnt)

    return cnt

  time = 0

  while(True):
    time += 1
    rem = deque()   # near_zero ���� ť
    check_near_zero(rem)
    still = deque()# 1�� �� ������ �ִ� ��ǥ ���� ť
    melting(rem)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    flag = is_separate()

    if flag >= 2:
        print(time)
        break
    elif flag == 0:
        print(0)
        break

  ```

  </details> 
  
  - �׷���, 2���� ����Ʈ�� �ٿ������� �Ʒ��� ���� ������ �����ߴ�.
    1. ������ ��� �� ������ �� ��ǥ������ ��ó 0�� ���� �ľ��ؼ� rem�̶�� ť�� �־��ش�. (��ǥ,��ǥ,��ó 0�� ��)
       - check_near_zero(rem) 
    2. rem�� pop�ϸ鼭 �ش� ��ǥ�� (��ó 0�� ��)�� ���ָ� �̶� ���� ������ �Ǹ� 0���� �ٲ㼭 ����.
       - melting(rem) 
    3. ���� ������ �������� bfs�� �����ϸ鼭 ������ �� ��� �̻�(flag>=2)�̸� ���� �ð��� ����ϰ�, ������ ���ٸ�(flag==0) 0�� ����Ѵ�.
       - is_separate()

- �̷��������� bfs, dfs������ python3�δ� ����ϱⰡ �����. pypy�� �� �𸣰ڴٸ� c++�� �ٲ㼭 �ϴ� ����� �������� �ʿ䰡 �ִ°� ����.

</details>


---

## Q14503

<details>
<summary>�κ� û�ұ�</summary>

- ��ũ : https://www.acmicpc.net/problem/14503
- Ǯ�� ���
  - �־��� ���ǿ� ���߾� �����ϸ� ��.
  1. ���� ��ġ�� û���Ѵ�. 
    
    ```python
    # ���� ��ġ û��
    if board[r][c] == 0:
        answer += 1
    board[r][c] = 2
    ``` 
    
  2. ���� ��ġ���� ���� ������ �������� ���ʹ������ ���ʴ�� Ž���� �����Ѵ�
    
    ```python
    check = False
    for i in range(4):
        d = turn_left(d)
        nx = r + dx[d]
        ny = c + dy[d]

        ...
    ```
  
  a. ���� ���⿡ ���� û������ ���� ������ �����Ѵٸ�, �� �������� ȸ���� ���� �� ĭ�� �����ϰ� 1������ �����Ѵ�.
    
    ```python
    if nx >=0 and nx < N and ny >= 0 and ny < M and board[nx][ny] == 0:
      r = nx
      c = ny
      check = True
      break
    ```
  b. ���� ���⿡ û���� ������ ���ٸ�, �� �������� ȸ���ϰ� 2������ ���ư���.

    ```python
    if check == True:   #û�Ҹ� �ߴٸ�
      continue
    ```
  c. �� ���� ��� û�Ұ� �̹� �Ǿ��ְų� ���� ��쿡��, �ٶ󺸴� ������ ������ ä�� �� ĭ ������ �ϰ� 2������ ���ư���.
    ```python
    else:   # û�Ҹ� ����
      # ������ ����
      if d == 0:
          nx = r + 1
          ny = c
      elif d == 1:
          nx = r
          ny = c - 1
      elif d == 2:
          nx = r - 1
          ny = c
      elif d == 3:
          nx = r
          ny = c + 1 
    ```
  d. �� ���� ��� û�Ұ� �̹� �Ǿ��ְų� ���̸鼭, ���� ������ ���̶� ������ �� �� ���� ��쿡�� �۵��� �����.
    ```python
    if board[nx][ny] == 1:  # ��
      break
    else:   # ���� ����
      r = nx
      c = ny
    ```

</details>


---

## Q7579

<details>
<summary>��</summary>

- ��ũ : https://www.acmicpc.net/problem/7579
- Ǯ�� ���
  - 0/1 ���� �����ΰ��� �˾����� Ǯ�� ���ߴ�.
  - dp[i][j] : i��° �۱��� �� j �ڽ�Ʈ�� ���� �� �ִ� �ִ� byte
  

</details>

---

## Q9252

<details>
<summary>LCS 2</summary>

- ��ũ : https://www.acmicpc.net/problem/9252
- Ǯ�� ���
  - ���̴� LCS Ǯ��ó�� ���ϸ� ��
  - ���ڿ��� �������ϸ鼭 ���� �ش� ���ڰ� �밢������ �����Ȱ��̶�� �װ��� REM�� �����Ű�� �ȴ�.

</details>

---

## Q10942

<details>
<summary>�Ӹ����?</summary>

- ��ũ : https://www.acmicpc.net/problem/10942
- Ǯ�� ���
  - �Ӹ�����̶� '121', '1223221'�� ���� ����� �Ȱ��� ���ڸ� �ǹ��Ѵ�.
  - N<=2,000, M<=1,000,000 �ε� �̸� 1�ʾȿ� �ذ��ؾ��ϹǷ� ó�� �� ������ O(NM)�� �Ұ����ϰ�, �׷��� O(MlogN)���� �ذ��ؾ��Ѵٴ� ������ �����.
  - �׷��� logN�� ���� �̺� Ž���� ���÷����� �̺� Ž�����δ� ��� �ؾ����� ���� ����� �״��� DP�� ���÷ȴ�.
  - DP[i][j]
    - j��° ���ں��� i���� ���ڰ� �縰��� ���������� ���� True False�� �����Ѵ�.
  - ![10942](./readme_img/10942.JPG)
    - ó�� dp ���̺��� �����ϸ鼭 �׸� ���.
    - ������ dp�� �����ϸ� �Ʒ��� ���� ������ �ȴ�.
  - DP�� ���� False�� �ʱ�ȭ �� �� row 1�� row 2�� ���� ���Ѵ�.
  -  row 3���ʹ� �Ʒ��� ������ ������� True�� �ٲ��ش�.     
    ```python
    if data[j] == data[j+i-1] and dp[i-2][j+1] == 1:  #isTrue?
      dp[i][j] = 1
    ```  

    - data[j] == data[j+i-1] 
      - ���� �հ� ���� ���� ���ڰ� �Ȱ�����
    - dp[i-2][j+1] == 1
      - ���� �� ���ڿ� ���� �� ���ڸ� ������ ���ڵ��� �Ӹ���� ���ڶ��

  - ������ DP ���̺��� �������� ����� �ϸ� �ȴ�.
    - print(dp[E-S+1][S])
      - [E-S+1] => �˻��� ���ڵ��� ����
      - [S] => ���° ������ �����ΰ�

</details>

---

## Q2917

<details>
<summary>���� ��ɲ�</summary>

- ��ũ : https://www.acmicpc.net/problem/2917
- Ǯ�̹��
  - ��û�ظ̴�. �и� Ǯ���Ѱ� ������ �ð��ʰ�, Ʋ�Ƚ��ϴٰ� ��� ���´�.
  - ������ ��Ȯ�� �����ؾ��Ѵ�.
  - �ϴ�, ������ ������(1���̻�)! ����� �Ѹ�! ���θ��� �ϳ�
  >���� ������ ���̶� ���찡 �̵��ϴ� ��� ĭ���� ������ �Ÿ��� �ּڰ��� ���� ū ����̴�. ��, ���θ��� �ִ� ĭ�� ����� �Ϻ��̱� ������ ������ �Ÿ��� ����ؾ� �Ѵ�.
  - ���� ������ �ǹ̸� ����� �ľ��ؾ��Ѵ�
  - ��, ���찡 ���θ����� ���� ������ ��ΰ� �ִ�. �׷��� ��ε��� ������ ��ǥ��� �̷�����ְ�, �ش� ��ǥ���� ���� ��������� �ּ� �Ÿ����� �������ִ�.
  - �̷��� ��ο� �� ��ο� �ش��ϴ� ��ǥ �� ��������� �ּ� �Ÿ����� ���� ���� ���� �ش� ��ο��� ������ ���� ��������� �����̰�, �� ���� ����� ��ǥ���̶� �����Ѵ�.
  - ������ ��� �� �� ��ǥ���� ���� ū ���� ã�� �����̴�.
  - �˰���
    - �켱 �������� �������� bfs�� ���� �� ��ǥ�� �������� �ּ� �Ÿ��� ���Ѵ�.
    - �� ��, ������ ��ġ���� ���ͽ�Ʈ�� �����µ� �̶�, �켱���� ť�� ���� ����(-����� ��ǥ��(�������� �Ÿ��� ����� ��),��ǥ1,��ǥ2)�̴�. �̶�, ����� ��ǩ���� �������� �Ÿ��� ���� �� ���� ã�� ������ MaxHeap�� ����Ѵٴ� �ǹ̷� ����� ��ǥ���� ��ȣ�� ������ ���Ͽ� �־��ش�.
    - �׸���, �湮�ߴ� ���� �湮�� �ʿ�� �����Ƿ� visited�̶�� ����Ʈ�� �����.
      - visited�� �ش� ��ǥ�� �˻��� ��ε��� ��ǥ�� �� �ش� ��ǥ������ �ּڰ��� ������.
    - �� ��, visited[���θ� ��ǥ1][���θ� ��ǥ2]�� ����ϸ� ���θ� ��ǥ������ ��ε��� ��ǥ�� �� �ּڰ��� ���� �� �ִ�.

</details>


---

## Q11049

<details>
<summary>��� ���� ����</summary>

- ��ũ : https://www.acmicpc.net/problem/11049
- Ǯ�� ���
  - �и� ����µ� �ʹ� ��ƴ�. ó���� dp ������ �߸��ؼ� ����ߴ�.
  - dp[i][j] : i��° ��Ŀ��� j��° ��ı����� �ּҺ��
  - ��ȭ�� : dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]+(d[i-1]*d[k]*d[j]))
    - �밢������ �ö󰡸鼭 ���� ����

</details>


---

## Q11437

<details>
<summary>LCA</summary>

- ��ũ : https://www.acmicpc.net/problem/11437
- Ǯ�� ���
  - ó�� ���������� ����� �� ������ �־�����. �̸� �������� ������ �׷���(tree)�� �����.
  - �� ��, tree���� �θ�-�ڽ��� ���踦 �˾ƾ��ϹǷ� bfs�� ���� �ش� ����� depth�� �ش� ����� parent �ľ��ߴ�.
  - ���������� �� ������ �Է����� �־�����, �� ������ �θ� ������������ �ݺ��ϸ� ���� �ٸ��ٸ�, depth�� �� �������� parent���� ���ϸ� �ȴ�.
  - python3 �ð��ʰ�, pypy3 ���
  - python3�� ����� ������� �ִµ� ��� �Ѱ��� �𸣰ڴ�.

</details>

---

## Q13460

<details>
<summary>���� Ż��2</summary>

- ��ũ : https://www.acmicpc.net/problem/13460
- Ǯ�� ���
  - �ùķ��̼�+bfs �����̾���.
  - �ٸ� ť�� �ߺ��Ǵ� ���� ���� ���� bfs�� set()�� �̿��Ͽ� �־��� ������ �����ϸ� �ڵ带 �ۼ��ߴ�.
  - ���� ���̽����� ���� ���� �� �ִ�.
    - �������, ������ ���ÿ� ���ų�, ������ ������ Ƚ���� 11�� �Ѱų�...
  - �ٸ� ������� Ǯ�̸� ���� bfs�� ������ visited[nx][ny][bx][by]�� ����� �ش� ��ǥ�� red�� blue�� �� ���� ������ ť�� ���� �ʾҴ�. visited�� �� Ȱ���ؾ߰ڴ�.(2,3,4... �迭)

</details>


---

## Q12100

<details>
<summary>2048(easy)</summary>

- ��ũ : https://www.acmicpc.net/problem/12100
- Ǯ�̹��
  - bfs�� Ǯ����.
  - ó������ �������´�� Ǯ������, `0 0 8` �� ����Ʈ���� �������� �������ٸ� `8 0 0`�� �Ǿ���ϳ� �̸� ����ġ���ϰ� `0 8 0`���� ���� �ڵ带 �ھ�����.
  - �����϶��� ������ ť�� ����Ͽ� �� ���� ������ 0�� �ƴ� ���ڵ��� ť�� �־��ش�. �� ��, ������ �� �ִ� ���ڰ� ������ �̸� ��ġ�� �̸� ����Ʈ temp�� ���� �� ���� ĭ�� 0�� ä����.
  - �� ��, ����Ʈ�� �ƴ� ������ ����Ʈ rem���� ���� �� now�� ���ؼ� �ٸ��ٸ� bfs�� ť�� �־��־���.
  - �ٵ� ���� Ǭ ����� 996ms�� ������ �� Ǭ ������� 100ms���������� ���´�.
  - �� ȿ������ ����� ã�ƺ����ҵ�.


</details>


---