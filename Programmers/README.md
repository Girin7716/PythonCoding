# ���α׷��ӽ� ����Ʈ ���� Ǯ��

## �������� ���� ����

<details>
<summary>Ǯ��</summary>

- participant�� key�� �ش� �̸��� ������ ����� ���� value�� �����ߴ�. �׸��Ͽ� completion���� �Ѹ� �̸��� ���Ƽ� dictionary���� ������ �� ���߿� dictionary�� value�� 1�� ���� ����� ������ �� ����� ȥ�� �������� ���� ������� �����ϰ� ����Ͽ���.

</details>

<details>
<summary>�ڵ�</summary>

```python
def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        try:
            dic[p] += 1
        except:
            dic[p] = dic.get(p, 1)

    for element in completion:
        dic[element]-=1

    for key, value in dic.items():
        if value == 1:
            answer = key
    return answer
```

</details>

---

## ��ȭ��ȣ ���

<details>
<summary>Ǯ��</summary>

  - ���ξ ã���� �� ��� ���Ḧ �ϰ� answer�� False�� �־���Ѵ�. �׷��Ƿ� �־��� phone_book ����Ʈ�� ���� ������ ������ �� ��, �տ������� �� �ڿ� �ִ� ��� ���ڿ��� �պκи��� ���Ͽ� ���� ã����� answer False�� �ְ� �����Ѵ�.
  - ���� ���Ḧ �����ʰ� ��� ������ ��� ȿ���� Ż��

</details>


<details>
<summary>�ڵ�</summary>

```python
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    length = len(phone_book)
    #print(phone_book[0]==phone_book[2][0:3])
    for i in range(length):
        #phone_book[i]
        l = len(phone_book[i])
        for j in range(i+1,length):
            if phone_book[i] == phone_book[j][0:l]:
                answer = False
                return answer
    return answer
```

</details>

---

## ¡�˴ٸ� �ǳʱ�

<details>
<summary>��ũ</summary>

-  https://programmers.co.kr/learn/courses/30/lessons/64062
</details>

<details>
<summary>Ǯ�� ���</summary>

  - ó�� Ǭ ���
    - k��ŭ�� window�� ������ ��, stones�� window��ŭ ���鼭 window�� ���� ū ���� ����Ѵ�. �̷������� stones�� ���� ���� ����� �� �� ���� ���� ���� �����̴�.
    - ������ �̴�, ��Ȯ�������� �ٸ¾Ƶ�, ȿ�������� ���ϴ�(O(N^2))�̱⶧��.
  - �ι�°�� Ǭ ���
    - O(N^2)���� �� ���� Ǯ����Ѵ�. �׷��� O(NlogN)���� Ǯ������ ����Ž���� �����ߴ�.
    - ����Ž�� ����� ����� �ǳ� �� �ֳķ� �����߰� min=1,max=200,000,000���� �� ��, stones�� ó������ ������ ���� ���� min~max ������ ���� 3�� �̻� ������ max ���� �ٿ��ְ�(max = mid), ���� ���δ� ����� ��� min���� �÷��ش�(min = mid).
    - �̷��� ������ ���ؼ�, �ᱹ ���������� max = mid �� break���� ���� while�� ������ min < max -1�� ��� Ż���ϸ� return max���ϸ� ������ ���´�.

</details>
---

## �ҷ� �����

<details>
<summary>��ũ</summary> 

- https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

</details>

<details>

<summary>Ǯ�� ���</summary>

- ó�� Ǭ ���
  - user_id�� ���ڼ��� ���� digit ����Ʈ�� �־��ش�.
  - �� ��, banned_id�� ���ҵ��� ó������ �ϳ��� ���ϸ鼭, �ش� banned_id�� ������ ������ user_id�� rem�� �־��ش�.
  - �� ����, rem���� ����Ʈ���� product�� �ϰ�, ���ҵ��� ���Ľ�Ų �� �־��ش�.
  - �� �� rem�� �ϳ��� ���鼭 �Ȱ��� id�� ������ �̸� ������� �����Ѵ�.
  - �׷��� ���Ű� ������ ���� answer�� �����̴�.
  - ������, test case5���� �ð��ʰ� �߻�.(�ٵ� �� �̻��Ѱ� �ٸ� case�鿡���� �ð��� ��û ������ ����)
  ![baduser](./readme_img/baduser.JPG)

  <details>
  <summary>�ڵ�</summary>

  ```python
  from itertools import product

  def solution(user_id, banned_id):
      digit = [[] for _ in range(9)]
      rem = []
      for u in user_id:
          digit[len(u)].append(u)
      for i in range(len(banned_id)):
          rem.append([])
          b_len = len(banned_id[i])
          for d in digit[b_len]:
              cnt = 0
              for j in range(b_len):
                  if banned_id[i][j] != '*' and banned_id[i][j] != d[j]:
                      break
                  cnt+=1
              if cnt == b_len:
                  rem[i].append(d)

      temp = []
      for i in list(product(*rem)):
          temp.append(tuple(sorted(i)))

      temp = list(set(temp))
      answer = len(temp)
      for x in temp:
          for j in range(len(i)-1):
              if x[j] == x[j+1]:
                  answer-=1
                  break
      return answer
  ```
  </details>
