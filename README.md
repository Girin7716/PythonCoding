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
    <summary>출력</summary>
        [('1', '2', 1), ('1', '2', 3), ('1', '2', ['a', 'b']), ('1', 1, '2'), ('1', 1, 3), ('1', 1, ['a', 'b']), ('1', 3, '2'), ('1', 3, 1), ('1', 3, ['a', 'b']), ('1', ['a', 'b'], '2'), ('1', ['a', 'b'], 1), ('1', ['a', 'b'], 3), ('2', '1', 1), ('2', '1', 3), ('2', '1', ['a', 'b']), ('2', 1, '1'), ('2', 1, 3), ('2', 1, ['a', 'b']), ('2', 3, '1'), ('2', 3, 1), ('2', 3, ['a', 'b']), ('2', ['a', 'b'], '1'), ('2', ['a', 'b'], 1), ('2', ['a', 'b'], 3), (1, '1', '2'), (1, '1', 3), (1, '1', ['a', 'b']), (1, '2', '1'), (1, '2', 3), (1, '2', ['a', 'b']), (1, 3, '1'), (1, 3, '2'), (1, 3, ['a', 'b']), (1, ['a', 'b'], '1'), (1, ['a', 'b'], '2'), (1, ['a', 'b'], 3), (3, '1', '2'), (3, '1', 1), (3, '1', ['a', 'b']), (3, '2', '1'), (3, '2', 1), (3, '2', ['a', 'b']), (3, 1, '1'), (3, 1, '2'), (3, 1, ['a', 'b']), (3, ['a', 'b'], '1'), (3, ['a', 'b'], '2'), (3, ['a', 'b'], 1), (['a', 'b'], '1', '2'), (['a', 'b'], '1', 1), (['a', 'b'], '1', 3), (['a', 'b'], '2', '1'), (['a', 'b'], '2', 1), (['a', 'b'], '2', 3), (['a', 'b'], 1, '1'), (['a', 'b'], 1, '2'), (['a', 'b'], 1, 3), (['a', 'b'], 3, '1'), (['a', 'b'], 3, '2'), (['a', 'b'], 3, 1)]
    </details>
    <br /><br />

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

<!--
코드 - 출력  markdown 형식

- 부제목

    ```python
    ```
    <details>
    <summary>출력</summary>
    </details><br /><br />
 -->