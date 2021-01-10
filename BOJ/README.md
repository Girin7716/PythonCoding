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