- �ι�°�� Ǭ ���
  - ó�� user_id�κ��� ������ �������� ���Ѵ�.
  - �� ��, �� ���ڵ��� banned_id�� ������ �������� �˻縦 �ϸ� ������ ��� �ش� candidate_users�� set���� ���� �� �ش� set�� rem ����Ʈ �ȿ� ���� ��� rem�ȿ� �־��ش�.
  - ��� �������� �˻��� ��, rem�� ���̸� ��ȯ�ϸ� �����̴�.
  - �̰Ŵ� ���1)���ٴ� ��ü������ ��������, �׽�Ʈ 5�� ����ϴ� ����̴�.
  - ![baduser2](./readme_img/baduser2.JPG)
  
  <details>

  <summary>�ڵ�</summary>

  ```python
  from itertools import permutations

  def solution(user_id, banned_id):
      rem = []
      for candidate_users in permutations(user_id, len(banned_id)):
          #print(candidate_users)
          check = True
          for i in range(len(banned_id)):
              c_len = len(candidate_users[i])
              b_len = len(banned_id[i])
              if c_len != b_len:
                  check = False
                  break
              for j in range(b_len):
                  if banned_id[i][j] == '*' or banned_id[i][j] == candidate_users[i][j]:
                      continue
                  else:
                      check = False
                      break
          if check == False:
              continue
          candidate_users = set(candidate_users)
          if candidate_users not in rem:
              rem.append(candidate_users)

      return len(rem)
  ```

  </details> 

</details>

---

## ȣ�� �� ����

<details>
<summary>��ũ</summary>

- https://programmers.co.kr/learn/courses/30/lessons/64063

</details>


<details>
<summary>Ǯ�� ���</summary>

- ������ ���ڸ��� union-find�� ����ϰڴٴ� �����̿Դ�.
- ������, ó�� �õ����� ������� Ǯ������ �ʾƼ� �ϴ� ��Ȯ���� �����ڴ� ������ navie�ϰ� �ݺ����� ���� 0�� ������ ���������� �˻��ؼ� �־��ִ� ������ �Ͽ���.
```python
# naive(��Ȯ��o, ȿ����x)
def solution(k, room_number):
    answer = []
    data = [0 for i in range(k+1)]

    for r in room_number:
        if data[r] == 0:
            data[r] = r
            answer.append(r)
        else:
            rem = r
            while True:
                rem += 1
                if data[rem] == 0:
                    data[rem] = rem
                    answer.append(rem)
                    break
```

- �� ��, ���ͳ��� ã�ƺ� ���, ��ųʸ��� Ȱ���ؼ� �� ��� �ſ� �����ϴٴ� ����� �˰� �����غ��Ҵ�.
- �׸���, ��͸� �̿��Ͽ� ������ Ǯ������ ����� Ƚ�� ������ �� Ǯ������
- parent�� �ش� ���� �̹� ������ �Ǿ� �־� ���� �� ��ȣ�� ����Ű�� �ִ�. �׸��Ͽ� find_parent(parent,parent[x])�� �� ���, ��������� �� ������ �ȳ����ش�.
```python
import sys
sys.setrecursionlimit(10**8)

def find_parent(parent,x):
    if x not in parent:
        parent[x] = x+1
        return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]

def solution(k, room_number):
    answer = []
    parent = {}

    for r in room_number:
        answer.append(find_parent(parent,r))
    return answer
```

</details>

---

## ��Ʈ��ũ

<details>
<summary>Ǯ�� ���</summary>

�������� BFS/DFS �����̴�.

��尡 n�� ��ŭ������ n���� ��带 �˻��ϸ鼭 visited�� False�� node�� �˻��Ҷ� answer+=1���ָ�, �� ���� bfs Ȥ�� dfs�� ���� �湮�� ��带 üũ���ش�. �׷��� ���� ��Ʈ��ũ�� �����ȴ�.

