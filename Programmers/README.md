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