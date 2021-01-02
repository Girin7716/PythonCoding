# 파이썬 알고리즘 정리 노트

## 경우의 수

<details>
<summary>순열(Permutations)</summary>

- 순열 : 순서가 상관있는 경우의 수
  
- 2개 순열

    ```python
    from itertools import permutations
    item = ['1','2',1,3,['a','b']]
    print(list(permutations(item,2)))
    ```
    <details>
    <summary>출력</summary>
        [('1', '2'), ('1', 1), ('1', 3), ('1', ['a', 'b']), ('2', '1'), ('2', 1), ('2', 3), ('2', ['a', 'b']), (1, '1'), (1, '2'), (1, 3), (1, ['a', 'b']), (3, '1'), (3, '2'), (3, 1), (3, ['a', 'b']), (['a', 'b'], '1'), (['a', 'b'], '2'), (['a', 'b'], 1), (['a', 'b'], 3)]
    </details>
    <br /><br />

- 3개 순열

    ```python
    from itertools import permutations
    item = ['1','2',1,3,['a','b']]
    print(list(permutations(item,3)))
    ```
    <details>
    <summary>중복된 출력</summary>
        [('1', '2', 1), ('1', '2', 3), ('1', '2', ['a', 'b']), ('1', 1, '2'), ('1', 1, 3), ('1', 1, ['a', 'b']), ('1', 3, '2'), ('1', 3, 1), ('1', 3, ['a', 'b']), ('1', ['a', 'b'], '2'), ('1', ['a', 'b'], 1), ('1', ['a', 'b'], 3), ('2', '1', 1), ('2', '1', 3), ('2', '1', ['a', 'b']), ('2', 1, '1'), ('2', 1, 3), ('2', 1, ['a', 'b']), ('2', 3, '1'), ('2', 3, 1), ('2', 3, ['a', 'b']), ('2', ['a', 'b'], '1'), ('2', ['a', 'b'], 1), ('2', ['a', 'b'], 3), (1, '1', '2'), (1, '1', 3), (1, '1', ['a', 'b']), (1, '2', '1'), (1, '2', 3), (1, '2', ['a', 'b']), (1, 3, '1'), (1, 3, '2'), (1, 3, ['a', 'b']), (1, ['a', 'b'], '1'), (1, ['a', 'b'], '2'), (1, ['a', 'b'], 3), (3, '1', '2'), (3, '1', 1), (3, '1', ['a', 'b']), (3, '2', '1'), (3, '2', 1), (3, '2', ['a', 'b']), (3, 1, '1'), (3, 1, '2'), (3, 1, ['a', 'b']), (3, ['a', 'b'], '1'), (3, ['a', 'b'], '2'), (3, ['a', 'b'], 1), (['a', 'b'], '1', '2'), (['a', 'b'], '1', 1), (['a', 'b'], '1', 3), (['a', 'b'], '2', '1'), (['a', 'b'], '2', 1), (['a', 'b'], '2', 3), (['a', 'b'], 1, '1'), (['a', 'b'], 1, '2'), (['a', 'b'], 1, 3), (['a', 'b'], 3, '1'), (['a', 'b'], 3, '2'), (['a', 'b'], 3, 1)]
    </details>
    <br /><br />

