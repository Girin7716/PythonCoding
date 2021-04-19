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

---

## [īī�� ����]Ű�е� ������

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/67256

</details>

<details>
<summary>Ǯ�� ���</summary>

�� �������� �ٽ��� 2,5,8,0�̶�� ���ڰ� �������� �޼հ� ������ �� ���� �հ������� �������ϴ����� ���� ó���� �߿��ϴٰ� �����ߴ�.

�־��� Ű�е忡�� ���� ó���ϱ� ���ϰ� `*`�� `10`���� `0`�� `11`�� `#`�� `12`�� �ٲ㼭 ó���Ͽ���.

�־��� �Է��� �տ������� �����鼭(now), now%3==0�̸� ������, now%3==1�̸� �޼��� �������ϸ� ���������� ������ ��ġ�� �ش��ϴ� ��ȣ�� �����Ͽ���.

�׸��� now%3==2�̸�, �̴� ����� �����⶧���� �޼հ� �������� �� ��ġ�߿��� ����� �հ����� �������ϸ� ���� �Ÿ��� ��쿡�� hand�� ���� ���� �޶�����.

������ �հ����� now�� ��ġ���� �Ÿ��� ���ϴ� ����� �Ʒ��� ����.
```python
left_dist = (int((abs(now-left_location)/3))) + abs(now-left_location)%3
right_dist = (int((abs(now - right_location) / 3))) + abs(now-right_location)%3
```
�̶� `(int((abs(now-location)/3)))`�� �ش� �հ����� now�� ���η� ��ĭ ���̳����� ��Ÿ����, `abs(now-location)%3`�� �ش� �հ����� now�� ���η� ��ĭ ���̳������� ��Ÿ����.

�ش� dist�� ���ϰ� ���ٸ� hand�� ���� ������ ó���� �ٸ��� �ϸ�ȴ�.

Ǯ�ٰ����ϱ�, dist���ϴ� ���� �Լ�ȭ�ϸ� �� ���������Ű��ٴ°��� ���޾Ҵ�.

</details>

---

## [īī�� ����] ���� �ִ�ȭ

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/67257

</details>

<details>
<summary>Ǯ�̹��</summary>

eval()�� �̿��Ͽ� ������ �ذ��ߴ�.

�������, "100-200*300-500+20" �̶�� input�� ������ �Ʒ��� ���� ����Ʈȭ �����ش�.(end�� ���� �ǹ�)

```python
['100', '-', '200', '*', '300', '-', '500', '+', '20', 'end']
```

�� ��, �����ڴ� +,-,* 3���̹Ƿ� �̵��� ������ ���ؼ� ����Ž���ϸ� �ȴ�.
```python
prior = permutations(['+','-','*'],3)
```

�� ����, ������ �켱������ �°� ex_list�� ó������ �˻��ϸ鼭 ���� ���ٸ� �ش� ������ �� �ڷ� ���ڷ� ���� eval()�� �� ����Ʈ�� ���� �ٽ� ������ָ� �ȴ�.
```python
ex_list = ex_list[:idx-1]+[str(eval(''.join((ex_list[idx-1:idx+2]))))]+ex_list[idx+2:]
```

���� Ž���ϸ鼭 answer�� max���� ���ϸ� �ȴ�.
```python
answer = max(answer,abs(int(ex_list[0])))
```

</details>

---

## ���� �˻�

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/72412

</details>

<details>
<summary>Ǯ�� ���</summary>

������ ��Ȯ���� �䱸�ϴ� ������ �ϴ� ����Ž���� dictionary�� ���÷ȴ�.

