# 백준 사이트 문제 풀이

## Q17298

<details>
<summary>오큰수</summary>

- 링크 : https://www.acmicpc.net/problem/17298
- 풀이 방법
  - 스택과 우선순위 큐를 사용해서 풀었다.
  - 앞에서부터 숫자를 읽어오면서 스택이 비어있을 경우 스택에 해당 index를 push해주고, 그 다음 숫자를 읽는다.
  - 이때, 스택의 제일 윗 숫자와 그 다음 숫자를 비교해서 만약 스택의 제일 윗 숫자가 더 작다면 pop()을 해준 뒤 우선순위 큐에 (stack에서 pop된 index, 읽어온 숫자)를 넣어준다.
  - 위 과정을 반복한다.
  - 위 과정이 끝난 후, (stack에 남아 있는 인덱스,-1)를 우선순위 큐에 넣어준다.
  - 그 후, 우선순위 큐를 꺼내면서 값을 출력한다.(인덱스 우선)
- 더 좋은 방법
  - stack안에는 해당 값의 index가 들어가야한다. 처음 입력했을 때 몇번째 index에 위치한 값인지를 넣어야 한다는 말이다. 다시 주어진 예제를 본다면 3 5 2 7에서 처음에 3의 index인 0을 push하고 5에 해당하는 index 1을 넣어줄 때에는 결과 리스트의 index 0에 해당하는 값을 5로 바꿔주고 stack에서는 pop시킨 후에 5에 해당하는 index 1을 push해주면 된다.
  
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
  - 출처: https://suri78.tistory.com/49 [공부노트]

</details>

---

## Q1655

<details>
<summary>가운데를 말해요</summary>

- 링크 : https://www.acmicpc.net/problem/1655
- 풀이 방법
  - 우선순위 큐를 사용하여 중간 값을 기준으로 낮은 값은 max_heap으로 저장하고, 큰 값은 min_heap으로 저장한다. 이때, max_heap의 root가 중간 값으로 생각한다.
  - 새로운 데이터를 push할때 max_heap과 min_heap의 원소 개수가 다르면 max_heap에 넣고, 그 외에는 min_heap에 넣어준다.
  - 그 후, 각각의 heap에의 root를 비교해서 이때 max_heap(즉 left)가 min_heap(즉 right)보다 클 경우 서로의 원소를 바꿔서 저장한 뒤, max_heap의 root를 출력하면 된다.
  <br/>
  ![Q1655](./readme_img/Q1655.JPG)

</details>

---

## Q1300

<details>
<summary>K번째 수</summary>

- 링크 : https://www.acmicpc.net/problem/1300
- 풀이 방법
  - K번째의 숫자를 알아야한다.
  - 이분탐색으로 mid보다 낮은 숫자의 개수를 알아낼 수 있다.
    - 각 row에서 mid보다 낮은 숫자의 개수는 mid//i(이때 i는 1~N)이다.
    - 이 모든 개수를 더하면 mid라는 숫자는 몇번째 위치한지 알 수 있다.
  - 이때, 개수가 같은 숫자가 있을 수 있는데 이때는 최솟값을 찾아야 하므로 result에 mid를 저장한 다음 end = mid - 1 해서 계속 진행한다.
- Binary Search가 끝나면 result를 출력한다.

</details>

---
