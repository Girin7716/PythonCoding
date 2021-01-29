# 프로그래머스 사이트 문제 풀이

## 완주하지 못한 선수

<details>
<summary>풀이</summary>

- participant를 key로 해당 이름을 가지는 사람의 수를 value로 지정했다. 그리하여 completion에서 한명씩 이름을 보아서 dictionary에서 차감한 뒤 나중에 dictionary에 value를 1을 가진 사람이 있으면 그 사람은 혼자 완주하지 못한 사람으로 생각하고 출력하였다.

</details>

<details>
<summary>코드</summary>

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

## 전화번호 목록

<details>
<summary>풀이</summary>

  - 접두어를 찾으면 그 즉시 종료를 하고 answer에 False를 넣어야한다. 그러므로 주어진 phone_book 리스트를 길이 순으로 정렬을 한 후, 앞에서부터 그 뒤에 있는 모든 문자열의 앞부분만을 비교하여 만약 찾을경우 answer False를 넣고 종료한다.
  - 만약 종료를 하지않고 계속 실행할 경우 효율성 탈락

</details>


<details>
<summary>코드</summary>

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

## 징검다리 건너기

<details>
<summary>링크</summary>

-  https://programmers.co.kr/learn/courses/30/lessons/64062
</details>

<details>
<summary>풀이 방법</summary>

  - 처음 푼 방법
    - k만큼의 window를 설정한 뒤, stones를 window만큼 보면서 window안 가장 큰 값을 기억한다. 이런식으로 stones를 전부 보면 기억한 값 중 가장 작은 값이 정답이다.
    - 하지만 이는, 정확성에서는 다맞아도, 효율적이지 못하다(O(N^2))이기때문.
  - 두번째로 푼 방법
    - O(N^2)보다 더 좋게 풀어야한다. 그래서 O(NlogN)으로 풀기위해 이진탐색을 생각했다.
    - 이진탐색 대상은 몇명이 건널 수 있냐로 설정했고 min=1,max=200,000,000으로 한 뒤, stones를 처음부터 끝까지 보는 와중 min~max 사이의 수가 3번 이상 나오면 max 값을 줄여주고(max = mid), 만약 전부다 통과할 경우 min값을 늘려준다(min = mid).
    - 이러한 과정을 통해서, 결국 마지막에는 max = mid 후 break문에 들어가서 while의 조건인 min < max -1을 벗어나 탈출하며 return max를하면 정답이 나온다.

</details>
---

## 불량 사용자

<details>
<summary>링크</summary> 

- https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

</details>

<details>

<summary>풀이 방법</summary>

- 처음 푼 방법
  - user_id를 글자수에 따라 digit 리스트에 넣어준다.
  - 그 후, banned_id의 원소들을 처음부터 하나씩 비교하면서, 해당 banned_id와 조건이 부합한 user_id를 rem에 넣어준다.
  - 그 다음, rem에서 리스트간의 product를 하고, 원소들을 정렬시킨 뒤 넣어준다.
  - 그 후 rem을 하나씩 보면서 똑같은 id가 있으면 이를 결과에서 제거한다.
  - 그러면 제거가 끝나고 남은 answer가 정답이다.
  - 하지만, test case5에서 시간초과 발생.(근데 또 이상한게 다른 case들에서의 시간은 엄청 빠르게 동작)
  ![baduser](./readme_img/baduser.JPG)

  <details>
  <summary>코드</summary>

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
- 두번째로 푼 방법
  - 처음 user_id로부터 가능한 순열들을 구한다.
  - 그 후, 각 문자들이 banned_id와 조건이 부합한지 검사를 하며 부합할 경우 해당 candidate_users를 set으로 묶은 후 해당 set이 rem 리스트 안에 없을 경우 rem안에 넣어준다.
  - 모든 순열들을 검사한 뒤, rem의 길이를 반환하면 정답이다.
  - 이거는 방법1)보다는 대체적으로 느리지만, 테스트 5는 통과하는 모습이다.
  - ![baduser2](./readme_img/baduser2.JPG)
  
  <details>

  <summary>코드</summary>

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

## 호텔 방 배정

<details>
<summary>링크</summary>

- https://programmers.co.kr/learn/courses/30/lessons/64063

</details>


<details>
<summary>풀이 방법</summary>

- 문제를 보자마자 union-find를 써야하겠다는 느낌이왔다.
- 하지만, 처음 시도때는 마음대로 풀리지가 않아서 일단 정확도라도 맞추자는 식으로 navie하게 반복문을 통해 0이 나오지 않을때까지 검사해서 넣어주는 식으로 하였다.
```python
# naive(정확도o, 효율성x)
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

- 그 후, 인터넷을 찾아본 결과, 딕셔너리를 활용해서 할 경우 매우 간편하다는 사실을 알고 응용해보았다.
- 그리고, 재귀를 이용하여 문제를 풀때에는 재귀의 횟수 제한을 꼭 풀어주자
- parent는 해당 방은 이미 예약이 되어 있어 다음 방 번호를 가리키고 있다. 그리하여 find_parent(parent,parent[x])를 할 경우, 재귀적으로 빈 방으로 안내해준다.
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