�׸��� ���,����,���,�ҿ�Ǫ���� ����� ���� ���� ��� �̿� ���� ��� ����� ���� dictionary�� key�� �־��־���.
```python
dict_keys(['jbjp', 'jbjc', 'jbj-', 'jbsp', 'jbsc', 'jbs-', 'jb-p', 'jb-c', 'jb--', 'jfjp', 'jfjc', 'jfj-', 'jfsp', 'jfsc', 'jfs-', 'jf-p', 'jf-c', 'jf--', 'j-jp', 'j-jc', 'j-j-', 'j-sp', 'j-sc', 'j-s-', 'j--p', 'j--c', 'j---', 'pbjp', 'pbjc', 'pbj-', 'pbsp', 'pbsc', 'pbs-', 'pb-p', 'pb-c', 'pb--', 'pfjp', 'pfjc', 'pfj-', 'pfsp', 'pfsc', 'pfs-', 'pf-p', 'pf-c', 'pf--', 'p-jp', 'p-jc', 'p-j-', 'p-sp', 'p-sc', 'p-s-', 'p--p', 'p--c', 'p---', 'cbjp', 'cbjc', 'cbj-', 'cbsp', 'cbsc', 'cbs-', 'cb-p', 'cb-c', 'cb--', 'cfjp', 'cfjc', 'cfj-', 'cfsp', 'cfsc', 'cfs-', 'cf-p', 'cf-c', 'cf--', 'c-jp', 'c-jc', 'c-j-', 'c-sp', 'c-sc', 'c-s-', 'c--p', 'c--c', 'c---', '-bjp', '-bjc', '-bj-', '-bsp', '-bsc', '-bs-', '-b-p', '-b-c', '-b--', '-fjp', '-fjc', '-fj-', '-fsp', '-fsc', '-fs-', '-f-p', '-f-c', '-f--', '--jp', '--jc', '--j-', '--sp', '--sc', '--s-', '---p', '---c', '----'])
```
- �̶�

```python
rem = [['j','p','c','-'],['b','f','-'],['j','s','-'],['p','c','-']]
for x in list(product(*rem)):
    info_dict[''.join(x)] = []
```

�̷������� �ڵ带 ����������, �������� product�� ����ؼ� ������Ʈ�� ���� ����ϴ°� �����ߴ�.

�� ��, �Է����� �־��� infos�� ���� ���� ���·� �ٲٰ� �� 16���� ���� '-'�� ��ġ�� ���ڸ� key�� �־��ְ� ������ value�� �־��־���.

```python
for info in infos:
    rem = info.split()
    string = ''
    for i in range(5):
        if i == 4:
            for k in range(5):
                for j in combinations(range(1,5),k):
                    temp = list(string)
                    for x in j:
                        temp[x-1] = '-'
                    info_dict[''.join(temp)].append(int(rem[i]))
        string+=rem[i][0]
```

�׷��� key�� �ش��ϴ� �������� �����Ǿ��ִµ� �̸� ����Ž������ ������ �ľ��ϱ� ���ؼ� ������������ sorting���־���.

```python
for key in info_dict.keys():
    info_dict[key].sort()
```
����������, �Է����� �־��� query�� ���� ���� ��ó�� ��, �ش� key�� �ش��ϴ� (value ����Ʈ ���� - query���� �־��� ����)�� answer�� �߰����ָ� �ȴ�.

```python
for qry in query:
    temp = qry.split(' and ')
    temp = temp[:3] + temp[3].split()
    score = temp[4]
    string = ''
    for i in range(4):
        string+=temp[i][0]
    answer.append(len(info_dict[string])-bisect_left(info_dict[string],int(score)))
```

</details>

<details>
<summary>������</summary>

1. dictionary�� Ȱ���ϴ� ���� �ͼ�������.
2. combination, products ������ �ͼ�������.

</details>

---

## [2021 īī��]�ű� ���̵� ��õ

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/72410

</details>

<details>
<summary>Ǯ�� ���</summary>

�׳� ������ �°� ������� �����ߴ�.

�ٵ� ���࿡ ���ڿ� ó���� ���ڰ� �Ǿ������ index ó���� ��ٷο�� �־ check�ϴ°��� �߰��ؼ� �˻���.

</details>

<details>
<summary>������</summary>

�׳� ������ �°� ������� �����ߴ�.

�ٵ� ���߿� ã�ƺ��ϱ� `���Խ�`�̶�°��� �ִٴ°��� �˾Ҵ�.

�����ϸ� ���ҵ�...?

</details>

---

## [2021 īī��] �޴� ������

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/72411

</details>

<details>
<summary>Ǯ�� ���</summary>

�Է����� �־����� orders�� ���� ������ ������ ���ش�(�������ϱ� �� �ʿ� ���µ�)

�� ���� �Է����� �־��� course�� ���Ҹ�ŭ orders�� ���ҿ� combination�� ���Ѵ�. �̶�, order�� ���ĺ������� ��ġ�Ǿ���Ѵ�. �׸���, �ش� combination�� key�� ������ ��ųʸ��� �����ؼ� ������ count�Ѵ�.
```python
order = ''.join(list(sorted(list(order))))
rems = list(combinations(order,c))
for rem in rems:
    comb[rem] = comb.get(rem,0) + 1
```