- 순열은 중복이 됨
    ```python
    from itertools import permutations
    op = ['+', '+', '-', '*', '/']
    per = list(permutations(op,len(op)))
    ```
    <details>
    <summary>출력(len=120)</summary>
    [('+', '+', '-', '*', '/'), ('+', '+', '-', '/', '*'), ('+', '+', '*', '-', '/'), ('+', '+', '*', '/', '-'), ('+', '+', '/', '-', '*'), ('+', '+', '/', '*', '-'), ('+', '-', '+', '*', '/'), ('+', '-', '+', '/', '*'), ('+', '-', '*', '+', '/'), ('+', '-', '*', '/', '+'), ('+', '-', '/', '+', '*'), ('+', '-', '/', '*', '+'), ('+', '*', '+', '-', '/'), ('+', '*', '+', '/', '-'), ('+', '*', '-', '+', '/'), ('+', '*', '-', '/', '+'), ('+', '*', '/', '+', '-'), ('+', '*', '/', '-', '+'), ('+', '/', '+', '-', '*'), ('+', '/', '+', '*', '-'), ('+', '/', '-', '+', '*'), ('+', '/', '-', '*', '+'), ('+', '/', '*', '+', '-'), ('+', '/', '*', '-', '+'), ('+', '+', '-', '*', '/'), ('+', '+', '-', '/', '*'), ('+', '+', '*', '-', '/'), ('+', '+', '*', '/', '-'), ('+', '+', '/', '-', '*'), ('+', '+', '/', '*', '-'), ('+', '-', '+', '*', '/'), ('+', '-', '+', '/', '*'), ('+', '-', '*', '+', '/'), ('+', '-', '*', '/', '+'), ('+', '-', '/', '+', '*'), ('+', '-', '/', '*', '+'), ('+', '*', '+', '-', '/'), ('+', '*', '+', '/', '-'), ('+', '*', '-', '+', '/'), ('+', '*', '-', '/', '+'), ('+', '*', '/', '+', '-'), ('+', '*', '/', '-', '+'), ('+', '/', '+', '-', '*'), ('+', '/', '+', '*', '-'), ('+', '/', '-', '+', '*'), ('+', '/', '-', '*', '+'), ('+', '/', '*', '+', '-'), ('+', '/', '*', '-', '+'), ('-', '+', '+', '*', '/'), ('-', '+', '+', '/', '*'), ('-', '+', '*', '+', '/'), ('-', '+', '*', '/', '+'), ('-', '+', '/', '+', '*'), ('-', '+', '/', '*', '+'), ('-', '+', '+', '*', '/'), ('-', '+', '+', '/', '*'), ('-', '+', '*', '+', '/'), ('-', '+', '*', '/', '+'), ('-', '+', '/', '+', '*'), ('-', '+', '/', '*', '+'), ('-', '*', '+', '+', '/'), ('-', '*', '+', '/', '+'), ('-', '*', '+', '+', '/'), ('-', '*', '+', '/', '+'), ('-', '*', '/', '+', '+'), ('-', '*', '/', '+', '+'), ('-', '/', '+', '+', '*'), ('-', '/', '+', '*', '+'), ('-', '/', '+', '+', '*'), ('-', '/', '+', '*', '+'), ('-', '/', '*', '+', '+'), ('-', '/', '*', '+', '+'), ('*', '+', '+', '-', '/'), ('*', '+', '+', '/', '-'), ('*', '+', '-', '+', '/'), ('*', '+', '-', '/', '+'), ('*', '+', '/', '+', '-'), ('*', '+', '/', '-', '+'), ('*', '+', '+', '-', '/'), ('*', '+', '+', '/', '-'), ('*', '+', '-', '+', '/'), ('*', '+', '-', '/', '+'), ('*', '+', '/', '+', '-'), ('*', '+', '/', '-', '+'), ('*', '-', '+', '+', '/'), ('*', '-', '+', '/', '+'), ('*', '-', '+', '+', '/'), ('*', '-', '+', '/', '+'), ('*', '-', '/', '+', '+'), ('*', '-', '/', '+', '+'), ('*', '/', '+', '+', '-'), ('*', '/', '+', '-', '+'), ('*', '/', '+', '+', '-'), ('*', '/', '+', '-', '+'), ('*', '/', '-', '+', '+'), ('*', '/', '-', '+', '+'), ('/', '+', '+', '-', '*'), ('/', '+', '+', '*', '-'), ('/', '+', '-', '+', '*'), ('/', '+', '-', '*', '+'), ('/', '+', '*', '+', '-'), ('/', '+', '*', '-', '+'), ('/', '+', '+', '-', '*'), ('/', '+', '+', '*', '-'), ('/', '+', '-', '+', '*'), ('/', '+', '-', '*', '+'), ('/', '+', '*', '+', '-'), ('/', '+', '*', '-', '+'), ('/', '-', '+', '+', '*'), ('/', '-', '+', '*', '+'), ('/', '-', '+', '+', '*'), ('/', '-', '+', '*', '+'), ('/', '-', '*', '+', '+'), ('/', '-', '*', '+', '+'), ('/', '*', '+', '+', '-'), ('/', '*', '+', '-', '+'), ('/', '*', '+', '+', '-'), ('/', '*', '+', '-', '+'), ('/', '*', '-', '+', '+'), ('/', '*', '-', '+', '+')]    
    </details>

 - 순열의 중복 없애기(set)
    ```python
    from itertools import permutations
    op = ['+', '+', '-', '*', '/']
    per = list(permutations(op,len(op)))
    ```
    <details>
    <summary>출력(len=60)</summary>
    {('*', '+', '+', '-', '/'), ('+', '*', '-', '+', '/'), ('*', '-', '+', '/', '+'), ('+', '/', '+', '-', '*'), ('+', '/', '-', '+', '*'), ('*', '+', '/', '-', '+'), ('-', '*', '/', '+', '+'), ('+', '/', '-', '*', '+'), ('-', '+', '/', '+', '*'), ('-', '+', '/', '*', '+'), ('*', '+', '+', '/', '-'), ('+', '-', '*', '/', '+'), ('-', '/', '+', '*', '+'), ('*', '-', '/', '+', '+'), ('+', '*', '+', '/', '-'), ('/', '-', '*', '+', '+'), ('/', '+', '*', '+', '-'), ('/', '*', '+', '-', '+'), ('+', '+', '*', '/', '-'), ('/', '-', '+', '+', '*'), ('/', '-', '+', '*', '+'), ('+', '-', '+', '/', '*'), ('/', '+', '+', '*', '-'), ('+', '-', '/', '*', '+'), ('*', '/', '-', '+', '+'), ('/', '*', '-', '+', '+'), ('-', '/', '+', '+', '*'), ('+', '+', '/', '*', '-'), ('-', '*', '+', '+', '/'), ('/', '+', '+', '-', '*'), ('-', '+', '+', '*', '/'), ('+', '/', '*', '-', '+'), ('+', '*', '/', '+', '-'), ('-', '+', '*', '+', '/'), ('+', '/', '*', '+', '-'), ('+', '+', '*', '-', '/'), ('+', '+', '-', '*', '/'), ('*', '+', '/', '+', '-'), ('*', '/', '+', '+', '-'), ('/', '*', '+', '+', '-'), ('+', '+', '-', '/', '*'), ('-', '/', '*', '+', '+'), ('+', '-', '/', '+', '*'), ('-', '*', '+', '/', '+'), ('*', '+', '-', '/', '+'), ('/', '+', '-', '+', '*'), ('-', '+', '+', '/', '*'), ('*', '/', '+', '-', '+'), ('+', '*', '-', '/', '+'), ('/', '+', '-', '*', '+'), ('/', '+', '*', '-', '+'), ('+', '/', '+', '*', '-'), ('*', '-', '+', '+', '/'), ('+', '+', '/', '-', '*'), ('+', '-', '*', '+', '/'), ('+', '*', '+', '-', '/'), ('-', '+', '*', '/', '+'), ('*', '+', '-', '+', '/'), ('+', '-', '+', '*', '/'), ('+', '*', '/', '-', '+')}
    </details>

