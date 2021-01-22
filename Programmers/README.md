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