�� ��, comb�� ���� �� ��ųʸ��� continue, �ƴ� ��� max_value�� Ȯ���ؼ� 1�ϰ�� continue, �� ���� ���� max_value�� ���� ���� ������ key�� answer�� �߰����ָ� �ȴ�.

</details>

---

## ���� ����

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/72414

</details>

<details>
<summary>Ǯ�� ���</summary>

ó�� Ǯ���� �ð��ʰ��� � ���� ��Ǯ����.. �ᱹ ���ͳ��� �����ϰ� �������̶�� ���� ����Ѵٴ� ���� �˰� �ڵ� �м��� �غ����� �Ѵ�.

```python
def makeSecond(time):
    time = time.split(':')
    second = int(time[0])*3600+int(time[1])*60+int(time[2])
    return second

def makeTime(second):
    h=second//3600
    m=(second-(h*3600))//60
    s=(second-(h*3600)-(m*60))
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
```
- �ϴ� ����ϱ� ���ϰ� ���ڿ��� ������ time�� ������ second�� �ٲ��ִ� �۾�(makeSecond)�� ������ second�� �ٽ� ���ڿ� time���� �ٲ��ִ� �۾�(makeTime)�� �����ߴ�.

```python
def solution(play_time, adv_time, logs):
    answer =''
    play_time = makeSecond(play_time)
    adv_time = makeSecond(adv_time)

    # ��û�� �� �޸�
    memo = [0 for _ in range(play_time+1)]
    for log in logs:
        start, end = log.split('-')
        start = makeSecond(start)
        end = makeSecond(end)

        memo[start] += 1
        memo[end] -= 1

    # ���� ��û�� �� �޸�
    # 1) ���� ��û�� ��
    for i in range(1,play_time+1):
        memo[i] = memo[i] + memo[i-1]
    # 2) ���� ��û�� ��
    for i in range(1,play_time+1):
        memo[i] = memo[i] + memo[i-1]

    max_play = memo[adv_time-1]
    start = 0
    for i in range(adv_time,play_time):
        play = memo[i] - memo[i-adv_time]

        if play > max_play:
            max_play = play
            start = i - adv_time+1
    answer=makeTime(start)

    return answer
```
- ��ü�ڵ��̰� �ϳ��ϳ��� �м��غ��ڴ�.

```python
play_time = makeSecond(play_time)
adv_time = makeSecond(adv_time)
```
- ����ϱ� ���ϰ� ������ second�� �ٲٱ�.

```python
# ��û�� �� �޸�
memo = [0 for _ in range(play_time+1)]
for log in logs:
    start, end = log.split('-')
    start = makeSecond(start)
    end = makeSecond(end)

    memo[start] += 1
    memo[end] -= 1
```
- �ð��� �� ��û�ڼ��� ����ϱ� ���� memo ����Ʈ�� �����ؼ� log�� start ������ end ������ ǥ�ø� �صд�(start : +1, end : -1)

```python   
# ���� ��û�� �� �޸�
# 1) ���� ��û�� ��
for i in range(1,play_time+1):
    memo[i] = memo[i] + memo[i-1]
# 2) ���� ��û�� ��
for i in range(1,play_time+1):
    memo[i] = memo[i] + memo[i-1]
```
- memo ����Ʈ�� ���� ���������� ����Ŵ�.
- sum(memo[start:end])�� ����� ��� �־��� ��� O(N^2)�� �ɸ�����, �������� ����� ��� O(N)���� ���� �� �ְԵȴ�.
- 1)������ memo �����z �Ʒ��� ���� ������ ���̴�.
```
memo : [0,0,0,1,1,1,1,1,1,1,-1,...]
```
- 2)�� �۾��� ���ָ� �Ʒ��� ����.
```
memo : [0,0,0,1,2,3,4,5,6,7,6,...]
```

```python
max_play = memo[adv_time-1]
start = 0
for i in range(adv_time,play_time):
    play = memo[i] - memo[i-adv_time]

    if play > max_play:
        max_play = play
        start = i - adv_time+1
answer=makeTime(start)
```
- �̷��� �������� ���ϰ� �Ǹ� ���� ������ ã�� �� �ִ�.
- �ʱ�ȭ : start = 0��, max_play : ���� 0�ʿ� �����ؼ� �������� ������
- �ð����� �������� �˸� ������� �ð��� �� �� �����ϱ�, adv_time���� �˻��ؼ� play_time���� for���� ������ȴ�.
- �׷��� ���� �������� ū �κ��� �ð��� �����ؼ� ������ָ��.