</details>

<details>
<summary>조합(Combinations)</summary>

- 조합 : 순서 상관없는 경우의 수

- 2개 조합

    ```python
    from itertools import combinations
    item = ['1','2',1,3,['a','b']]
    print(list(combinations(item,2)))
    ```
    <details>
    <summary>출력</summary>
    [('1', '2'), ('1', 1), ('1', 3), ('1', ['a', 'b']), ('2', 1), ('2', 3), ('2', ['a', 'b']), (1, 3), (1, ['a', 'b']), (3, ['a', 'b'])]
    </details><br /><br />

- 3개 조합

    ```python
    from itertools import combinations
    item = ['1','2',1,3,['a','b']]
    print(list(combinations(item,3)))
    ```
    <details>
    <summary>출력</summary>
        [('1', '2', 1), ('1', '2', 3), ('1', '2', ['a', 'b']), ('1', 1, 3), ('1', 1, ['a', 'b']), ('1', 3, ['a', 'b']), ('2', 1, 3), ('2', 1, ['a', 'b']), ('2', 3, ['a', 'b']), (1, 3, ['a', 'b'])]
    </details><br /><br />

</details>

<details>
<summary>중복 순열(product)</summary>

- 코드 예시
  - repeat = ? 에서 ?는 몇개 뽑을지에 대한 수
    ```python
    from itertools import product
    n = 4
    print(list(product(['+','-','*','/'],repeat=(n-1))))
    ```
    <details>
    <summary>출력</summary>
        [('+', '+', '+'), ('+', '+', '-'), ('+', '+', '*'), ('+', '+', '/'), ('+', '-', '+'), ('+', '-', '-'), ('+', '-', '*'), ('+', '-', '/'), ('+', '*', '+'), ('+', '*', '-'), ('+', '*', '*'), ('+', '*', '/'), ('+', '/', '+'), ('+', '/', '-'), ('+', '/', '*'), ('+', '/', '/'), ('-', '+', '+'), ('-', '+', '-'), ('-', '+', '*'), ('-', '+', '/'), ('-', '-', '+'), ('-', '-', '-'), ('-', '-', '*'), ('-', '-', '/'), ('-', '*', '+'), ('-', '*', '-'), ('-', '*', '*'), ('-', '*', '/'), ('-', '/', '+'), ('-', '/', '-'), ('-', '/', '*'), ('-', '/', '/'), ('*', '+', '+'), ('*', '+', '-'), ('*', '+', '*'), ('*', '+', '/'), ('*', '-', '+'), ('*', '-', '-'), ('*', '-', '*'), ('*', '-', '/'), ('*', '*', '+'), ('*', '*', '-'), ('*', '*', '*'), ('*', '*', '/'), ('*', '/', '+'), ('*', '/', '-'), ('*', '/', '*'), ('*', '/', '/'), ('/', '+', '+'), ('/', '+', '-'), ('/', '+', '*'), ('/', '+', '/'), ('/', '-', '+'), ('/', '-', '-'), ('/', '-', '*'), ('/', '-', '/'), ('/', '*', '+'), ('/', '*', '-'), ('/', '*', '*'), ('/', '*', '/'), ('/', '/', '+'), ('/', '/', '-'), ('/', '/', '*'), ('/', '/', '/')]
    </details>