</details>

---

## �� �����ϱ�

<details>
<summary>Ǯ�� ���</summary>

ó������ ���ڸ��� ũ�罺Į �˰����� ���÷ȴ�. �׸��� ������ �����.

�׸��� �ٸ� ������� �ڵ带 ���� �켱���� ť�� �̿��ؼ� Ǭ ������� �ڵ尡 �ִٴ� ����� �˾Ұ�, �̸� �̿��ؼ� Ǯ�� �ٸ� �׸��� �����鵵 ���� Ǯ �� ������ ���ٴ� ������ �����.

</details>

<details>
<summary>�ڵ�(�켱���� ť)</summary>

```python
import heapq

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    pq = []
    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]

    for a,b,c in costs:
        graph[a].append([b,c])
        graph[b].append([a,c])
        heapq.heappush(pq,[c,a,b])

    edges_cnt = 0
    while edges_cnt != n-1:
        c,a,b = heapq.heappop(pq)

        a = find_parent(parent,a)
        b = find_parent(parent,b)

        if a != b:
            union_parent(parent,a,b)
            answer += c
            edges_cnt+=1

    return answer
```

</details>

<details>
<summary>�ڵ�(ũ�罺Į)</summary>

```python
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])

    for a,b,c in costs:
        graph[a].append([b,c])
        graph[b].append([a,c])

    edges_cnt = 0
    for a,b,c in costs:
        if edges_cnt == n-1:
            break
        a = find_parent(parent,a)
        b = find_parent(parent,b)

        if a != b:
            union_parent(parent,a,b)
            answer += c
            edges_cnt += 1

    return answer
```

</details>

---

## �Ա��ɻ�

<details>
<summary>Ǯ�� ���</summary>

ó������ �Է��� ���ڸ� ���� �̺�Ž������ �ذ��ؾ��Ѵٴ� ������ ������� ������ ����� �������� �ʾҴ�. �׷��� �ϴ� naive�ϰ� Ǯ������ ���ó� �׽�Ʈ���̽� ���ݸ� ������ ���߰� �������� �ð��ʰ��� ����. ����� �غ����� Ǯ�� ���ؼ�, ���ͳ��� �ٸ� ����� Ǯ�̹����� ������ Ǯ����.
>���� : https://kdgt-programmer.tistory.com/60

�̺�Ž���� ����� **���� �� �� �ִ� �˻��ð�**�̴�. �׷��Ƿ�, ������ 1 ~ (���� �� �� �ִ� �˻��ð��� �ִ� ����)�̴�. ���⼭ ���� �� �� �ִ� �˻��ð��� �ִ밪�� n*min(times)�̴�.

�� ��, �̺� Ž���� �����ϸ鼭 �� �ɻ�밡 mid �ð��� ������ �� �ִ� ��� ���� ����Ѵ�. 

�� ������� ���� n���� ũ�ų� ���� ��� mid�� ���� �ٿ��� �ϹǷ� right = mid -1�� ���ְ�, �̶��� mid���� answer�� �������ش�. 

�� ������� ���� n���� ���� ��� mid�� ���� �÷��� �ϹǷ� left = mid + 1�� ���ش�.

�׷���, �ڿ������� �ش� ���� ã�� �� �ִ�.

</details>

<details>
<summary>�ڵ�</summary>

```python
def solution(n, times):
    answer = 0
    left = 1
    right = min(times) * n

    while left <= right:
        mid = (left+right)//2
        temp = n

        for t in times:
            temp -= mid//t
            if temp <= 0:
                right = mid - 1
                answer = mid
                break

        if temp >0:
            left = mid + 1

    return answer
```

<details>
<summary>������</summary>

�̺�Ž���� ������ ���� Ǯ����߰ڴ�.

�̺�Ž������ ���� �߿��ϴٰ� �����ϴ� �κ��� **�̺� Ž���� ���**�� ���ؾ��Ѵٴ� ���̴�.

�̷��� �̺� Ž�� ����� ���ϴ� ����� ���������߰ڴ�.

�̺�Ž���� ����� �� �� �ִ� ���� �Է��� N�� ���� �̺�Ž���� ������� �ϰų�, Ȥ�� **���� �� �� �ִ� ��**�� ã�� �͵� �����ϴٴ� ���� �˾Ҵ�.

</details>

</details>

---

## ¡�˴ٸ�

<details>
<summary>��ũ</summary>
https://programmers.co.kr/learn/courses/30/lessons/43236

</details>

<details>
<summary>Ǯ�� ���</summary>

1 <= distance <= 1,000,000,000�� ���� �̺�Ž���� ������ ���ߴ�. �׷��� �Ա��ɻ� ������ ���ø��鼭 �̺�Ž���� ����� ���ϱ�� �ߴ�.

�̺�Ž���� ����� ������ ������ ������� ��Ҵ�. ��, ������ n�� ������ �� �� ���� ������ �Ÿ��� �ּڰ��� ���Ѵ�.

�̺�Ž���� �����ϸ鼭 ������������ rocks�� ����� �������� ������� ���캻��. 

mid ���� �������� ����� prev���� �˻��ϴ� rock�� �Ÿ��� ���Ѵ�.
    - mid > rock - prev
      - �� ���� ������ �����ؾ� �� ������ �ּҰ��� mid���� Ŀ����. �׷��Ƿ�, �ش������ �����Ѵٴ� �ǹ̷� remove_cnt�� +1 ���ش�.
    - mid <= rock - prev
      - �� ���� ������ �����ϸ� �ȵȴٴ� �ǹ̷� prev�� �ش� ������ �����Ͽ� �� �������� �Ÿ��� ��ٴ� �ǹ̷� ��Ÿ����.

�� ������ ���� �� 
    - remove_cnt�� ���� ���� ������ n���� ũ�ٸ� mid ���� �ٿ��� �ϹǷ� right = mid - 1
    - removen_cnt <= n �̸�, answer = mid�� �����ϰ�, mid ���� �÷����ϹǷ� left =mid + 1���ش�.


</details>

<details>
<summary>�ڵ�</summary>

```python
# ¡�˴ٸ�
def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance

    rocks.sort()

    while left <= right:
        mid = (left+right)//2
        remove_cnt = 0
        prev = 0

        for rock in rocks:
            if mid > rock - prev:
                remove_cnt += 1
            else:
                prev = rock

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

print(solution(25,[2, 14, 11, 21, 17],2))
```

</details>

<details>
<summary>������</summary>

�̺� Ž�������� Ž���� ����� ���ϴ� ���̰� �̷��� ����� �ַ� `������ ����`�� �ȴٴ� ���� �˾Ҵ�.

</details>

---

## ��ũ ��Ʈ�ѷ�

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42627

</details>

<details>
<summary>Ǯ�� ���</summary>

�־��� �Է��� jobs_pq�� �켱���� ť�� �����.

now_time�� �ξ jobs_pq�� pop�ϸ鼭 ��ũ�� �޾��� �ð�(jobs[i][0])�� now_time�� �ִٸ� �켱����ť(pq)�� �־��ش�. ����, ���� ���� break�� �ϸ� �ȴ�. �� ��, pq���� �ϳ��� pop�� �� answer += (now_time-job[0]) �� �ϸ� �ȴ�.

�̶�, �ϳ� �����ؾ��� ���� �Ʒ��� ���� �Է��� ���� ���� �ִ�.
> print(solution([[0, 3], [4, 9], [5, 6]]))

�̷� ���, [0,3]�� ó�� ��, now_time�� 3�̵Ǵµ� �� �ȿ� ��� ��찡 �����Ƿ� jobs_pq�� ù��° job�� ������ �� �ش� ���� �ð��� now_time�� ������ְ� �ٽ� jobs_pq�� push ���־���Ѵ�.

</details>

<details>
<summary>������</summary>

�� ������ �׸����� �����ϰ� �ִµ� �׸��������� �켱���� ť�� �̿��Ͽ� ������ Ǯ ��� ������ �� �� �� ���� �� ����.

�ٵ� �ڵ尡 �� ������. �ٸ� ������� Ǭ �ڵ带 ���� ������ �ؾ��� �� ����.

</details>

---

## �߼� Ʈ����

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/17676

</details>

<details>
<summary>Ǯ�� ���</summary>

�� ������ ��� �־��� input�� ���� �ٷ�� ������ ������ ������Ѵ�.

������� �Ʒ��� ���� �Է��� ���Դٰ� �����غ���.
```
[
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
```

