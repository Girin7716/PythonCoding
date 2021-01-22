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