</details>

<details>
<summary>두 개 이상의 리스트에서 모든 경우의 수 구하기(product)</summary>

- 제대로 된 쓰임새(*를 붙여야함)

    ```python
    from itertools import product
    items = [['a','b','c'],[1,2,3,4],['!','@']]
    print(list(product(*items)))
    ```
    <details>
    <summary>출력</summary>
    [('a', 1, '!'), ('a', 1, '@'), ('a', 2, '!'), ('a', 2, '@'), ('a', 3, '!'), ('a', 3, '@'), ('a', 4, '!'), ('a', 4, '@'), ('b', 1, '!'), ('b', 1, '@'), ('b', 2, '!'), ('b', 2, '@'), ('b', 3, '!'), ('b', 3, '@'), ('b', 4, '!'), ('b', 4, '@'), ('c', 1, '!'), ('c', 1, '@'), ('c', 2, '!'), ('c', 2, '@'), ('c', 3, '!'), ('c', 3, '@'), ('c', 4, '!'), ('c', 4, '@')]
    </details><br /><br />

- 잘못된 쓰임새

    ```python
    from itertools import product
    items = [['a','b','c'],[1,2,3,4],['!','@']]
    print(list(product(items)))
    ```
    <details>
    <summary>출력</summary>
    [(['a', 'b', 'c'],), ([1, 2, 3, 4],), (['!', '@'],)]
    </details><br /><br />

    </details>