�׷��� "2016-09-15 01:00:04.001 2.0s" ���� �⵵-��-���� ��Ÿ���� `2016-09-15` ���ֹ�����, `01:00:04.001`�� �ð��� second�� �ٲ� ǥ���Ѵ�. �׷��� 01*3600 + 00*60 + 04.001 = 3604.001�� �ȴ�. �� �ð��� ������ �ð�(end_time)�� �ǰ�, ������ �ð�(start)�� ���� ���Ͽ���. ������ �ð��� strat_time = round(end_time - float(c[:-1]) + 0.001,3) ���� ��������, end_time���� �ɸ� �ð��� ���� �� �� 0.001�ʸ� ������ߵȴ�.(0~0.999�ʰ� 1�ʵ��� ������ �ð��̱� ������)

�̷��� �Է°����� ��ó�� ��, �������� 1�ʳ� ó������ max ���� ���ؾ��ϴµ�, 1ms�� ������ �˻��ϱ⿡�� ���� �ʹ� ����. �׷��Ƿ�, ������ ����� 1�ʳ��� ó������ ������ �ɷ��� � �κ��� �������̳� �������� ������ �Ͼ�Ƿ� �̷��� �κе鸸 �˻��ϸ�ȴٰ� �����ߴ�. �׷���� �Ʒ��� 5���� ������ �ִٴ� ����� �� �� �ִ�.

![traffic](./readme_img/traffic.JPG)

�� �� 1���� 5�� case�� ������ ��� ���� �ش� �ð��ȿ� ���Ƿ� result+=1�� ���ָ� �ȴ�.

```python
for r in rem:
    r_start, r_end = r
    if r_end < start or r_start > end:
        continue
    result+=1
```

</details>

---

## �ս� �ý� ���

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/72413

</details>

<details>
<summary>Ǯ�̹��(���ͽ�Ʈ��)</summary>

�� ������ ũ�� ����, 
```
S -> (�ս� ����) -> A 
                ->  B
```
�̷��� ����� �� ���� �ּҰ��� ���ϴ� �����̴�.

�׷��Ƿ�, for���� ���� ��� ��带 �˻��ϸ鼭 s->i,i->a,i->b�� ���� ����� ���� �ּҰ� �Ǵ� ��θ� ���ϸ�ȴ�.

�������� ���ͽ�Ʈ�� ����ϴϱ� ����� �߾ȳ� ��Ȳ�ߴ�. �������� ���� ������ʰ� �����ص־߰ڴ�.

</details>

<details>
<summary>Ǯ�̹��(�÷��̵�-����)</summary>

ó������ �÷��̵�-���� �˰������� Ǯ�̸� ������ �׽�Ʈ���̽� 26���� �ð��ʰ��� �޾ƹ��ȴ�. �׷��� ���ͽ�Ʈ��� ������. �ڼ��� ������ ���ͽ�Ʈ�� Ǯ�̰������� �����ϰڴ�.

</details>

---

## ǳ�� ��Ʈ����

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/68646

</details>

<details>
<summary>Ǯ�� ���</summary>

�־��� a ����Ʈ�� �ִ� ���̰� 1,000,000�̴�. �׷��Ƿ�, O(N^2)���� Ǯ ��� �ð��ʰ��� �߻��Ұ� ���� �����̾ O(NlogN)�� ����� ����ߴ�.

ó������ �̺�Ž���� ����غ��� ����������, ǳ���� ��Ʈ���� ���ؼ��� ������ �ϸ� �ȵɰ� ���Ƽ� ���� ���ø� ���� LIS �˰����� �̺�Ž������ �� ��츦 ���÷ȴ�.

�׷��� LIS�� �̿��ؼ� �̸����� ����ϴٰ� �ϳ��� ����� ã�Ƴ´�.

�̺�Ž������ LIS�� �� ��� �ش� ���ڰ� LIS �迭 �������� index�� �� �� �ִ�. �׷��� index�� rem�̶�� ����Ʈ�� �����Ѵ�.

������� �Ʒ��� ���� �Է��� �����ִٰ� �����غ���.
```
[-16,27,65,-2,58,-92,-71,-68,-61,-33]
```

�׷��� rem ����Ʈ���� �Ʒ��� ���� ����ȴ�.
```
[1,2,3,2,3,1,2,3,4,5]
```

�� ��, min = int(1e9)�� �ΰ� �̷��� rem����Ʈ�� �����ʿ��� ���� �˻��Ͽ� min > rem[?] �� ���, answer+=1�� ���ְ� min ���� rem[?]�� �ٲ��ش�. �̶�, rem[?]�� 1�� ���� ������ �����ϴ� ����̹Ƿ� �׳� answer+=1�� ���ָ� ������ �ȴ�.

</details>