</details>

---

## �ڹ���� ����

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/60059

</details>

<details>
<summary>Ǯ�� ���</summary>

����� �˰ڴµ� ������ �����ߴ�.. �׷��� ���ͳݿ� �˻��ؼ� �� ����� �ڵ带 �м��ϴ� �������� ������.

```python
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]
```
- lock�� ���踦 ���ϴ� ����

```python
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]
```
- lock�� ���踦 ���� ����

```python
def rotate90(arr):
    return list(zip(*arr[::-1]))
```
- ���踦 90�� ȸ���ϴ� ����

```python
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False;
    return True
```
- lock�� Ȯ���ؼ� �������� Ȯ���ϴ� ����

```python
def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    # �ڹ��� �߾� ��ġ
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    rotated_key = key
    # ��� ���� (4�� ����)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M + N):
            for y in range(1, M + N):
                # ���� �־��
                attach(x, y, M, rotated_key, board)
                # lock ���� check
                if (check(board, M, N)):
                    return True
                # ���� ����
                detach(x, y, M, rotated_key, board)

    return False
``` 

</details>

---

## ���� �� ���

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/49189

</details>

<details>
<summary>Ǯ�̹��</summary>

```python
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
number = [0] * (n + 1)
for edge in edges:
    a,b = edge
    graph[a].append(b)
    graph[b].append(a)
```
- �׷��� ����

```python
q = deque()
q.append(1)
visited[1] = True
max_value = 0

while q:
    now = q.popleft()
    for i in graph[now]:
        if visited[i] is True:
            continue
        visited[i] = True
        q.append(i)
        number[i] = number[now] + 1
        if number[i] > max_value:
            max_value = number[i]
```
- ������ �׷����� �������� bfs ����
- �̶�, �Ÿ��� �˾ƾ��ϹǷ� �湮�� ����� �Ÿ��� �˱� ���ؼ� `number[i] = number[now]+1`�� �߰����༭ �Ÿ��� �ľ�
- ����, ���߿� ���� �� ��带 ã�� ���ؼ� max���� �߰��� update

```python
for n in number:
    if n == max_value:
        answer+=1
```
- ���� �� ����� �Ÿ��� �ش��ϴ� ����� ���� �ľ�

</details>

---

## ����Ʈ�ٹ�

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42579

</details>

<details>
<summary>Ǯ�̹��</summary>

```python
# ����Ʈ�ٹ�
import heapq

def solution(genres, plays):
    answer = []
    bestMusic = {}  # key: genres, value: �ش� �帣�� ������ plays�� ���ҷΰ����� �켱���� ť(MaxHeap)
    totalplay = {}  # key: genres, value: plays�� ����

    # input�� �������� ��ųʸ� ����
    for i in range(len(genres)):
        totalplay[genres[i]] = totalplay.get(genres[i],0) + plays[i]
        try:
            heapq.heappush(bestMusic[genres[i]], (-plays[i], i))
        except:
            bestMusic[genres[i]] = [(-plays[i], i)]

    # value: plays�� ������ �������� ������������ ����
    totalplay = sorted(totalplay, key=lambda x: totalplay[x],reverse=True)

    # ������������ ���ĵ� totalplay�� �ϳ��� ���鼭
    for t in totalplay:
        # bestMusic �帣�� �ش��ϴ� answer�� Maxheap���� pop�Ѵ�(�̶�, 2��° ���Ҵ� minheap�̴ϱ� ���� ������ �ε����� �������Ұ� ����), 2���̻��̸� �׸�.
        for i in range(len(bestMusic[t])):
            if i == 2:
                break
            answer.append(heapq.heappop(bestMusic[t])[1])

    return answer
```
- ��ü�ڵ�

</details>

---

## �ٸ��� ������ Ʈ��

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42583

</details>

<details>
<summary>Ǯ�̹��</summary>

�ٸ��� ���� �ִ� Ʈ���� �ð��� ���� �������� ǥ���ϱ� ���� �Ʒ��� ���� ����Ʈ�� �����ߴ�.
```python
onBridge = deque([0] * (bridge_length))
```