___
<br />

## 우선순위 큐(Priority Queue)

<details>
<summary>정의</summary>

- 우선순위 큐는 데이터를 추가한 순서대로 제거하는 FIFO 특성을 가진 일반적인 큐와는 달리, 데이터 추가는 어떤 순서로해도 상관이 없지만, 제거될 때는 가장 작은 값(우선 순위가 높은) 제거하는 자료구조이다.

</details>

<details>
<summary>파이썬에서의 구현</summary>

- heapq 라이브러리와 PriorityQueue 라이브러리가 있다
  - 하지만 heapq가 더 빠르게 동작한다. (대신, thread-safe 보장 안함)
- 파이썬에서는 Min Heap을 제공하지만, Max Heap은 제공하지 않는다.
  - 따라서 heapq 라이브러리를 이용하여 Max Heap을 구현해야 할 때는 원소에 (-1)를 곱해줌으로서 부호를 반전 시켜서 사용한다.
- O(N), O(NlogN)
- 삽입
  - heapq.heappush()
- 삭제(원소 꺼내기)
  - heapq.heappop()
- 예제> Heap Sort
    ```python
    import heapq

    def heapsort(iterable):
        h = []
        result = []
        # 모든 원소를 차례대로 힙에 삽입
        for value in iterable:
            heapq.heappush(h,value) # min heap
            #heapq.heappush(h,-value)   # max heap
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        # min heap
        for i in range(len(h)):
            result.append(heapq.heappop(h))
        # max heap  #[-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
        # for i in range(len(h)):
        #   result.append(-heapq.heappop(h))
        return reseult
    
    result = heapsort([1,3,5,7,9,2,4,6,8,0])
    print(result)
    ```
    - 결과>
      - [0,1,2,3,4,5,6,7,8,9] # min heap
      - [9,8,7,6,5,4,3,2,1,0] # max heap

</details>

___
<br />

## 파이썬 내장 함수
<details>
<summary>수학 수식 계산(eval())</summary>

- eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과 반환.

    ```python
        result = eval("(3+5)*7")
        print(result)
    ```
    <details>
    <summary>출력</summary>

    - 56
  
    </details>

</details>

<details>
<summary>리스트 정렬(sorted())</summary>

- sorted() : iterable 객체가 들어왔을 때, 정렬된 결과 반환/
- key 속성으로 정렬 기준 명시 가능
- reverse = 정렬된 결과 리스트를 뒤집을지 여부 설정

    ```python
        result = sorted([9,1,8,5,4])
        print(result)
        result = sorted([9,1,8,5,4], reverse = True)
        print(result)
    ```
    
    <details>
    <summary>출력</summary>

    - [1, 4, 5, 8, 9]
    - [9, 8, 5, 4, 1]

    </details>

</details>

<details>
<summary>리스트 두번째 key 기준으로 정렬하기(sorted())</summary>

- 리스트의 원소로 리스트나 튜플이 존재할 때, 특정한 기준에 따라서 정렬을 수행할 수 있다.
- 정렬 기준은 key 속성을 이용해 명시 가능.

    ```python
        result = sorted([('홍길동',35),('이순신',75),('아무개',50)], key= lambda x:x[1], reverse=True)
        print(result)
    ```

    <details>
    <summary>출력</summary>

    - [('이순신', 75), ('아무개',50), ('홍길동', 35)]

    </details>

</details>

---
<br />

## bisect(이진 탐색)
<details>
<summary>biset(이진탐색)</summary>

- bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적.
- bisect_left(a, x)
  - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 method
- bisect_right(a, x)
  - 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 method
- 위 두 method는 O(logN).
  - 사용 예시
    ```python
    from bisect import bisect_left, bisect_right

    a = [1,2,4,4,8]
    x = 4

    print(bisect_left(a,x))
    print(bisect_right(a,x))
    ```
    <details>
    <summary>출력</summary>
    2<br/>
    4
    </details>

