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
<summray>01Ÿ��</summary>

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