�� ��, input���� �־��� truck_weights�� ť�� �ٲ� �� �տ������� �ϳ��� Ʈ���� popleft�ϸ鼭 onBridge���� �ִ� Ʈ���� �� ���԰� �ٸ��� �ߵ� �� �ִ� ���Զ�� Ʈ���� �ø���, �ƴ� ��쿡�� �ø��� �ʴ´�.
```python
while truck_weights:
    answer+=1
    outTruck = onBridge.popleft()
    sumOnBridge -= outTruck
    if sumOnBridge + truck_weights[0] <= weight:
        onBridge.append(truck_weights.popleft())
        sumOnBridge += onBridge[-1]
    else:
        onBridge.append(0)
```

�׷��� ������ Ʈ���� �ٸ��� �ö��ڸ��� while���� ����Ǵµ� �� ���� ������ Ʈ���� �ٸ��� �ǳʴ� ������ �� �ɸ� �ð��̹Ƿ� �Ʒ��� ���� �۾��� ���ָ� �ȴ�.
```python
answer+=bridge_length
```

</details>

---

## �ֽİ���

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42584

</details>

<details>
<summary>Ǯ�̹��</summary>

ó������ �׳� ���߹ݺ������� Ǯ������ �ð��ʰ�..

�׷����ؼ� �ð��� ���̰��� ������ ����� deque�� ����ϴ°��̴�.

```python
answer = [0] * (len(prices))
q = deque()
index = -1
for price in prices:
    index+=1
    if q == deque():
        q.append((price,index))
        continue

    while q != deque():
        if q[-1][0] > price:
            p,i = q.pop()
            answer[i] = index-i
        else:
            break
    q.append((price,index))
```
- answer�� prices���̸�ŭ 0���� �ʱ�ȭ�����ش�
- prices�� ���ʴ�� ���캸�鼭
- q�� ����ִٸ� (price,index)�� �־��ְ� ���� price�� Ȯ���Ѵ�.
- q�� ������ ���Ұ� price���� Ŭ ��� �̴� �ֽİ����� �϶��ߴٴ� �ǹ��̹Ƿ� pop()�� �ؼ� ���������Ҹ� ���� �� �ش� ������ index���� ������� `answer[i] = index -i`�� ���ָ�ȴ�. �׸��� �̸� �ݺ��ϸ鼭 ������ ���Ұ��� price���� �۰ų� ������ �׸��θ� �ȴ�.(�ֳ��ϸ� q���� �׻� �ֽİ����� �����ϴ� ���� �������̱� ����)
- �׸��� ���������� q�� (price,index)�� �־��ָ� �ȴ�.

```python
last_p,last_i = q.pop()
while q:
    p,i = q.popleft()
    answer[i] = last_i-i

return answer
```
- �� �κ���, q�� �����ִ� �κ��� ó���ϴ� ���̴�.
- q�� �����ִٴ� �ǹ̴� q�� ���Ҹ� ���� �������� ������ ������ ����ߴٴ� �ǹ̿� ����.
- �׷��� q�� �տ������� popleft()�ϰ�, last_i-i�� �ϸ�ȴ�.

</details>

---

## �� �ʰ�

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42626

</details>

<details>
<summary>Ǯ�̹��</summary>

1. �־��� scoville�� minHeap���� ������ش�
2. pq�� ������������� �ݺ����� �ݺ��Ѵ�
3. ù��° ���Ҹ� ����� �� ���� K ���� ũ�ų� ���� ��� minHeap�� ��� ���Ҵ� K���� ũ�ų� ���� ������ �׸��д�.
4. Ȥ�� ù��° ���Ҹ� �����µ� pq�� ����ִٸ� �̴� minHeap�� ��� ���Ұ� scoville���� �۴ٴ� �ǹ��̹Ƿ� -1�� ��ȯ�ϸ� �ȴ�.
5. �� ���� ���� �ι�° ���Ҹ� ������ ���ں� ��꿡 ���� ����ϰ� �ش� ���� minHeap�� �־��ְ� answer+=1�� �Ѵ�.

</details>

---

## �Ҽ� ã��

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42839

</details>

<details>
<summary>Ǯ�̹��</summary>

�־��� numbers���� ���� ������ ��� ���ڿ� ���ؼ� �Ҽ����� �Ǻ��ϴ� �����̴�.