- 위 두 method는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용 가능.
  - 사용 예시
    ```python
    from bisect import bisect_left, bisect_right

    # 값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
    def count_by_range(a, left_value, right_value):
        right_index = bisect_right(a,right_value)
        left_index = bisect_left(a,left_value)
        return right_index - left_index

    # 리스트 선언
    a = [1,2,3,3,3,3,4,4,8,9]
    # 값이 4인 데이터 개수 출력
    print(count_by_range(a,4,4))
    # 값이 [-1,3] 범위에 있는 데이터 개수 출력
    print(count_by_range(a,-1,3))
    ```
    
    <details>
    <summary>출력</summary>
    2<br/>
    6
    </details>

</details>

<details>
<summary>이진 탐색 직접 구현 함수</summary>

```python
def count_by_value(array,x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array,x,0,n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array,x,0,n-1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    # 중간값의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 화깅ㄴ
    elif array[mid] >= target:
        return first(array,target,start,mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array,target,mid+1,end)

def last(array,target,start,end):
    if start>end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid==n-1 or target<array[mid+1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array,target,start,mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array,target,mid+1,end)
```

</details>


<details>
<summary>이진 탐색 & 파라메트릭 서치(Parametric Search)</summary>

- 파라메트릭 서치
  - 최적화 문제(문제의 상황을 만족하는 특정 변수의 최솟값, 최댓값을 구하는 문제)를 결정 문제('예 혹은 '아니오'로 답하는 문제')로 바꾸어 해결하는 기법.
  - '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치 사용.
  - ex> 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.
  - https://sarah950716.tistory.com/16 -> 예제

</details>

---
<br />

## 정렬(sort)

<details>
<summary>lambda(key 정렬 정의)</summary>

- ```python
    data.sort(key=lambda x : (-x[1], x[2], -x[3],x[0]))
  ```
  - 이런식으로 정렬 정의 가능
  - -x[1] : 두번째 key를 내림차순으로 정렬.
  - x[2] : 세번째 key를 오름차순으로 정렬.


- 예제
    ```python
    N = int(input())
    data = []
    for i in range(N):
        # 이런식으로 하나하나 받을 수 있음
        name, korean, english, math = input().split()
        data.append([name,int(korean),int(english),int(math)])

    # 의미
    # 1. 국어 점수가 감소하는 순서로
    # 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
    # 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
    # 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 옵니다.)
    data.sort(key=lambda x : (-x[1], x[2], -x[3],x[0]))
    for i in range(N):
        print(data[i][0])
    # input
    # 12
    # Junkyu 50 60 100
    # Sangkeun 80 60 50
    # Sunyoung 80 70 100
    # Soong 50 60 90
    # Haebin 50 60 100
    # Kangsoo 60 80 100
    # Donghyuk 80 60 100
    # Sei 70 70 70
    # Wonseob 70 70 90
    # Sanghyun 70 70 80
    # nsj 80 80 80
    # Taewhan 50 60 90
    ```
    
    <details>
    <summary>출력</summary>
    Donghyuk <br />
    Sangkeun <br />
    Sunyoung <br />
    nsj <br />
    Wonseob<br />
    Sanghyun<br />
    Sei<br />
    Kangsoo<br />
    Haebin<br />
    Junkyu<br />
    Soong<br />
    Taewhan<br />
    </details>

</details>

---
<br />

## 리스트 다루기(list)

<details>
<summary>리스트 슬라이싱(리스트 원소 뒤집기 가능)</summary>

- 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때 슬라이싱(Slicing) 사용.
- 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 (끝 인덱스 -1)을 설정할 수 있다.
- ex>
```python
a = [1,2,3,4,5,6,7,8,9,10]
print(a[3:5])
print(a[:4])
print(a[7:])
```
<details>
<summary>출력</summary>
[4,5]<br />
[1,2,3,4]<br />
[8,9,10]<br />
</details>