�׷��� �ϴ� numbers�� ���̸� ���ؼ� �����佺�׳׽��� ü �˰����� ����Ͽ� �ִ� numbers�� ���̸�ŭ�� �� �� �Ҽ��� ���߰� �̸� dictionary�� key�� value�� True ���� �־��־���.

�� ��, numbers�� permutations���� ����Ž���Ͽ� ���ڵ��� ���ϰ� ���� ���ڰ� dictionary�� key�̸鼭 value�� True�̸� �Ҽ��� ���̴�(�̶� ���� value�� False��� �̴� ����Ž������ ���� ���ڰ� �ߺ��Ǿ ���Դٴ� ���� �ǹ��ؼ� answer+=1�� �ϸ� �ȵȴ�.)

</details>

---

## ����

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/49191

</details>

<details>
<summary>Ǯ�̹��</summary>

ó������ �������ķ� Ǯ����� ������ ������. �׷��� ���ͳݿ��� �����ϴ� `�̱�Ƚ�� + �� Ƚ�� == n-1`�� �� ��� ������ Ȯ���� �� �ִٴ� ����� �˰� �̸� �����ؼ� graph�� �ΰ� ���� bfs�� ���� ���� ���ϰ� �Ǿ���.

```python
# ����
from collections import deque

def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n+1)]   # Parent:�� ���, Child : �̱���
    loser = [[] for _ in range(n+1)]    # Parent:�̱���, Child : �� ���
    total = [0] * (n+1) # �� ���� ������ �̱�� �� Ƚ���� �� ��

    for result in results:
        a,b = result
        loser[b].append(a)
        winner[a].append(b)

    def bfs(graph,i):
        q = deque()
        q.append(i)
        visited = [False] * (n+1)

        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if visited[nxt] is True:
                    continue
                visited[nxt] = True
                total[i] += 1
                q.append(nxt)

    # �� �������� �̱�� �� ȸ�� bfs�� ���ϱ�
    for i in range(1,n+1):
        bfs(winner,i)
        bfs(loser,i)

    # total�� ���� n-1�̸� ������ Ȯ���� ���̹Ƿ� ���� �ľ�
    for t in total:
        if t == n-1:
            answer+=1

    return answer
```

</details>

---

## H-Index

<details>
<summary>��ũ</summary>

https://programmers.co.kr/learn/courses/30/lessons/42747

</details>

<details>
<summary>Ǯ�̹��</summary>

���� �����ϴ°͵� �������.

���ø� ���� [3, 0, 6, 1, 5]���� ������ h���� ���ϴ� ���� �����̴�.

�̶�, h�� h�� �̻� �ο�� ���� h�� �̻��̰� ������ ���� h�� ���� �ο�Ǿ����� h�� �ִ��̴�.

��, [3, 0, 6, 1, 5] �������� sorting�� �ϸ� [0, 1, 3, 5, 6]�� �ǰ� h�� 2,3,4�϶��� ����
- 2���̻� �ο� -> 3,5,6 (2�� �̻� �ο�� ���� 2�� �̻�)
- 2������ �ο� -> 0,1 (2�� ���� �ο�� ���� 2�� ����)
  - h�� 2�� ���� ����
- 3���̻� �ο� -> 3,5,6 (3�� �̻� �ο�� ���� 3�� �̻�)
- 3������ �ο� -> 0,1,3 (3�� ���� �ο�� �빮�� 3�� ����)
  - h�� 3�� ���� ����
- 4���̻� �ο� -> 5,6(4�� �̻� �ο�� ���� 4�� �̻��� �ƴ�)
  - h�� 4�� �� ����

�׷��Ƿ�, �� ���ÿ����� h�� �ִ��� 4�� �ȴ�.

```python
answer = 0
length = len(citations)
citations.sort()
for i in range(length):
    if citations[i] >= length - i:
        answer = length - i
        break
```
- ������������ ���ĵ� citations�� �ϳ��ϳ� ���鼭, `�ش� ������ �� >= �ش� ���Ҹ� �����ؼ� ���� ������ ����` �̸� h�� �ִ��� `���� ������ ����`�� ���� �� �ִ�.


```python
# H-Index
def solution(citations):
    answer = 0
    length = len(citations)
    citations.sort()
    for i in range(length):
        if citations[i] >= length - i:
            answer = length - i
            break

    return answer
```


</details>