- a[:] == a
- a[::2] == step(간격)을 2로 해서 뽑아내기
    ```python
    print(a[::2])
    ```
    <details>
    <summary>출력</summary>
    [1,3,5,7,9]
    </details>
- a[-1::-2] == 마지막 요소부터 시작해서 앞으로 하나 건너 하나씩 요소를 가져오기.
    ```python
    print(a[-1::-2])
    ```
    <details>
    <summary>출력</summary>
    [10,8,6,4,2]
    </details>
- ex2>
    ```python
    print(a[1::])
    print(a[-1::])
    print(a[-1::-1])
    print(a[-1::-2])
    print(a[1::-2])
    ```
    <details>
    <summary>출력</summary>
    [2, 3, 4, 5, 6, 7, 8, 9, 10] <br />
    [10]<br />
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]<br />
    [10, 8, 6, 4, 2]<br />
    [2]<br />
    </details>

</details>

<details>
<summary>list.count(x) x 개수 세기</summary>

- list.count(x)를 사용하면 해당 list안에 x가 몇개 있는지 return한다.
- O(N)
```python
    a = ['a','b','c','c','c','d','d']
    b = [1,1,2,2,2,2,3,7,7,8,8,8]
    print(a.count('c'))
    print(b.count('b'))
```
<details>
<summary>출력</summary>
3<br />
3
</details>

- 만약 정렬된 리스트에서 count를 구할때 더 빠르게 구하고 싶다면 bisect를 이용하면 O(logN)으로 구할 수 있다.
```python
from bisect import bisect_left, bisect_right
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

a = ['a','b','c','c','c','d','d']
b = [1,1,2,2,2,2,3,7,7,8,8,8]
print(count_by_range(a,'c','c'))
print(count_by_range(b,8,8))
```
<details>
<summary>출력</summary>
3<br />
3
</details>

</details>

---
<br />

## input()관련


<details> 
<summary>여러 값 input()으로 받기</summary>

- 한 line에 서로 다른 형태의 값들을 받기

- 예제
    ```python
    N = int(input())
    data = []
    for i in range(N):
        # 이런식으로 하나하나 받을 수 있음
        name, korean, english, math = input().split()
        data.append([name,int(korean),int(english),int(math)])

    #f = sorted(e, key = lambda x : (x[0], -x[1]))
    data.sort(key=lambda x : (-x[1], x[2], -x[3],x[0]))
    for i in range(N):
        print(data[i][0])
    # input
    # 12
    # Junkyu 50 60 100
    # Sangkeun 80 60 50
    # Sunyoung 80 70 100
    # Soong 50 60 90
    # Haebin 50 60 100
    # Kangsoo 60 80 100
    # Donghyuk 80 60 100
    # Sei 70 70 70
    # Wonseob 70 70 90
    # Sanghyun 70 70 80
    # nsj 80 80 80
    # Taewhan 50 60 90
    ```
  
</details>


<details>
<summary>input() 속도 높이기 sys.stdin.readline</summary>

- 사용 문구

    ```python
    import sys
    input = sys.stdin.readline
    ```

- 사용예시

    ```python
    import sys
    input = sys.stdin.readline

    N,C = map(int,input().split())
    data = []
    for i in range(N):
        data.append(int(input()))
    data.sort()
    ```

</details>

<details>
<summary>한 줄 문자열 -> 2차원 리스트로 input()</summary>

- 예시
```python
for tc in range(int(input())):  # 테스트 케이스 입력 2
    n,m = map(int,input().split())  # 3 4
    array = list(map(int,input().split()))  # 1 3 3 2 2 1 4 1 0 6 4 7

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m]) # 한 줄 문자열(1차원 리스트) -> 2차원 리스트로 바꾸기
        index += m
```

</details>

---


<!--
코드 - 출력  markdown 형식

- 부제목

    ```python
    ```
    <details>
    <summary>출력</summary>
    </details><br /><br />
 -->

